import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

access_token_bitly=os.getenv("ACCESS_TOKEN_BITLY")
#headers = {
#    'Authorization':f'Bearer {access_token_bitly}',
#}

#response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)

#response.raise_for_status() 
#print (response.json()["emails"][0]["email"])


print ("1) Сократить ссылку 2) Узнать количество кликов по сокращенной ссылке")
user_choice=int(input("Выберите функцию:"))
if user_choice==1:
    choice=input("Напишите свою ссылку: ")
    headers = {
    'Authorization': f'Bearer {access_token_bitly}',
    'Content-Type': 'application/json',
    }
    params = { "long_url": choice}
    
    
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=params)
    response.raise_for_status()
    user_link=response.json()["link"]
    print (user_link,"Ваша ссылочка")
else:
    print ("узнать количество кликов")























