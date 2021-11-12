import requests
import json

d1={
    'username':'admin',
    'email':'abcd@gmail.com',
    'password':'password123'
}
json_data=json.dumps(d1)
res=requests.post("http://127.0.0.1:8000/api/register/",data=json_data)
print(res.json())
print(res.status_code)