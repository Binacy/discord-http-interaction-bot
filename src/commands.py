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

import config, asyncio, aiohttp


async def main():
    for c in commands:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://discord.com/api/v10/applications/{config.APPLICATION_ID}/commands",
                headers={"Authorization": f"Bot {config.TOKEN}"},
                json=c,
            ) as r:
                print(await r.json())


if __name__ == "__main__":
    asyncio.run(main())
