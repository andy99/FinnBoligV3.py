import requests

def get_html(url):
    response = requests.get(url)
    
    if not response.ok:
        print(f'Code: {response.status_code}, url: {url}')
    return response.text

def main():
    start = 0
    url = "  "

if __name__ == '__main__':
    main()

print(main())