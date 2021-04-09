import re

def crawl_camera_row(temp_dict,td): 
    camera = td[1].text
    data = td[1]
    #temp_dict["카메라"] = camera
    
    if camera.find("[ 전면 카메라 정보") != -1 or camera.find("[ 전면/커버 카메라 정보") != -1:
        
        if td[1].select(".wiki-table-wrap > table"):

            front_cam_table = td[1].select(".wiki-table-wrap > table")
            front_cam_trs = front_cam_table[0].select("tr")

            front_camera = ""
            for num_tr in range(len(front_cam_trs)):
                front_cam_td = front_cam_trs[num_tr].select("td")
                if num_tr == 0:
                    temp_dict["Flash"] = front_cam_td[-1].text
                    
                for td in front_cam_td:
                    if num_tr == 0 and td.text.find("화소") != -1:
                        front_camera = td.text
                    elif td.text.find("화소") != -1:
                        front_camera += (" + ") + (td.text)
            temp_dict["전면카메라"] = front_camera
    
    elif camera.find("전면") != -1:
        
        if td[1].text == "전면 카메라":
            pass
        elif td[1].text == "후면 카메라":
            pass
        else:
            camera = camera.replace("\n","")                       
            temp_dict["전면카메라"] = re.search('전면[0-9 ,만/팝업형]+화소', camera).group()
    

    if data.find("[ 후면 카메라 정보") != -1:
        if data.select(".wiki-table-wrap > table"):

            back_cam_table = data.select(".wiki-table-wrap > table")
            back_cam_trs = back_cam_table[0].select("tr")

            back_camera = ""
            for num_tr in range(len(back_cam_trs)):
                back_cam_td = back_cam_trs[num_tr].select("td")
                if num_tr == 0:
                    temp_dict["Flash"] = back_cam_td[-1].text
                    
                for td in back_cam_td:
                    if num_tr == 0 and td.text.find("화소") != -1:
                        back_camera = td.text
                    elif td.text.find("화소") != -1:
                        back_camera += (" + ") + (td.text)
                        
            temp_dict["후면카메라"] = back_camera
    elif camera.find("후면") != -1:
        temp_dict["후면카메라"] = re.search('후면( OIS 지원 )?[0-9 ,만]+화소', camera).group()

    return temp_dict