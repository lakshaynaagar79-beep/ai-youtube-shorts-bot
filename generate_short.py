import random
import os
topics = [
"Space",
"Ancient History",
"Psychology",
"Money",
"Technology",
"Mysteries",
"Human Body"
]

facts = [
"Octopuses have three hearts.",
"The pyramids are over 4500 years old.",
"Your brain uses about 20 percent of your body's energy.",
"Some millionaires wake up at 5 AM daily.",
"AI can already create music and movies.",
"The ocean is mostly unexplored.",
"You blink around 20000 times a day."
]

topic = random.choice(topics)

script = f"""
3 Crazy Facts About {topic}

1. {random.choice(facts)}
2. {random.choice(facts)}
3. {random.choice(facts)}

Subscribe for more!
"""

print(script)

with open("short_script.txt","w") as f:
    f.write(script)
creds = os.getenv("YOUTUBE_CREDENTIALS")

if creds:
    print("YouTube credentials connected")
else:
    print("Missing credentials")
