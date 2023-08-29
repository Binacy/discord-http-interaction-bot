commands = [
    {
        "type": 1,
        "name": "hi",
        "description": "Say hi to someone",
        "options": [
            {
                "name": "user",
                "description": "The user to say hi",
                "type": 6,
                "required": True,
            }
        ],
    },
    {
        "type": 1,
        "name": "bye",
        "description": "Say bye to someone",
        "options": [
            {
                "name": "user",
                "description": "The user to say bye",
                "type": 6,
                "required": True,
            }
        ],
    },
]
import config, requests

for c in commands:
    headers = {"Authorization": f"Bot {config.TOKEN}"}

    r = requests.post(f"https://discord.com/api/v10/applications/{config.APPLICATION_ID}/commands", headers=headers, json=c)
    print(r.json())
