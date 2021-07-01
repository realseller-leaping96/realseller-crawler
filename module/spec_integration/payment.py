import re


def find_payment(namu_row,danawa_row,cetizen_row):
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
    return payment