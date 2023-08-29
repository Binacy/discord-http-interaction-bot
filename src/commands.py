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

import config
from requests import Request, Session

s = Session()
s.headers.update({"Authorization": f"Bot {config.TOKEN}"})
r = s.send(
    s.prepare_request(
        Request(
            "PUT",
            f"https://discord.com/api/v10/applications/{config.APPLICATION_ID}/commands",
            json=commands,
        )
    )
)
print(f"{r.json()}")
