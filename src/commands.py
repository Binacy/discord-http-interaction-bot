from utils import (
    SlashCommand,
    Option,
    InteractionResponseFlags,
    InteractionResponseType,
    ApplicationCommandOptionType,
)


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
        # This function is aync just so that fastapi supports async poggies
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
        # This function is aync just so that fastapi supports async poggies
        user_id = json_data["data"]["options"][0]["value"]
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": f"Bye <@!{user_id}>",
                "flags": InteractionResponseFlags.EPHEMERAL,
            },
        }


commands = [HelloCommand(), ByeCommand()]
# NOTE: Please updates this `commands` list with your commands
