from .commands import *
import aiohttp, config

#NOTE: This file is for uploading commands to discord, please run this file before running main.py

async def main():
    for c in commands:
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"https://discord.com/api/v8/applications/{config.APPLICATION_ID}/commands",
                headers={"Authorization": f"Bot {config.TOKEN}"},
                json=c,
            ) as response:
                print("Resgistered command", c["name"])
