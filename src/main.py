import config
from quart import Quart, request
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType, InteractionResponseFlags

CLIENT_PUBLIC_KEY = config.CLIENT_PUBLIC_KEY

app = Quart(__name__)

@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
async def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        return {
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': 'Hello world'
            }
        }
    elif request.json['type'] == InteractionType.MESSAGE_COMPONENT:
        return {
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': 'Hello, you interacted with a component.',
                'flags': InteractionResponseFlags.EPHEMERAL
            }
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)