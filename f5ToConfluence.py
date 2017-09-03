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
url = 'https://confluence/rest/api/content/'
pageid = 'pageID'

#Create JSON file
def file_creation():
    r = requests.get(url + pageid + '/child/attachment', auth=(user, pwd), stream=True)
    data = r.json()
    with open('data.json', 'w') as file:
        json.dump(data, file)
    print('JSON file has been successfully created')

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
    print('Attachments file has been successfully created')

def remove_attachments():

    file = open('attachmentID.txt', 'r')
    for i in file:
        headers = {'Content-Type': 'application/json'}
        link = url + str(i).strip()
        response = requests.delete(str(link), auth=(user, pwd), headers=headers)
        print(link +" " + str(response.status_code))
    print('Previous attachments have been successfully removed from ' + url + pageid)

def upload_attachments():
    imagedir = 'c:\img\Common'
    list = os.listdir(imagedir)
    for file in list:
        headers = {'X-Atlassian-Token': 'no-check'}
        content_type = 'image/jpeg'
        files = {'file': (file, open(file, 'rb'), 'image/jpeg')}
        print(files)
        r = requests.post(url + pageid + '/child/attachment', headers=headers, files=files, auth=(user, pwd))
    print('New attachments have been successfully uploaded to ' + url + pageid)

file_creation()
get_attachmentsid()
remove_attachments()
upload_attachments()