import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))   

my_list = ['apple', 'banana', 'grapes', 'pear']
for frukt, value in enumerate(my_list, 1):
    print(frukt, value)
