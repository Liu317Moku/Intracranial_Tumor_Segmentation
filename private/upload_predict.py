import datetime
import os
import tempfile
import time
import zipfile

import requests

### Use https://icts.top/api/names_generator/?name=test to get your own team and token

TEAM  = 'xenodochial_dewdney'
TOKEN = 'a797bdbc99dcdd9df8d46f4914ff6de746118fa39eb6f106272a77ad'

TEAM = "xenodochial_dewdney"
TOKEN = "a797bdbc99dcdd9df8d46f4914ff6de746118fa39eb6f106272a77ad"
#TEAM = "sandyliu"
#TOKEN = "7855570e6bad56ff33a6347b2a22f7831702c48381f9d075e9886dfd"

STAGE = '2025'

DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'PREDICT')



#zip prediction

temp_name = next(tempfile._get_candidate_names())
print('creating', temp_name)

with zipfile.ZipFile(temp_name, 'w') as zf:
    for root,dir1,files in os.walk(DIR):
        for file in sorted(files):
            if file.lower().endswith('.nii.gz'):
                fullpath = os.path.join(root,file)
                print(fullpath)
                zf.write(fullpath, file)

print(temp_name, 'written')

### submit zip file

API_URL = 'https://icts.top/api/'

url = API_URL+'upload/'
data = {
    'team': TEAM, 
    'token': TOKEN, 
    'stage': STAGE
}
files = {'file': open(temp_name, 'rb')}

response = requests.post(url, data=data, files=files)

print(datetime.datetime.now(), response.content)

# cleamup zip file

# os.remove(temp_name)
# print(temp_name, 'deleted')

try:
    os.remove(temp_name)
    print(temp_name, 'deleted')
except:
    print(temp_name, 'can be deleted after submission')
    

# query submission immediately (metrics are pending)

id = response.json()['id']
url = API_URL+'query/'+id

secs = 1
while True:
    time.sleep(secs)
    response = requests.get(url)
    print(datetime.datetime.now(), response.content)
    if response.json()['status'] != 'P':
        break
    secs = min(60, secs * 2)
