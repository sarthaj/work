url = "https://blah/blah/blah"
headers = {
    "Accept": "application/json",
    "Authentication": "Bearer 37d5a9ac5442ba9f594a8ca1421a27b"
}
response = requests.get(url, headers=headers)
print(response.text)