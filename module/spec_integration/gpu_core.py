def find_gpu_core(namu_row,cetizen_row,danawa_row):
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
    return gpu_core