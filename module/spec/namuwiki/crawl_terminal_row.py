import re

def crawl_terminal_row(temp_dict, td):
    terminal = td[1].text
    charge = ""
    if terminal.find("x 1") != -1:
        temp_dict["충전단자"] = re.search('(.*x 1)', terminal).group()
        charge =  re.search('(.*x 1)', terminal).group()
        
    elif terminal.find("단자") != -1:
        temp_dict["충전단자"] = re.search('(.*단자)', terminal).group()
        charge = re.search('(.*단자)', terminal).group()

    if terminal.replace(charge,"") != "":
        temp_dict["듀얼유심"] = terminal.replace(charge,"")
        
    return temp_dict