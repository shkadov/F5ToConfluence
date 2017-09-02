import json
import requests
import jira


user = 'user'
pwd =  "password"
#Create JSON file
def file_creation():
    r = requests.get('https://confluence/rest/api/content/60606188/child/attachment', auth=(user, pwd), stream=True)
    data = r.json()
    with open('data.json', 'w') as file:
        json.dump(data, file)

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
        user = 'user'
        pwd = "password"
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
