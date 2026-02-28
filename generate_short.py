import random

topics = [
"Space facts",
"History facts",
"Psychology facts",
"Money facts",
"AI facts"
]

topic = random.choice(topics)

script = f"""
3 Mind Blowing Facts About {topic}

1. The human brain processes information faster than a computer in some tasks.

2. Ancient civilizations built structures we still can't fully explain.

3. AI is changing the world faster than any technology before.
"""

print(script)

with open("short_script.txt","w") as f:
    f.write(script)
