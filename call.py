#!/usr/bin/python


import json
import requests

url = 'http://0.0.0.0:80/'
data = {
    'contents':  open('/home/aq446/trash/blah.html').read().encode('base64'),
}
css_data = {
 'contents': open('/home/aq446/trash/GlobalNotes_files/print.css').read().encode('base64')
}
headers = {
    'Content-Type': 'application/json',    # This is important
}
response = requests.post(url, data=json.dumps(data), headers=headers)

# Save the response contents to a file
with open('/home/aq446/trash/file1.pdf', 'wb') as f:
    f.write(response.content)
