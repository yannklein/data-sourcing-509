import requests

# url = 'https://api.github.com/users/yannklein'
# response = requests.get(url).json()

# print(response['name'])

isbn = '0451526538'
key = f'ISBN:{isbn}'

# https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data

response = requests.get(
    'https://openlibrary.org/api/books',
    params={'bibkeys': key, 'format':'json', 'jscmd':'data'},
).json()

print(response[key]['title'])
