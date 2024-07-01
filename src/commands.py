import os

import aiohttp
import dotenv

from utils import (ApplicationCommandOptionType, InteractionResponseFlags,
                   InteractionResponseType, Option, SlashCommand)

dotenv.load_dotenv()


class HelloCommand(SlashCommand):
    def __init__(self):
        super().__init__(
            name="hello",
            description="Say hello to someone",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user to say hello",
                    required=True,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        # This function is async just so that fastapi supports async poggies
        user_id = json_data["data"]["options"][0]["value"]
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": f"Hello <@!{user_id}>",
                "flags": InteractionResponseFlags.EPHEMERAL,
            },
        }


class ByeCommand(SlashCommand):
    def __init__(self):
        super().__init__(
            name="bye",
            description="Say bye to someone",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user to say bye",
                    required=True,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        # This function is async just so that fastapi supports async poggies
        user_id = json_data["data"]["options"][0]["value"]
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": f"Bye <@!{user_id}>",
                "flags": InteractionResponseFlags.EPHEMERAL,
            },
        }


token = os.getenv("TOKEN")
base_url = "https://discord.com/api/v19"
cdn_url = "https://cdn.discordapp.com"

async def get_user(user_id: str):
    async with aiohttp.ClientSession(
        headers= {
            "Authorization": f"Bot {token}"
        }
    ) as session:
        async with session.get(
            f"{base_url}/users/{user_id}"
        ) as response:
            return await response.json()
              
class AvatarCommand(SlashCommand):
    def __init__(self):
        super().__init__(
            name="avatar",
            description="Displays someone's avatar",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user whose avatar you want to see",
                    required=False,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        user_id = json_data["data"]["options"][0]["value"] if json_data.get("data") and json_data["data"].get("options") else None

        if user_id is not None:
            user_data = await get_user(user_id=user_id)
            avatar_url = f"{cdn_url}/avatars/{user_id}/{user_data['avatar']}.png?size=1024"
            user_name = user_data["username"]
            return {
                    "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                    "data": {
                        "embeds": [
                            {
                                "author": {
                                    "name": user_name,
                                    "icon_url": avatar_url
                                },
                                "image": {
                                    "url": avatar_url
                                },
                                "color": 0x2b2d31
                            }
                        ]
                    },
                }

        else:
            avatar_url = f"{cdn_url}/avatars/{json_data['member']['user']['id']}/{json_data['member']['user']['avatar']}.png?size=1024"
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "embeds": [
                        {
                            "author": {
                                "name": json_data["member"]["user"]["username"],
                                "icon_url": avatar_url
                            },
                            "image": {
                                "url": avatar_url
                            },
                            "color": 0x2b2d31
                        }
                    ],
                },
            }


commands = [HelloCommand(), ByeCommand(), AvatarCommand()]
# NOTE: Please updates this `commands` list with your commands