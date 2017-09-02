import json
import requests

#Create JSON file
def FileCreation():
    r = requests.get('https://confluence/rest/api/content/pageId/child/attachment', auth=('', ''), stream=True)
    data = r.json()
    with open('data.json', 'w') as file:
        json.dump(data, file)

#Get attachment's IDs from JSON file
def getAttachmentsID():
    FileCreation()
    with open('data.json')as data_file:
        data = json.load(data_file)
        attachmentID = [item['id'] for item in data[u'results']]
    file = open('attachmentID.txt', 'w')
    for i in attachmentID:
        file.write(i + '\n')
    file.close()



getAttachmentsID()