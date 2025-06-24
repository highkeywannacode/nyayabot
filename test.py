import requests

url = "http://127.0.0.1:5000/ask"
data = {
    "question": "Does the wife have anyright on the property ownership if the husband has died?"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
