from commands import commands


def get_command(json_data: dict):
    for command in commands:
        if command.name == json_data["data"]["name"]:
            return command
    return None


class CommandHandler:
    def __init__(self, json_data: dict):
        self.json_data = json_data

    async def execute(self):
        command = get_command(self.json_data)
        if command is None:
            return None
        result = await command.respond(self.json_data)
        return result
