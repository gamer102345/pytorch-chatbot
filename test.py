import requests
re = requests.get('https://web.whatsapp.com')
print(re.content)