import random
import os
import requests

API_KEY = os.getenv("YOUTUBE_API_KEY")

topics = [
    "space facts",
    "history facts",
    "psychology facts",
    "technology facts",
    "money facts"
]

topic = random.choice(topics)

url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={topic}&maxResults=5&type=video&key={API_KEY}"

response = requests.get(url).json()

titles = []

for item in response["items"]:
    titles.append(item["snippet"]["title"])

script = f"""
3 Viral Shorts Ideas About {topic}

1. {random.choice(titles)}
2. {random.choice(titles)}
3. {random.choice(titles)}

Subscribe for more!
"""

with open("short_script.txt", "w") as f:
    f.write(script)

print(script)

