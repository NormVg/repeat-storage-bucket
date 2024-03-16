import requests

url = 'http://localhost:5000/api/upload-notes?title=gg&noqna=15&noflash=30'  # Replace this with your Flask server URL

files = {'file': open('xyz.md', 'rb')}  # Open the file in binary mode

json={
    "flash":[{"data":"54564asda"},{"data":"54564asda"},{"data":"54564asda"}],
    "qna":[{"lola":"54564asda"},{"lola":"54564asda"}]
}

response = requests.post(url , files=files)
print(response.text)  # Print the response from the server


# from tinydb import TinyDB,Query
# import uuid
# import os
# import json





# notes = TinyDB("db/notes.json")
# usr = TinyDB("db/user.json")
# ext = TinyDB("db/notes_extention.json")


# pattern = {
#         "name":"Admin",
#         "userid":"xyz",
#         "year":{"1":100,"2":100,"3":50,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0},
#         "month":{"1":100,"2":100,"3":50,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"24":0,"25":0,"26":0,"27":0,"28":0,"29":0,"30":0},
#         "score":1000,
#         "week":16
#     }

# usr.insert(pattern)