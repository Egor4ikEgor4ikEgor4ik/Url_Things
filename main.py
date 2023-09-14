import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

access_token_bitly = os.getenv("ACCESS_TOKEN_BITLY")
#headers = {
#    'Authorization':f'Bearer {access_token_bitly}',
#}

#response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)

#response.raise_for_status() 
#print (response.json()["emails"][0]["email"])

while True:
    print("1) Сократить ссылку 2) Узнать количество кликов по сокращенной ссылке 3) Выход из программы")
    try:
        user_choice = int(input("Выберите функцию:"))
    except ValueError:
        print("Сэр,не бейте мою грудную клетку арматурой пожалуйста и напишите цифру от 1 до 3 ")
        continue
    
    if user_choice == 1:
        choice = input("Напишите свою ссылку: ")
        headers = {
            'Authorization': f'Bearer {access_token_bitly}',
            'Content-Type': 'application/json',
        }
        params = { "long_url": choice}
        
        try:
            response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Чел напиши ссылку, ботик")
            continue
        user_link = response.json()["link"]
        print(user_link,"-Ваша ссылочка")
    if user_choice == 2:
        headers = {
            'Authorization': f'Bearer {access_token_bitly}',
        }
        user_bit_link = input("ВВЕДИТЕ ВАШУ СОКРАЩЕННУЮ ССЫЛКУ: ")
        if "https" in user_bit_link:
            user_bit_link=user_bit_link.replace("https://","")
        if "http" in user_bit_link:
            user_bit_link=user_bit_link.replace("http://","")
        try:
            response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{user_bit_link}/clicks/summary', headers=headers,)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Упс!Сервера отдыхают, попробуйте еще раз или проверьте верность ссылки <:")
            continue
            
        user_clicks = response.json()["total_clicks"]
        
        print("КЛИКОВ НА ЭТОЙ ССЫЛКЕ",user_clicks)
    if user_choice == 3:
        exit()





















