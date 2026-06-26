import os
import json
import requests

BOT_TOKEN = os.getenv("BEARER_TOKEN")
headers = {"Authorization": f"Bearer {BOT_TOKEN}"}

# Get information about a person
response = requests.get("https://webexapis.com/v1/people", headers=headers, params={
    "email": "alphonses@stifel.com"
})

person = response.json()
print(f"data type: {type(person)}")
print(person.get("items")[0].get("addresses")[0])