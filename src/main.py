import config
from fastapi import FastAPI, Request
from constants import InteractionType, InteractionResponseType, InteractionResponseFlags, verify_key_decorator

app = FastAPI()

CLIENT_PUBLIC_KEY = config.CLIENT_PUBLIC_KEY

@app.post("/")
@verify_key_decorator(CLIENT_PUBLIC_KEY)
async def interactions(request: Request):
    json_data = await request.json()

    if json_data["type"] == InteractionType.APPLICATION_COMMAND:
        if json_data["data"]["name"] == "hi":
            user_name = json_data["data"]["options"][0]["value"]
            response_data = {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": f"Hello {user_name}",
                    "flags": InteractionResponseFlags.EPHEMERAL,
                },
            }
        else:
            response_data = {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": "Hello world",
                },
            }
        return response_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
