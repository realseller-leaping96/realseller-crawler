def clean_garbage(txt):
  garbages = ["미탑재","(파트넘버 불명) 내장"]
  for g in garbages:
      txt = txt.replace(g,"")
  return txt

def find_modem(namu_row,cetizen_row,danawa_row):
    #modem
    modem = ""
    if len(namu_row) == 1 :
        if namu_row.iloc[0]['sn_modem'] is not None:
            modem = namu_row.iloc[0]['sn_modem']
    return clean_garbage(modem)