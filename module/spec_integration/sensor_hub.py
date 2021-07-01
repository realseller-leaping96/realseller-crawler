def clean_garbage(txt):
  garbages = ["미탑재","(파트넘버 불명) 내장"]
  for g in garbages:
      txt = txt.replace(g,"")
  return txt

def find_sensor_hub(namu_row,cetizen_row,danawa_row):
    #sensor_hub
    sensor_hub = ""
    if len(namu_row) == 1 :
        if namu_row.iloc[0]['sn_sensor_hub'] is not None:
            sensor_hub = namu_row.iloc[0]['sn_sensor_hub']

    return clean_garbage(sensor_hub)