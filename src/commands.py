commands = [
    {
        "type": 1,
        "name": "hi",
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
import config, aiohttp, asyncio

async def main():
    for c in commands:
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"https://discord.com/api/v8/applications/{config.APPLICATION_ID}/commands",
                headers={"Authorization": f"Bot {config.TOKEN}"},
                json=c,
            ) as response:
                print("Resgistered command", c["name"])

if __name__ == "__main__":
    asyncio.run(main())
