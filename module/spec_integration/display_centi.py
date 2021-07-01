#화면센치
#화면인치를 비율로 계산
def find_display_centi(display_in):
    display_cm = ""
    if display_in != "" and display_in is not None:
        display_cm = round(float(display_in)*2.54,2)
    return display_cm