def clean_garbage(txt):
  garbages = [" /"]
  for g in garbages:
      txt = txt.replace(g,"")
  return txt

def find_ram(namu_row,cetizen_row,danawa_row):
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
    
    return clean_garbage(ram)