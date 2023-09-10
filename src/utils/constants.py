from enum import Enum


class InteractionType:
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class InteractionResponseType:
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9


class InteractionResponseFlags:
    EPHEMERAL = 1 << 6


class ApplicationCommandOptionType(Enum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8


class Option:
    def __init__(
        self,
        name: str,
        type: ApplicationCommandOptionType,
        description: str = "...",
        required: bool = False,
    ):
        self.name = name
        self.description = description
        self.type = type
        self.required = required

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "type": self.type.value,
            "required": self.required,
        }


class SlashCommand:
    def __init__(self, name: str, description: str = "...", options: list = None):
        self.name = name
        self.description = description
        self.options = options or []

    async def respond(self, json_data: dict):
        # This function is aync just so that fastapi supports async poggies
        ...

    def to_dict(self):
        return {
            "type": 1,  # Slash command
            "name": self.name,
            "description": self.description,
            "options": [option.to_dict() for option in self.options],
        }
