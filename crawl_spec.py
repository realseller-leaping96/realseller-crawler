import pandas as pd
from module.spec.namuwiki.detail_df_init import df_init #출력할 데이터 프레임 형식 정의 =>  DataFrame 리턴
import module.spec.cetizen.main as cetizen # 세티즌 스펙크롤러
import module.spec.namuwiki.main as namu # 나무위키 스펙크롤러
import module.spec.danawa.main as danawa # 다나와 스펙크롤러
import pandas as pd
import numpy as np
import module.db_module as db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)
import module.chrome_driver_module as chrome_driver_module #크롬드라이버 연결 정의모듈 (버전,경로 로컬환경따라 다름)
from module.spec_integration.main import spec_integration

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver

   ####################################################
  #           기종 URL 확보 크롤링 코드                # 
 #   입력:phone_list 테이블 출력:url_list 테이블      #
####################################################
try: 
    with db_class.db_conn.cursor() as cursor:
        sql =( """
                        CREATE TABLE if not exists `phone_spec` (
                `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
                `model_name` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `model_code` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `maker` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `communication_standard` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `os` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `display_in` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `display_cm` VARCHAR(50) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
                `display_resolution` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `display_type` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `display_ppi` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `display_aspect_ratio` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `ap_type` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `core` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `core_clock` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `gpu_core` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `sensor_hub` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `modem` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `ram` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `Builtin_memory` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `external_memory` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `front_camera` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `back_camera` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `front_video_resolution` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `flash` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `photo_resolution` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `camera_aperture` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `fingerprint` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `face` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `charging_terminal` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `bluetooth` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `usim_type` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `battery` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `battery_type1` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `battery_type2` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `battery_type3` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `wireless_charge` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `thickness` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `width` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `height` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `weight` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `price` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `release_date` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `country` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `color` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                `payment` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                PRIMARY KEY (`id`) USING BTREE
            )
            COLLATE='latin1_swedish_ci'
            ENGINE=InnoDB
            AUTO_INCREMENT=0
            ;
            """
             )
        cursor.execute(sql)

    db_class.db_conn.commit()
finally:
    pass

phone_list = pd.read_sql_table('g5_phone_list',db_class.engine_conn) #최신버전 g5_phone_list 테이블 로드
phone_spec = pd.read_sql_table('phone_spec',db_class.engine_conn) #최신버전 g5_phone_spec 테이블 로드

new_code_list = []
new_index_list = []
for i, row in phone_list.iterrows():
    index = i
    phone_list_row = row.copy()
    is_new = True
    for i, row in phone_spec.iterrows():
        if phone_list_row['pl_model_code'] == row['model_code']:
            is_new = False
    
    if is_new:
        new_code_list.append(phone_list_row['pl_model_code'])
        new_index_list.append(index)

crawl_code_list = phone_list[phone_list['pl_model_code'].isin(new_code_list)]
num = len(crawl_code_list) 
URL = pd.DataFrame(dict(),index=[0])
URL_cetizen = cetizen.URL(crawl_code_list,driver,URL,0,num) #세티즌사이트 URL 확보하기
URL_danawa = danawa.URL(crawl_code_list,driver,URL,0,num) #다나와사이트 URL 확보하기
URL_namu = namu.URL(crawl_code_list,driver,URL,0,num) #나무위키사이트 URL 확보하기

join_keys = ['pl_model_code','pl_maker','pl_id','pl_name','pl_model_name'] #URL 데이터 조인
df_OUTER_JOIN = pd.merge(URL_danawa, URL_cetizen, left_on=join_keys, right_on=join_keys, how='outer')
df_OUTER_JOIN = pd.merge(df_OUTER_JOIN,URL_namu, left_on=join_keys, right_on=join_keys, how='outer')
df_OUTER_JOIN = df_OUTER_JOIN.drop(df_OUTER_JOIN.columns[0], axis=1)
df_OUTER_JOIN.dropna(subset=['pl_maker'], inplace=True)


try: 
    #url_list 테이블이 없다면 생성해주는 코드
    with db_class.cursor as cursor:
        sql =( "CREATE TABLE if not exists `url_list` (`url_id` INT(11) NOT NULL AUTO_INCREMENT,"+
              "`pl_maker` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`pl_model_code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`pl_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`pl_model_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`나무링크` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`세티즌링크` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`다나와링크` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "PRIMARY KEY (`url_id`) USING BTREE"+
              ")COLLATE='utf8mb4_general_ci'"+
              "ENGINE=InnoDB;" 
             )
        cursor.execute(sql)

    db_class.db_conn.commit()

finally:
    db_class.db_conn.close()

#확보된 url들을 url_list 테이블에 밀어넣기
df_OUTER_JOIN.to_sql(name='url_list', con=db_class.engine, if_exists='append', index=False)

# print("HeidiSQL틀고 url_list 테이블에서 하위 'new'개의 행에 대해서 빈셀 있을경우 수기로 채우기")
# print("--------다 마쳤으면 enter를 누르시오-------------")
# input()


   ###########################################################################
  #               스펙 크롤링 코드                                           #
 #   입력:url_list 테이블 / 출력:g5_phone_spec_cetizen,danawa,namu 테이블   #
##########################################################################

df_input = pd.read_sql_table('url_list',db_class.engine)#입력 파일 로드
df_output = df_init()#출력 형식 로드
driver = chrome_driver_module.ChromeDriver().driver

crawl_url_list = df_input[df_input['pl_model_code'].isin(new_code_list)]
num = len(crawl_url_list) 
df_output = namu.add(crawl_url_list, driver, df_output,0,num)#나무위키 상세스펙 크롤링
driver = chrome_driver_module.ChromeDriver().driver
df_output = cetizen.add(crawl_url_list, driver, df_output,0,num)#세티즌 상세스펙 크롤링
df_output = danawa.add(crawl_url_list, driver, df_output,0,num)#다나와 상세스펙 크롤링
df_output = df_output.drop(["카메라 특징"], axis=1)#결과데이터에서 불필요한 컬럼 삭제
if "생체인식" in df_output.columns:
    df_output = df_output.drop(["생체인식"], axis=1)

##############################################################################################
#                                 DB 백업코드                                                #
#            g5_phone_spec_namu / g5_phone_spec_namu /g5_phone_spec_namu 테이블              #
##############################################################################################

#불필요한 열 삭제
df_complete_review = df_output.drop(["타겟제품"], axis=1) 
df_namu = df_complete_review[df_complete_review['사이트명'] == '나무위키'].drop(["사이트명"], axis=1) #
df_cetizen = df_complete_review[df_complete_review['사이트명'] == '세티즌'].drop(["사이트명"], axis=1)
df_danawa = df_complete_review[df_complete_review['사이트명'] == '다나와'].drop(["사이트명"], axis=1)

#컬럼명 맞춰주기 & 빈셀 NULL처리
sn_columns = ["sn_model_name","sn_model_code",
"sn_maker","sn_release_date","sn_os","sn_sale_type",
"sn_display_cm","sn_display_in","sn_display_type",
"sn_display_resolution","sn_display_ppi","sn_display_hz",
"sn_display_aspect_ratio","sn_display_size","sn_display_width",
"sn_display_height","sn_display_hdr","sn_ap_type","sn_core",
"sn_core_clock","sn_gpu_core","sn_npu_dsp","sn_sensor_hub",
"sn_modem","sn_ram","sn_Builtin_memory","sn_storage",
"sn_external_memory","sn_5g","sn_4g","sn_wifi","sn_bluetooth",
"sn_satellite","sn_usim_type","sn_dual_usim","sn_camera_type",
"sn_back_camera","sn_front_camera","sn_camera_resolution",
"sn_flash","sn_photo_resolution","sn_front_resolution","sn_front_video_resolution",
"sn_camera_aperture","sn_hand_tremor_correction","sn_hand_tremor_protection",
"sn_camera_flash","sn_hdr_filming","sn_auto_hdr","sn_optical_zoom","sn_geotag",
"sn_laser_auto_focus","sn_auto_focus","sn_out_focus","sn_touch_focus","sn_panorama",
"sn_tof","sn_night_photography","sn_iphone_terminal","sn_speaker","sn_high_sound_quality",
"sn_sound_technology","sn_fingerprint","sn_face","sn_iris","sn_voice","sn_ai","sn_payment",
"sn_touch_pen","sn_dustproof","sn_etc","sn_charging_terminal","sn_battery","sn_battery_type1",
"sn_battery_type2","sn_battery_type3","sn_battery_terminal","sn_fast_charge","sn_wireless_charge",
"sn_color","sn_width","sn_height","sn_thickness","sn_weight"]
sc_columns = ["sc_model_name","sc_model_code","sc_maker","sc_release_date",
"sc_os","sc_sale_type","sc_display_cm","sc_display_in","sc_display_type",
"sc_display_resolution","sc_display_ppi","sc_display_hz",
"sc_display_aspect_ratio","sc_display_size","sc_display_width",
"sc_display_height","sc_display_hdr","sc_ap_type","sc_core","sc_core_clock",
"sc_gpu_core","sc_npu_dsp","sc_sensor_hub","sc_modem","sc_ram",
"sc_Builtin_memory","sc_storage","sc_external_memory","sc_5g","sc_4g",
"sc_wifi","sc_bluetooth","sc_satellite","sc_usim_type","sc_dual_usim",
"sc_camera_type","sc_back_camera","sc_front_camera","sc_camera_resolution",
"sc_flash","sc_photo_resolution","sc_front_resolution",
"sc_front_video_resolution","sc_camera_aperture","sc_hand_tremor_correction",
"sc_hand_tremor_protection","sc_camera_flash","sc_hdr_filming","sc_auto_hdr",
"sc_optical_zoom","sc_geotag","sc_laser_auto_focus","sc_auto_focus",
"sc_out_focus","sc_touch_focus","sc_panorama","sc_tof","sc_night_photography",
"sc_iphone_terminal","sc_speaker","sc_high_sound_quality","sc_sound_technology",
"sc_fingerprint","sc_face","sc_iris","sc_voice","sc_ai","sc_payment","sc_touch_pen",
"sc_dustproof","sc_etc","sc_charging_terminal","sc_battery","sc_battery_type1",
"sc_battery_type2","sc_battery_type3","sc_battery_terminal","sc_fast_charge",
"sc_wireless_charge","sc_color","sc_width","sc_height","sc_thickness","sc_weight"]
sd_columns = ["sd_model_name","sd_model_code","sd_maker","sd_release_date",
"sd_os","sd_sale_type","sd_display_cm","sd_display_in","sd_display_type",
"sd_display_resolution","sd_display_ppi","sd_display_hz",
"sd_display_aspect_ratio","sd_display_size","sd_display_width",
"sd_display_height","sd_display_hdr","sd_ap_type","sd_core",
"sd_core_clock","sd_gpu_core","sd_npu_dsp","sd_sensor_hub","sd_modem",
"sd_ram","sd_Builtin_memory","sd_storage","sd_external_memory","sd_5g",
"sd_4g","sd_wifi","sd_bluetooth","sd_satellite","sd_usim_type",
"sd_dual_usim","sd_camera_type","sd_back_camera","sd_front_camera",
"sd_camera_resolution","sd_flash","sd_photo_resolution",
"sd_front_resolution","sd_front_video_resolution","sd_camera_aperture",
"sd_hand_tremor_correction","sd_hand_tremor_protection","sd_camera_flash",
"sd_hdr_filming","sd_auto_hdr","sd_optical_zoom","sd_geotag",
"sd_laser_auto_focus","sd_auto_focus","sd_out_focus","sd_touch_focus",
"sd_panorama","sd_tof","sd_night_photography","sd_iphone_terminal",
"sd_speaker","sd_high_sound_quality","sd_sound_technology",
"sd_fingerprint","sd_face","sd_iris","sd_voice","sd_ai","sd_payment",
"sd_touch_pen","sd_dustproof","sd_etc","sd_charging_terminal","sd_battery",
"sd_battery_type1","sd_battery_type2","sd_battery_type3","sd_battery_terminal",
"sd_fast_charge","sd_wireless_charge","sd_color","sd_width","sd_height",
"sd_thickness","sd_weight"]
df_namu.columns = sn_columns
df_cetizen.columns = sc_columns
df_danawa.columns = sd_columns
df_cetizen = df_cetizen.replace("", np.NaN)
df_namu = df_namu.replace("", np.NaN)
df_danawa = df_danawa.replace("", np.NaN)

#각각 사이트에 해당하는 테이블에 백업
df_namu.to_sql(name='g5_phone_spec_namu', con=db_class.engine, if_exists='append', index=False)
df_cetizen.to_sql(name='g5_phone_spec_cetizen', con=db_class.engine, if_exists='append', index=False)
df_danawa.to_sql(name='g5_phone_spec_danawa', con=db_class.engine, if_exists='append', index=False)

#db연결 종료
db_class.engine_conn.close()

#스펙통합테이블 작업
spec_integration(new_index_list)