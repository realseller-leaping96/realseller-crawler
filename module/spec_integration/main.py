##############################################
#           상세스펙 통합테이블 백업코드    #
#        phone_spec_test 테이블             #
#############################################
import pandas as pd
import numpy as np
from module.spec_integration.comunication_standard import find_comm_stand
from module.spec_integration.operation_system import find_os
from module.spec_integration.display_inch import find_disp_inch
from module.spec_integration.display_centi import find_display_centi
from module.spec_integration.display_resolution import find_display_resol
from module.spec_integration.display_panel import find_display_panel
from module.spec_integration.pixel_per_inch import find_ppi
from module.spec_integration.display_aspect_ratio import find_display_ratio
from module.spec_integration.ap_type import find_ap_type
from module.spec_integration.num_core import find_core_num
from module.spec_integration.clock_core import find_core_clock
from module.spec_integration.gpu_core import find_gpu_core
from module.spec_integration.sensor_hub import find_sensor_hub
from module.spec_integration.modem import find_modem
from module.spec_integration.ram import find_ram
from module.spec_integration.builtin_memory import find_builitin_memory
from module.spec_integration.external_memory import find_external_memory
from module.spec_integration.front_camera import find_front_camera
from module.spec_integration.back_camera import find_back_camera
from module.spec_integration.front_video_resolution import find_front_video_resol
from module.spec_integration.flash import find_flash
from module.spec_integration.photo_resolution import find_photo_resolution
from module.spec_integration.camera_aperture import find_camera_aperture
from module.spec_integration.fingerprint import find_fingerprint
from module.spec_integration.face import find_face
from module.spec_integration.charging_terminal import find_charging_terminal
from module.spec_integration.bluetooth import find_bluetooth
from module.spec_integration.usim_type import find_usim_type
from module.spec_integration.battery import find_battery
from module.spec_integration.battery_type import find_battery_type1,find_battery_type2,find_battery_type3
from module.spec_integration.wireless_charge import find_wireless_charge
from module.spec_integration.size import find_height,find_thickness,find_weight,find_width
from module.spec_integration.release_date import find_release_date
from module.spec_integration.color import find_color
from module.spec_integration.payment import find_payment
import module.db_module as db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)

def spec_integration(new_index_list):

    db_class = db_module.Database() #db연결 생성

    cetizen = pd.read_sql_table('g5_phone_spec_cetizen',db_class.engine_conn)
    danawa = pd.read_sql_table('g5_phone_spec_danawa',db_class.engine_conn)
    namu = pd.read_sql_table('g5_phone_spec_namu',db_class.engine_conn)
    phone_list = pd.read_sql_table('g5_phone_list',db_class.engine_conn)
    phone_spec_test = pd.read_sql_table('phone_spec_test',db_class.engine_conn)

    num = len(phone_list)
    for i in new_index_list:
        if True:
            cetizen_row =  cetizen[cetizen['sc_model_code'] == phone_list.iloc[i]['pl_model_code'] ]
            danawa_row = danawa[danawa['sd_model_code'] == phone_list.iloc[i]['pl_model_code'] ]
            namu_row = namu[namu['sn_model_code'] == phone_list.iloc[i]['pl_model_code'] ]

            model_name = phone_list.iloc[i]['pl_model_name']
            model_code = phone_list.iloc[i]['pl_model_code']
            maker = phone_list.iloc[i]['pl_maker']
            price = phone_list.iloc[i]['pl_price']
            
            
            communication_standard = find_comm_stand(cetizen_row,danawa_row,namu_row)#통신규격
            os = find_os(cetizen_row,danawa_row,namu_row)#운영체제
            display_in = find_disp_inch(cetizen_row,danawa_row,namu_row)#화면인치
            display_cm = find_display_centi(display_in)#화면센치
            display_resolution = find_display_resol(cetizen_row,danawa_row,namu_row)#화면해상도
            display_type = find_display_panel(cetizen_row,danawa_row,namu_row)#패널종류
            display_ppi = find_ppi(cetizen_row,danawa_row,namu_row)#ppi
            display_aspect_ratio = find_display_ratio(cetizen_row,danawa_row,namu_row,display_resolution) #화면비
            ap_type = find_ap_type(cetizen_row,danawa_row,namu_row)#AP 종류
            core = find_core_num(cetizen_row,danawa_row,namu_row)#코어수
            core_clock = find_core_clock(namu_row,cetizen_row,danawa_row)#코어클럭
            gpu_core = find_gpu_core(namu_row,cetizen_row,danawa_row)#그래픽코어
            sensor_hub = find_sensor_hub(namu_row,cetizen_row,danawa_row)#sensor_hub
            modem = find_modem(namu_row,cetizen_row,danawa_row)#modem
            ram = find_ram(namu_row,cetizen_row,danawa_row)#ram
            Builtin_memory = find_builitin_memory(cetizen_row,danawa_row,namu_row)#Builtin_memory
            external_memory = find_external_memory(namu_row,danawa_row,cetizen_row)#external_memory
            front_camera = find_front_camera(namu_row,danawa_row,cetizen_row)#front_camera
            back_camera = find_back_camera(namu_row,danawa_row,cetizen_row,front_camera)#back_camera
            front_video_resolution = find_front_video_resol(namu_row,danawa_row,cetizen_row)#front_video_resolution
            flash = find_flash(namu_row,danawa_row,cetizen_row)#flash
            photo_resolution = find_photo_resolution(namu_row,danawa_row,cetizen_row)#photo_resolution
            camera_aperture = find_camera_aperture(namu_row,danawa_row,cetizen_row)#camera_aperture
            fingerprint = find_fingerprint(namu_row,danawa_row,cetizen_row)#fingerprint
            face = find_face(namu_row,danawa_row,cetizen_row)#face
            charging_terminal = find_charging_terminal(namu_row,danawa_row,cetizen_row)#charging_terminal
            bluetooth = find_bluetooth(namu_row,danawa_row,cetizen_row)#bluetooth
            usim_type = find_usim_type(namu_row,danawa_row,cetizen_row)#usim_type
            battery = find_battery(namu_row,danawa_row,cetizen_row)#battery
            battery_type1 = find_battery_type1(namu_row,danawa_row,cetizen_row)#battery_type1, 배터리타입(종류)
            battery_type2 = find_battery_type2(namu_row,danawa_row,cetizen_row)#battery_type2 배터리특징 (충전기술 및 와트)
            battery_type3 = find_battery_type3(namu_row,danawa_row,cetizen_row)#battery_type3, 배터리장착방식
            wireless_charge = find_wireless_charge(namu_row,danawa_row,cetizen_row)#wireless_charge
            thickness = find_thickness(danawa_row,cetizen_row,namu_row)#thickness
            width = find_width(namu_row,danawa_row,cetizen_row)#width
            height = find_height(namu_row,danawa_row,cetizen_row)#height
            weight = find_weight(namu_row,danawa_row,cetizen_row)#weight
            release_date = find_release_date(namu_row,danawa_row,cetizen_row)#release_date
            color = find_color(namu_row,danawa_row,cetizen_row)#color
            payment = find_payment(namu_row,danawa_row,cetizen_row)#payment
            
            
            integration_row = {
                'model_name':phone_list.iloc[i]['pl_model_name'], 
                'model_code':phone_list.iloc[i]['pl_model_code'], 
                'maker':phone_list.iloc[i]['pl_maker'], 
                'communication_standard':communication_standard,
                'os':os, 
                'display_in':display_in, 
                'display_cm':display_cm,
                'display_resolution':display_resolution, 
                'display_type':display_type, 
                'display_ppi':display_ppi,
                'display_aspect_ratio':display_aspect_ratio, 
                'ap_type':ap_type, 
                'core':core, 
                'core_clock':core_clock,
                'gpu_core':gpu_core,
                'sensor_hub':sensor_hub, 
                'modem':modem, 
                'ram':ram, 
                'Builtin_memory':Builtin_memory, 
                'external_memory':external_memory,
            'front_camera':front_camera, 
                'back_camera':back_camera, 
                'front_video_resolution':front_video_resolution, 
                'flash':flash,
            'photo_resolution':photo_resolution, 
                'camera_aperture':camera_aperture, 
                'fingerprint':fingerprint, 
                'face':face,
            'charging_terminal':charging_terminal,
                'bluetooth':bluetooth,
                'usim_type':usim_type, 
                'battery':battery,
            'battery_type1':battery_type1,
                'battery_type2':battery_type2,
                'battery_type3':battery_type3,
                'wireless_charge':wireless_charge,
            'thickness':thickness,
                'width':width, 
                'height':height, 
                'weight':weight, 
                'price':price, 
                'release_date':release_date,
                'country':"한국", 
                'color':color,
                'payment':payment
            }

            phone_spec_test = phone_spec_test.append(pd.DataFrame(integration_row, index=[0]))
        pass


    pst = len(phone_spec_test)
    phone_spec_test.replace("",np.NaN,inplace=True)
    phone_spec_test.iloc[pst-len(new_index_list):pst].to_sql(name='phone_spec', con=db_class.engine, if_exists='append', index=False)
    db_class.db_conn.close()
    db_class.engine_conn.close()