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

from dotenv import load_dotenv
import os
from requests import Request, Session

load_dotenv()
TOKEN = os.environ.get("TOKEN")
APPLICATION_ID = os.environ.get("APPLICATION_ID")

s = Session()
s.headers.update({"Authorization": f"Bot {TOKEN}"})

r = s.send(
    s.prepare_request(
        Request(
            "PUT",
            f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands",
            json=commands,
        )
    )
)

print(f"{r.json()}")
