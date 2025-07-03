import requests 
from requests.exceptions import * 
from gtoken import get_token # create a separate module for importing your token 

token = get_token() 

user = 'yourusername' 

auth_header = (user, token) 

base_url = "https://api.github.com" 

header = { 

    'Authorization': 'token' + token 

} 

res = requests.get(f'{base_url}/user', headers=header) 

print(res.json()) 

s = requests.Session() 

for i in range (1,5): 
    s.get(f'{base_url}users/yourusername/repos', headers=header) 