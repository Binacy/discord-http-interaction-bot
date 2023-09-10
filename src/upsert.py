from dotenv import load_dotenv
import os
from requests import Request, Session
from commands import commands

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
            json=[c.to_dict() for c in commands],
        )
    )
)

print(f"{r.json()}")
