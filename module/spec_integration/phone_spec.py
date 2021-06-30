# 통신규격
communication_standard = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_5g'] is not None:
        communication_standard = '5G'
    elif cetizen_row.iloc[0]['sc_4g'] is not None:
        communication_standard = '4G'
if len(danawa_row) == 1 and communication_standard == "":
    if danawa_row.iloc[0]['sd_5g'] is not None:
        communication_standard = '5G'
    elif danawa_row.iloc[0]['sd_4g'] is not None:
        communication_standard = '4G'
if len(namu_row) == 1 and communication_standard == "":
    if namu_row.iloc[0]['sn_5g'] is not None:
        communication_standard = '5G'
    elif namu_row.iloc[0]['sn_4g'] is not None:
        communication_standard = '4G'

#운영체제
os = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_os'] is not None:
        os = re.sub(('삼성.*|옵티머스.*'),"",cetizen_row.iloc[0]['sc_os'])
        os_split = os.split("|")
        os_split = re.search('[0-9.]+',os_split[-1]).group()
        if os.find("iOS") != -1:
            os = 'iOS ' +  os_split
        elif os.find("안드로이드") != -1:
            os = 'Android ' +  os_split
if len(danawa_row) == 1 and os == "":
    if danawa_row.iloc[0]['sd_os'] is not None:
        os = danawa_row.iloc[0]['sd_os']
        os_split = os.split("|")
        os_split = re.search('[0-9.]+',os_split[-1]).group()
        if os.find("iOS") != -1:
            os = 'iOS ' +  os_split
        elif os.find("안드로이드") != -1:
            os = 'Android ' +  os_split
if len(namu_row) == 1 and os == "":
    if namu_row.iloc[0]['sn_os'] is not None:
        os = re.sub(('삼성.*|옵티머스.*|Samsung.*|LG.*'),"",namu_row.iloc[0]['sn_os'])
        os_split = os.split("|")
        os_split = re.search('[0-9.]+',os_split[-1]).group()
        if os.find("iOS") != -1:
            os = 'iOS ' +  os_split
        elif os.find("안드로이드") != -1:
            os = 'Android ' +  os_split
            
#화면인치
display_in = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_display_in'] is not None:
        display_in = cetizen_row.iloc[0]['sc_display_in']

if len(danawa_row) == 1 and display_in == "":
    if danawa_row.iloc[0]['sd_display_in'] is not None:
        display_in = danawa_row.iloc[0]['sd_display_in']

if len(namu_row) == 1 and display_in == "":
    if namu_row.iloc[0]['sn_display_in'] is not None:
        display_in = namu_row.iloc[0]['sn_display_in']
        
#화면센치
display_cm = ""
if display_in != "" and display_in is not None:
    display_cm = round(float(display_in)*2.54,2)
        
    
#화면해상도
display_resolution = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_display_resolution'] is not None:
        display_resolution = cetizen_row.iloc[0]['sc_display_resolution']
        resolution_list = display_resolution.split("x")
        width = resolution_list[0]
        height = resolution_list[1]
        display_resolution = height+"x"+width
        
if len(danawa_row) == 1 and display_resolution == "":
    if danawa_row.iloc[0]['sd_display_resolution'] is not None:
        display_resolution = danawa_row.iloc[0]['sd_display_resolution'].replace(" ","")

if len(namu_row) == 1 and display_resolution == "":
    if namu_row.iloc[0]['sn_display_resolution'] is not None:
        display_resolution = namu_row.iloc[0]['sn_display_resolution'].replace(" ","")
display_resolution = display_resolution.strip().replace("480x800","800x480")
# "x"를 기준으로 split해서 둘중에 큰값/작은값 비교해서 재구성 

#패널종류
display_type = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_display_type'] is not None:
        display_type = cetizen_row.iloc[0]['sc_display_type']
        
if len(danawa_row) == 1 and display_type == "":
    if danawa_row.iloc[0]['sd_display_type'] is not None:
        display_type = danawa_row.iloc[0]['sd_display_type']

if len(namu_row) == 1 and display_type == "":
    if namu_row.iloc[0]['sn_display_type'] is not None:
        display_type = namu_row.iloc[0]['sn_display_type']
display_type = display_type.replace("super ","S-").replace("Super ","S-").replace(
    "Dynamic ","D-").replace("pOLED","P-OLED").replace("Plastic 소재의 ","P-").strip()

#ppi
display_ppi = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_display_ppi'] is not None:
        display_ppi = cetizen_row.iloc[0]['sc_display_ppi']
        
if len(danawa_row) == 1 and display_ppi == "":
    if danawa_row.iloc[0]['sd_display_ppi'] is not None:
        display_ppi = danawa_row.iloc[0]['sd_display_ppi']

if len(namu_row) == 1 and display_ppi == "":
    if namu_row.iloc[0]['sn_display_ppi'] is not None:
        display_ppi = namu_row.iloc[0]['sn_display_ppi']
        
#화면비
display_aspect_ratio = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_display_aspect_ratio'] is not None:
        display_aspect_ratio = cetizen_row.iloc[0]['sc_display_aspect_ratio']
        
if len(danawa_row) == 1 and display_aspect_ratio == "":
    if danawa_row.iloc[0]['sd_display_aspect_ratio'] is not None:
        display_aspect_ratio = danawa_row.iloc[0]['sd_display_aspect_ratio']

if len(namu_row) == 1 and display_aspect_ratio == "":
    if namu_row.iloc[0]['sn_display_aspect_ratio'] is not None:
        display_aspect_ratio = namu_row.iloc[0]['sn_display_aspect_ratio']

#비율 계산하는식/공식 반영?
#함수화 => 정수x정수가 들어가면 비율값이 나오도록 하는
if  display_resolution == "1792x828": 
    display_aspect_ratio = "19.5:9"
elif  display_resolution == "2436x1125": 
    display_aspect_ratio = "19.5:9"
elif  display_resolution == "2688x1242": 
    display_aspect_ratio = "19.5:9"
elif  display_resolution == "1920x1080": 
    display_aspect_ratio = "16:9"
elif display_resolution == "800x480": 
    display_aspect_ratio = "16:9"
elif  display_resolution == "1280x720": 
    display_aspect_ratio = "16:9"
elif  display_resolution == "2560x1440": 
    display_aspect_ratio = "16:9"
elif  display_resolution == "1136x640":
    display_aspect_ratio = "16:9"
    
#AP 종류
ap_type = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_ap_type'] is not None:
        ap_type = cetizen_row.iloc[0]['sc_ap_type']
        
if len(danawa_row) == 1 and ap_type == "":
    if danawa_row.iloc[0]['sd_ap_type'] is not None:
        ap_type = danawa_row.iloc[0]['sd_ap_type']

if len(namu_row) == 1 and ap_type == "":
    if namu_row.iloc[0]['sn_ap_type'] is not None:
        ap_type = namu_row.iloc[0]['sn_ap_type']
        
ap_type = ap_type.replace("퀄컴","Qualcomm").replace("삼성","Samsung"
        ).replace("엑시노스","Exynos ").replace("(","").replace(")",""
        ).replace("SoC","").replace("애플","Apple").replace("스냅드래곤","Snapdragon"
        ).replace("[1]","").replace("미디어텍","MediaTek").strip()

#코어수
core = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_core'] is not None:
        core = cetizen_row.iloc[0]['sc_core'].replace("1개","싱글코어"
                ).replace("2개","듀얼코어").replace("4개","쿼드코어"
                ).replace("6개","헥사코어").replace("8개","옥타코어"
                ).replace(" 비트","비트")
        
if len(danawa_row) == 1 and core == "":
    if danawa_row.iloc[0]['sd_core'] is not None:
        core = danawa_row.iloc[0]['sd_core'].replace("(1)","").replace("(2)",""
                ).replace("(4)","").replace("(8)","")

if len(namu_row) == 1 and core == "":
    if namu_row.iloc[0]['sn_core'] is not None:
        core = namu_row.iloc[0]['sn_core']
        
#코어클럭
core_clock = ""

if len(namu_row) == 1 and core_clock == "":
    if namu_row.iloc[0]['sn_core_clock'] is not None:
        if re.search('[0-9.]+ GHz',namu_row.iloc[0]['sn_core_clock']) is not None:
            core_clock_iter = re.finditer('[0-9.]+ GHz',namu_row.iloc[0]['sn_core_clock'])
            for matchObj in core_clock_iter:
                if core_clock == "":
                    core_clock = matchObj.group()
                else:
                    core_clock += "+" + matchObj.group()   
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_core_clock'] is not None:
        core_clock = str(int(cetizen_row.iloc[0]['sc_core_clock'].replace("MHz",""))/1000)+("GHz")
        
if len(danawa_row) == 1 and core_clock == "":
    if danawa_row.iloc[0]['sd_core_clock'] is not None:
        core_clock = danawa_row.iloc[0]['sd_core_clock']
core_clock = core_clock.replace(" " ,"")

#그래픽코어
gpu_core = ""

if len(namu_row) == 1 :
    if namu_row.iloc[0]['sn_gpu_core'] is not None:
        gpu_core = namu_row.iloc[0]['sn_gpu_core'].replace("GPU",""
        ).replace("퀄컴","Qualcomm").replace("-.- GHz",""
        ).replace("-.- MHz","").replace(" MHz","MHz"
        ).replace(" GHz","GHz")

if len(cetizen_row) == 1 and gpu_core == "":
    if cetizen_row.iloc[0]['sc_gpu_core'] is not None:
        gpu_core = cetizen_row.iloc[0]['sc_gpu_core']
        
if len(danawa_row) == 1 and gpu_core == "":
    if danawa_row.iloc[0]['sd_gpu_core'] is not None:
        gpu_core = danawa_row.iloc[0]['sd_gpu_core']
        
#sensor_hub
sensor_hub = ""
if len(namu_row) == 1 :
    if namu_row.iloc[0]['sn_sensor_hub'] is not None:
        sensor_hub = namu_row.iloc[0]['sn_sensor_hub']
        
#modem
modem = ""
if len(namu_row) == 1 :
    if namu_row.iloc[0]['sn_modem'] is not None:
        modem = namu_row.iloc[0]['sn_modem']
        
#ram
ram = ""
if len(namu_row) == 1 :
    if namu_row.iloc[0]['sn_ram'] is not None:
        ram = namu_row.iloc[0]['sn_ram'].replace(" / ","|")
if len(cetizen_row) == 1 and ram == "":
    if cetizen_row.iloc[0]['sc_ram'] is not None:
        ram = cetizen_row.iloc[0]['sc_ram'].replace(" | ","|")
        
if len(danawa_row) == 1 and ram == "":
    if danawa_row.iloc[0]['sd_ram'] is not None:
        ram = danawa_row.iloc[0]['sd_ram']
ram = ram.replace(" GB","GB").replace(" MB","MB")

#Builtin_memory
Builtin_memory = ""

if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_Builtin_memory'] is not None:
        Builtin_memory = cetizen_row.iloc[0]['sc_Builtin_memory'].replace("/","|")
if len(danawa_row) == 1 and Builtin_memory == "":
    if danawa_row.iloc[0]['sd_Builtin_memory'] is not None:
        Builtin_memory = danawa_row.iloc[0]['sd_Builtin_memory']
if len(namu_row) == 1 and Builtin_memory == "":
    if namu_row.iloc[0]['sn_Builtin_memory'] is not None:
        Builtin_memory = namu_row.iloc[0]['sn_Builtin_memory']
        if Builtin_memory.find("/")!= -1:
            Builtin_memory = Builtin_memory.replace("/","GB|")
        
        if Builtin_memory.find("MB") == -1:
            Builtin_memory += "GB"
            
#external_memory
external_memory = ""

if len(namu_row) == 1 :
    if namu_row.iloc[0]['sn_external_memory'] is not None:
        external_memory = namu_row.iloc[0]['sn_external_memory']
if len(danawa_row) == 1 and external_memory == "":
    if danawa_row.iloc[0]['sd_external_memory'] is not None:
        external_memory = danawa_row.iloc[0]['sd_external_memory'].replace("미지원",""
                            ).replace("Micro","micro").replace("micro"," micro "
                            ).replace(":","").replace("최대","최대 ").replace("GB"," GB"
                            ).replace("TB"," TB").replace("MB"," MB")
    if external_memory.find("최대")!=-1:
        external_memory += " 지원"
if len(cetizen_row) == 1 and external_memory == "":
    if cetizen_row.iloc[0]['sc_external_memory'] is not None:
        external_memory = cetizen_row.iloc[0]['sc_external_memory'].replace("Micro","micro"
                        ).replace("micro"," micro ")
external_memory = external_memory.strip()

#front_camera
front_camera = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_front_camera'] is not None:
        if danawa_row.iloc[0]['sd_front_camera'].find("~")==-1:
            front_camera = danawa_row.iloc[0]['sd_front_camera'].replace(",","")
if len(namu_row) == 1 and front_camera == "":
    if namu_row.iloc[0]['sn_front_camera'] is not None:
        front_camera = namu_row.iloc[0]['sn_front_camera'].replace(" ","")
        
#back_camera
back_camera = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_back_camera'] is not None:
        if danawa_row.iloc[0]['sd_back_camera'].find("~")==-1:
            back_camera = danawa_row.iloc[0]['sd_back_camera'].replace(",","")
if len(namu_row) == 1 and front_camera == "":
    if namu_row.iloc[0]['sn_back_camera'] is not None:
        back_camera = namu_row.iloc[0]['sn_back_camera'].replace(" ","")
        
#front_video_resolution
front_video_resolution = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_front_video_resolution'] is not None:
        front_video_resolution = cetizen_row.iloc[0]['sc_front_video_resolution'].replace(")",") "
            ).replace("(Full HD)","").replace("(UHD)","").replace("(HD)",""
            ).replace("(WVGA)","").replace("(NTSC)","").replace("(VGA)","").replace("(QVGA)",""
            ).replace("(WQVGA)","")
    front_video_resolution = front_video_resolution.strip()
    if front_video_resolution == "FPS":
        front_video_resolution = ""
#UHD, FHD 다 지우고 다시 해상도기준으로 추가시키도록 로직작성

#flash
flash = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_flash'] is not None:
        flash = cetizen_row.iloc[0]['sc_flash']
if len(namu_row) == 1 and flash == "":
    if namu_row.iloc[0]['sn_flash'] is not None:
        flash = namu_row.iloc[0]['sn_flash'].replace("듀얼-","Dual "
                ).replace("듀얼","Dual").replace("쿼드-","Quad "
                ).replace("광학 2배줌 지원",""
                ).replace("광학 2배줌 지원","").replace("광학 1.85배줌 지원",""
                ).replace("LASER AF 및","").replace("플래시","")
        
        
#photo_resolution
photo_resolution = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_photo_resolution'] is not None:
        photo_resolution = cetizen_row.iloc[0]['sc_photo_resolution']
        
#camera_aperture
camera_aperture = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_camera_aperture'] is not None:
        camera_aperture = cetizen_row.iloc[0]['sc_camera_aperture'].replace("/","")
        
if len(danawa_row) == 1 and camera_aperture == "":
    if danawa_row.iloc[0]['sd_camera_aperture'] is not None:
        camera_aperture = danawa_row.iloc[0]['sd_camera_aperture']
camera_aperture = camera_aperture.replace(" ","")

#fingerprint
fingerprint = ""
if len(namu_row) == 1:
    if namu_row.iloc[0]['sn_fingerprint'] is not None:
        fingerprint = namu_row.iloc[0]['sn_fingerprint']
        
if len(danawa_row) == 1 and fingerprint == "":
    if danawa_row.iloc[0]['sd_fingerprint'] is not None:
        fingerprint = danawa_row.iloc[0]['sd_fingerprint']

if len(cetizen_row) == 1 and fingerprint == "":
    if cetizen_row.iloc[0]['sc_fingerprint'] is not None:
        fingerprint = cetizen_row.iloc[0]['sc_fingerprint']
        
#face
face = ""
if len(namu_row) == 1:
    if namu_row.iloc[0]['sn_face'] is not None:
        face = namu_row.iloc[0]['sn_face']
        
if len(danawa_row) == 1 and face == "":
    if danawa_row.iloc[0]['sd_face'] is not None:
        face = danawa_row.iloc[0]['sd_face']

if len(cetizen_row) == 1 and face == "":
    if cetizen_row.iloc[0]['sc_face'] is not None:
        face = cetizen_row.iloc[0]['sc_face']
        
#charging_terminal
charging_terminal = ""
if len(namu_row) == 1:
    if namu_row.iloc[0]['sn_charging_terminal'] is not None:
        charging_terminal = namu_row.iloc[0]['sn_charging_terminal']
        charging_terminal = re.sub("( x [0-9])","",charging_terminal.split(",")[0]).strip()
        
if len(danawa_row) == 1 and charging_terminal == "":
    if danawa_row.iloc[0]['sd_charging_terminal'] is not None:
        charging_terminal = danawa_row.iloc[0]['sd_charging_terminal']
        if charging_terminal.find("8핀"):
            charging_terminal = "USB 2.0 Apple Lightning 8-pin"
        elif charging_terminal.find("5핀"):
            charging_terminal = "USB 2.0 micro Type-B"
        elif charging_terminal.find("타입C"):
            charging_terminal = "USB 3.1 Type-C"
            
#bluetooth
bluetooth = ""

if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_bluetooth'] is not None:
        bluetooth = cetizen_row.iloc[0]['sc_bluetooth']
if len(danawa_row) == 1 and bluetooth == "":
    if danawa_row.iloc[0]['sd_bluetooth'] is not None:
        bluetooth = danawa_row.iloc[0]['sd_bluetooth'].replace("v","").replace(".0","")
if len(namu_row) == 1 and bluetooth == "":
    if namu_row.iloc[0]['sn_bluetooth'] is not None:
        bluetooth = namu_row.iloc[0]['sn_bluetooth']
        
#usim_type
usim_type = ""
if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_usim_type'] is not None:
        usim_type = cetizen_row.iloc[0]['sc_usim_type']
if len(danawa_row) == 1 and usim_type == "":
    if danawa_row.iloc[0]['sd_usim_type'] is not None:
        usim_type = danawa_row.iloc[0]['sd_usim_type']
        
#battery
battery = ""
if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_battery'] is not None:
        battery = cetizen_row.iloc[0]['sc_battery']
if len(danawa_row) == 1 and battery == "":
    if danawa_row.iloc[0]['sd_battery'] is not None:
        if danawa_row.iloc[0]['sd_battery'].find("~") == -1:
            battery = danawa_row.iloc[0]['sd_battery']
            
if len(namu_row) == 1 and battery == "":
    if namu_row.iloc[0]['sn_battery'] is not None:
        battery = namu_row.iloc[0]['sn_battery']
        
#battery_type1, 배터리타입(종류)
battery_type1 = ""
if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_battery_type1'] is not None:
        battery_type1 = cetizen_row.iloc[0]['sc_battery_type1']

if len(namu_row) == 1 and battery_type1 == "":
    if namu_row.iloc[0]['sn_battery_type1'] is not None:
        battery_type1 = namu_row.iloc[0]['sn_battery_type1'].replace("내장형","").replace("착탈식","").strip()
        
#battery_type2 배터리특징 (충전기술 및 와트)
battery_type2 = ""
if len(namu_row) == 1:
    if namu_row.iloc[0]['sn_battery_type2'] is not None:
        battery_type2 = namu_row.iloc[0]['sn_battery_type2'].replace(",","").replace(" W)","W) "
        ).replace("삼성전자의","Samsung").replace("삼성전자","Samsung"
        ).replace("퀄컴 퀵 차지","Qualcomm Quick Charge"
        ).replace("미디어텍","MediaTek").replace("(- W)","").strip()

#battery_type3, 배터리장착방식
battery_type3 = ""
if len(cetizen_row) == 1 :
    if cetizen_row.iloc[0]['sc_battery_type3'] is not None:
        battery_type3 = cetizen_row.iloc[0]['sc_battery_type3'].replace("급속충전 ","")
if len(danawa_row) == 1 and battery_type3 == "":
    if danawa_row.iloc[0]['sd_battery_type3'] is not None:
        battery_type3 = danawa_row.iloc[0]['sd_battery_type3'].replace("배터리","").replace("탈착","분리")
        
#wireless_charge
wireless_charge = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_wireless_charge'] is not None:
        wireless_charge = danawa_row.iloc[0]['sd_wireless_charge'].replace(":","")
if len(cetizen_row) == 1 and wireless_charge == "":
    if cetizen_row.iloc[0]['sc_wireless_charge'] is not None:
        wireless_charge = "무선충전"

        
#thickness
thickness = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_thickness'] is not None:
        if danawa_row.iloc[0]['sd_thickness'].find("~") == -1:
            thickness = danawa_row.iloc[0]['sd_thickness']
if len(cetizen_row) == 1 and thickness == "":
    if cetizen_row.iloc[0]['sc_thickness'] is not None:
        thickness = cetizen_row.iloc[0]['sc_thickness']
if len(namu_row) == 1 and thickness == "":
    if namu_row.iloc[0]['sn_thickness'] is not None:
        thickness = namu_row.iloc[0]['sn_thickness']
        
#width
width = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_width'] is not None:
        if danawa_row.iloc[0]['sd_width'].find("~") == -1:
            width = danawa_row.iloc[0]['sd_width']
if len(cetizen_row) == 1 and width == "":
    if cetizen_row.iloc[0]['sc_width'] is not None:
        width = cetizen_row.iloc[0]['sc_width']
if len(namu_row) == 1 and width == "":
    if namu_row.iloc[0]['sn_width'] is not None:
        width = namu_row.iloc[0]['sn_width']
        
#height
height = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_height'] is not None:
        if danawa_row.iloc[0]['sd_height'].find("~") == -1:
            height = danawa_row.iloc[0]['sd_height']
if len(cetizen_row) == 1 and height == "":
    if cetizen_row.iloc[0]['sc_height'] is not None:
        height = cetizen_row.iloc[0]['sc_height']
if len(namu_row) == 1 and height == "":
    if namu_row.iloc[0]['sn_height'] is not None:
        height = namu_row.iloc[0]['sn_height']
        
#weight
weight = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_weight'] is not None:
        if danawa_row.iloc[0]['sd_weight'].find("~") == -1:
            weight = danawa_row.iloc[0]['sd_weight']
if len(cetizen_row) == 1 and weight == "":
    if cetizen_row.iloc[0]['sc_weight'] is not None:
        weight = cetizen_row.iloc[0]['sc_weight']
if len(namu_row) == 1 and weight == "":
    if namu_row.iloc[0]['sn_weight'] is not None:
        weight = namu_row.iloc[0]['sn_weight']
weight = weight.replace("\r","")

#release_date
release_date = ""
if len(cetizen_row) == 1:
    if cetizen_row.iloc[0]['sc_release_date'] is not None:
        release_date = cetizen_row.iloc[0]['sc_release_date']
        
#color
color = ""
if len(namu_row) == 1:
    if namu_row.iloc[0]['sn_color'] is not None:
        color = namu_row.iloc[0]['sn_color']
        color = re.sub("\[[0-9]+\](GB)","",color).replace("&",","
                ).replace(",","|")
        
#payment
payment = ""
if len(danawa_row) == 1 :
    if danawa_row.iloc[0]['sd_payment'] is not None:
        payment = danawa_row.iloc[0]['sd_payment']
        payment = payment.replace("애플페이(국내미지원)","Apple Pay(국내미지원)"
                ).replace("삼성페이","SAMSUNG Pay"
                ).replace("LG페이","LG Pay")
if len(cetizen_row) == 1 and payment == "":
    if cetizen_row.iloc[0]['sc_payment'] is not None:
        payment = cetizen_row.iloc[0]['sc_payment']
        payment = payment.replace("apple pay","Apple Pay"
                ).replace("Apple Pay","Apple Pay(국내미지원)")