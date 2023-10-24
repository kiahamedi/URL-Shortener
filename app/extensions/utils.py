import requests
import json

def TestExtensions() -> bool:
    return True

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def english_number_converter(mystr):
    numbers = {
         "۰" : "0" , 
         "۱" : "1" , 
         "۲" : "2" , 
         "۳" : "3" , 
         "۴" : "4" , 
         "۵" : "5" , 
         "۶" : "6" , 
         "۷" : "7" , 
         "۸" : "8" , 
         "۹" : "9" , 
    }

    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr

def sendSMS(number, otp):
    num = f"{english_number_converter(number)}"
    if num[:2] != "98":
        num = f"00{num}"
    url = "https://api.kavenegar.com/v1/KEY/verify/lookup.json"
    params = {
                'receptor': str(num),
                'template': 'kiay',
                'token': otp,
                'type': 'sms',
            }
    req = requests.post(url = url , data = params)
    res = json.loads(req.text)
    return str(res["return"]["status"])