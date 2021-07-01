def clean_garbage(txt):
  garbages = [" ","ppi"]
  for g in garbages:
      txt = txt.replace(g,"")
  return txt

def find_ppi(cetizen_row,danawa_row,namu_row):
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

    return clean_garbage(display_ppi)