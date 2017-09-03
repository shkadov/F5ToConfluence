#---------------------------------------------------
# Script for automatic upload F5 configuration
# to the Confluence
# by Denis Shkadov
# shkadov@gmail.com
#---------------------------------------------------

import json
import requests
import os
import os.path


user = 'user'
pwd = 'password'
url = 'https://confluence/rest/api/content/60606188/child/attachment'
#Create JSON file
def file_creation():
    r = requests.get(url, auth=(user, pwd), stream=True)
    data = r.json()
    with open('data.json', 'w') as file:
        json.dump(data, file)

#file_creation()

#Get attachment's IDs from JSON file
def get_attachmentsid():
    file_creation()
    with open('data.json')as data_file:
        data = json.load(data_file)
        attachmentid = [item['id'] for item in data[u'results']]
    file = open('attachmentID.txt', 'w')
    for i in attachmentid:
        file.write(i + '\n')
    file.close()

def remove_attachments():
    file = open('attachmentID.txt', 'r')
    for i in file:
        headers = {'Content-Type': 'application/json'}
        # response = requests.delete(url, auth=(user, pwd))
        #user = 'user'
        #pwd = "password"
        url = "https://confluence/rest/api/content/" + str(i)
       # print(url)
        response = requests.get(url, auth=(user, pwd))
        print(str(url) + '=>' + str(response.status_code))

#def upload_new_attachments():

#get_attachmentsid()
def remove_attachments():

    file = open('attachmentID.txt', 'r')
    url = "https://confluence/rest/api/content/"
    for i in file:
        headers = {'Content-Type': 'application/json'}
        link = url + str(i).strip()
        response = requests.delete(str(link), auth=(user, pwd), headers=headers)
        print(link +" " + str(response.status_code))

def upload_attachments():
    imagedir = 'c:\img\Common'
    list = os.listdir(imagedir)
    for file in list:
        url = 'https://confluence/rest/api/content/60606188/child/attachment'
        headers = {'X-Atlassian-Token': 'no-check'}
        content_type = 'image/jpeg'
        #auth = (user, pwd)
        files = {'file': (file, open(file, 'rb'), 'image/jpeg')}
        print(files)
        r = requests.post(url, headers=headers, files=files, auth=auth)


#upload_attachments()




