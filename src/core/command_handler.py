from utils import (
    InteractionType,
    InteractionResponseType,
    InteractionResponseFlags,
)
from commands import commands


def get_command(json_data: dict):
    for command in commands:
        if command["name"] == json_data["data"]["name"]:
            return command
    return None


class CommandHandler:
    def __init__(self, json_data: dict):
        self.json_data = json_data

    def execute(self):
        if not self.json_data["type"] == InteractionType.APPLICATION_COMMAND:
            return None
        command = get_command(self.json_data)
        if command is None:
            return None
        if command["name"] == "hi":
            user_id = self.json_data["data"]["options"][0]["value"]
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": f"Hello <@!{user_id}>",
                    "flags": InteractionResponseFlags.EPHEMERAL,
                },
            }
