import pandas as pd
import pymysql
import pandas as pd
from sqlalchemy import create_engine

a = pd.read_csv("test0414_s (1).csv")

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

#detail_list에 백업
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
a.to_sql(name='detail_list', con=engine, if_exists='append', index=False)



# connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')

# try:
#     with connection.cursor() as cursor:
#         #세티즌
#         cetizen_sql =( "INSERT INTO g5_phone_spec_cetizen (sc_model_name,sc_model_code,sc_maker,sc_release_date,sc_os,sc_sale_type,sc_display_cm,sc_display_in,sc_display_type,sc_display_resolution,sc_display_ppi,sc_display_hz,sc_display_aspect_ratio,sc_display_size,sc_display_width,sc_display_height,sc_display_hdr,sc_ap_type,sc_core,sc_core_clock,sc_gpu_core,sc_npu_dsp,sc_sensor_hub,sc_modem,sc_ram,sc_Builtin_memory,sc_storage,sc_external_memory,sc_5g,sc_4g,sc_wifi,sc_bluetooth,sc_satellite,sc_usim_type,sc_dual_usim,sc_camera_type,sc_back_camera,sc_front_camera,sc_camera_resolution,sc_flash,sc_photo_resolution,sc_front_resolution,sc_front_video_resolution,sc_camera_aperture,sc_hand_tremor_correction,sc_hand_tremor_protection,sc_camera_flash,sc_hdr_filming,sc_auto_hdr,sc_optical_zoom,sc_geotag,sc_laser_auto_focus,sc_auto_focus,sc_out_focus,sc_touch_focus,sc_panorama,sc_tof,sc_night_photography,sc_iphone_terminal,sc_speaker,sc_high_sound_quality,sc_sound_technology,sc_fingerprint,sc_face,sc_iris,sc_voice,sc_ai,sc_payment,sc_touch_pen,sc_dustproof,cs_etc,cs_charging_terminal,sc_battery,sc_battery_type1,sc_battery_type2,sc_battery_type3,sc_battery_terminal,sc_fast_charge,sc_wireless_charge,sc_color,sc_width,cs_height,cs_thickness,cs_weight) " + 
#         "(SELECT model_name ,model_code ,maker ,lauch ,os ,sell_type ,display_centi ,display_inch ,panel_type ,resolution ,ppi ,refresh_rate ,display_ratio ,display_area ,display_width ,display_height ,hdr_standard ,ap_type ,core_num ,core_clock ,graphic_core ,npu_dsp ,sensor_hub ,com_modem ,system_ram ,in_mem ,storage_device ,out_mem ,5G ,4G ,wifi ,bluetooth ,satelite ,usim_type ,dual_usim ,cam_type ,back_cam ,front_cam ,video ,flash ,picture_resol ,front_disp_resol ,front_video_resol ,apecture ,trem_correction ,trem_prevention ,cam_flash ,hdr_support ,auto_hdr ,optic_zoom ,zio_tag ,lazer_auto_focus ,auto_focus ,out_focus ,touch_focus ,panorama ,tof_sensor ,shoot_night_mode ,earphone_term ,speaker ,high_sound_qual_play ,sound_tech ,fingerprint_recog ,face_recog ,iris_recog ,speech_recog ,ai ,elec_payment ,touch_pen ,waterproof ,etc ,charge_term ,battery_storage ,battery_type ,battery_char ,battery_mount_method ,charge_support ,high_speed_charge ,wireless_charge ,color ,length ,width ,thickness ,weight FROM detail_list WHERE site_name = '세티즌')" )

#         #나무위키
#         namu_sql =( "INSERT INTO g5_phone_spec_namu (sn_model_name ,sn_model_code ,sn_maker ,sn_release_date ,sn_os ,sn_sale_type ,sn_display_cm ,sn_display_in ,sn_display_type ,sn_display_resolution ,sn_display_ppi ,sn_display_hz ,sn_display_aspect_ratio ,sn_display_size ,sn_display_width ,sn_display_height ,sn_display_hdr ,sn_ap_type ,sn_core ,sn_core_clock ,sn_gpu_core ,sn_npu_dsp ,sn_sensor_hub ,sn_modem ,sn_ram ,sn_Builtin_memory ,sn_storage ,sn_external_memory ,sn_5g ,sn_4g ,sn_wifi ,sn_bluetooth ,sn_satellite ,sn_usim_type ,sn_dual_usim ,sn_camera_type ,sn_back_camera ,sn_front_camera ,sn_camera_resolution ,sn_flash ,sn_photo_resolution ,sn_front_resolution ,sn_front_video_resolution ,sn_camera_aperture ,sn_hand_tremor_correction ,sn_hand_tremor_protection ,sn_camera_flash ,sn_hdr_filming ,sn_auto_hdr ,sn_optical_zoom ,sn_geotag ,sn_laser_auto_focus ,sn_auto_focus ,sn_out_focus ,sn_touch_focus ,sn_panorama ,sn_tof ,sn_night_photography ,sn_iphone_terminal ,sn_speaker ,sn_high_sound_quality ,sn_sound_technology ,sn_fingerprint ,sn_face ,sn_iris ,sn_voice ,sn_ai ,sn_payment ,sn_touch_pen ,sn_dustproof ,cs_etc ,cs_charging_terminal ,sn_battery ,sn_battery_type1 ,sn_battery_type2 ,sn_battery_type3 ,sn_battery_terminal ,sn_fast_charge ,sn_wireless_charge ,sn_color ,sn_width ,cs_height ,cs_thickness ,cs_weight ) "
#               "(SELECT model_name ,model_code ,maker ,lauch ,os ,sell_type ,display_inch ,display_centi ,panel_type ,resolution ,ppi ,refresh_rate ,display_ratio ,display_area ,display_width ,display_height ,hdr_standard ,ap_type ,core_num ,core_clock ,graphic_core ,npu_dsp ,sensor_hub ,com_modem ,system_ram ,in_mem ,storage_device ,out_mem ,5G ,4G ,wifi ,bluetooth ,satelite ,usim_type ,dual_usim ,cam_type ,back_cam ,front_cam ,video ,flash ,picture_resol ,front_disp_resol ,front_video_resol ,apecture ,trem_correction ,trem_prevention ,cam_flash ,hdr_support ,auto_hdr ,optic_zoom ,zio_tag ,lazer_auto_focus ,auto_focus ,out_focus ,touch_focus ,panorama ,tof_sensor ,shoot_night_mode ,earphone_term ,speaker ,high_sound_qual_play ,sound_tech ,fingerprint_recog ,face_recog ,iris_recog ,speech_recog ,ai ,elec_payment ,touch_pen ,waterproof ,etc ,charge_term ,battery_storage ,battery_type ,battery_char ,battery_mount_method ,charge_support ,high_speed_charge ,wireless_charge ,color ,length ,width ,thickness ,weight FROM detail_list WHERE site_name = '나무위키')" )

#         #다나와
#         danawa_sql =( "INSERT INTO g5_phone_spec_danawa (sd_model_name ,sd_model_code ,sd_maker ,sd_release_date ,sd_os ,sd_sale_type ,sd_display_cm ,sd_display_in ,sd_display_type ,sd_display_resolution ,sd_display_ppi ,sd_display_hz ,sd_display_aspect_ratio ,sd_display_size ,sd_display_width ,sd_display_height ,sd_display_hdr ,sd_ap_type ,sd_core ,sd_core_clock ,sd_gpu_core ,sd_npu_dsp ,sd_sensor_hub ,sd_modem ,sd_ram ,sd_Builtin_memory ,sd_storage ,sd_external_memory ,sd_5g ,sd_4g ,sd_wifi ,sd_bluetooth ,sd_satellite ,sd_usim_type ,sd_dual_usim ,sd_camera_type ,sd_back_camera ,sd_front_camera ,sd_camera_resolution ,sd_flash ,sd_photo_resolution ,sd_front_resolution ,sd_front_video_resolution ,sd_camera_aperture ,sd_hand_tremor_correction ,sd_hand_tremor_protection ,sd_camera_flash ,sd_hdr_filming ,sd_auto_hdr ,sd_optical_zoom ,sd_geotag ,sd_laser_auto_focus ,sd_auto_focus ,sd_out_focus ,sd_touch_focus ,sd_panorama ,sd_tof ,sd_night_photography ,sd_iphone_terminal ,sd_speaker ,sd_high_sound_quality ,sd_sound_technology ,sd_fingerprint ,sd_face ,sd_iris ,sd_voice ,sd_ai ,sd_payment ,sd_touch_pen ,sd_dustproof ,cs_etc ,cs_charging_terminal ,sd_battery ,sd_battery_type1 ,sd_battery_type2 ,sd_battery_type3 ,sd_battery_terminal ,sd_fast_charge ,sd_wireless_charge ,sd_color ,sd_width ,cs_height ,cs_thickness ,cs_weight )" +
#               "(SELECT model_name ,model_code ,maker ,lauch ,os ,sell_type ,display_inch ,display_centi ,panel_type ,resolution ,ppi ,refresh_rate ,display_ratio ,display_area ,display_width ,display_height ,hdr_standard ,ap_type ,core_num ,core_clock ,graphic_core ,npu_dsp ,sensor_hub ,com_modem ,system_ram ,in_mem ,storage_device ,out_mem ,5G ,4G ,wifi ,bluetooth ,satelite ,usim_type ,dual_usim ,cam_type ,back_cam ,front_cam ,video ,flash ,picture_resol ,front_disp_resol ,front_video_resol ,apecture ,trem_correction ,trem_prevention ,cam_flash ,hdr_support ,auto_hdr ,optic_zoom ,zio_tag ,lazer_auto_focus ,auto_focus ,out_focus ,touch_focus ,panorama ,tof_sensor ,shoot_night_mode ,earphone_term ,speaker ,high_sound_qual_play ,sound_tech ,fingerprint_recog ,face_recog ,iris_recog ,speech_recog ,ai ,elec_payment ,touch_pen ,waterproof ,etc ,charge_term ,battery_storage ,battery_type ,battery_char ,battery_mount_method ,charge_support ,high_speed_charge ,wireless_charge ,color ,length ,width ,thickness ,weight FROM detail_list WHERE site_name = '다나와')" )


#         cursor.execute(cetizen_sql)
#         cursor.execute(namu_sql)
#         cursor.execute(danawa_sql)

#     connection.commit()

# finally:
#     connection.close()


