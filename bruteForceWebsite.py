import requests

dictionary = open ('D:\Projects\dictionary-PassList.txt' ,'r')
url = input("please Enter a url: ")
for x in  dictionary:
    r = requests.get(url + "/" + x.rstrip('/n'))
    if  r.status_code == 200 :
        print("the page" + url + '/' + x + " is available")
    else:
        print ("The  page " + url  +  '/' + x + " is Not available")

