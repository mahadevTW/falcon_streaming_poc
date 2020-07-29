import requests
url = 'http://127.0.0.1:8000/chunked-data'
files = {'file': open('/home/mahadev/Downloads/100MB.bin', 'rb')}
headers = {'content-type': 'application/zip'}
r = requests.post(url, files=files,headers=headers)
print(r.text)


# headersz = {'content-type': 'application/zip'}

# response = requests.get('https://speed.hetzner.de/100MB.bin', stream=True)

# post_response = requests.post(url, files={'file': ('filename', response.iter_content())},headers=headersz)



