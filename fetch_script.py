import requests

url = 'https://raw.githubusercontent.com/anudasachintha/Hello-Python01/refs/heads/main/Hello-Python01.py'

response = requests.get(url)

if response.status_code == 200:
    print("File content fetched successfully:")
    print(response.text)
else:
    print("Failed to fetch the file. Status code:", response.status_code)
