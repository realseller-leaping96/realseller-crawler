def clean_garbage(txt):
  garbages = [" "]
  for g in garbages:
      txt = txt.replace(g,"")
  return txt

def find_builitin_memory(cetizen_row,danawa_row,namu_row):
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
    return clean_garbage(Builtin_memory)