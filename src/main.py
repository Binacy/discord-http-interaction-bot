import config
from flask import Flask, jsonify, request
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType, InteractionResponseFlags


CLIENT_PUBLIC_KEY = config.CLIENT_PUBLIC_KEY

app = Flask(__name__)

@app.route('/', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        print(request.json)
        # just a test, i dont know what the response looks like
        if request.json['data']['name'] == "hi":
            return jsonify({
                'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                'data': {
                    'content': f"Hello {request.json['data']['options'][0]['value']}",
                "flags": InteractionResponseFlags.EPHEMERAL
                }
            })
        return jsonify({
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': 'Hello world'
            }
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
