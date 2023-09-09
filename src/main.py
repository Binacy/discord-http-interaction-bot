import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from utils import (
    InteractionType,
    InteractionResponseType,
    InteractionResponseFlags,
    CustomHeaderMiddleware,
)

app = FastAPI(middleware=[Middleware(CustomHeaderMiddleware)])


@app.post("/")
async def interactions(request: Request):
    json_data = await request.json()

    if json_data["type"] == InteractionType.PING:
        # A ping test sent by discord to check if your server works
        return {"type": InteractionResponseType.PONG}

    elif json_data["type"] == InteractionType.APPLICATION_COMMAND:
        if json_data["data"]["name"] == "hi":
            user_id = json_data["data"]["options"][0]["value"]
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": f"Hello <@!{user_id}>",
                    "flags": InteractionResponseFlags.EPHEMERAL,
                },
            }
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": "Hello world",
        },
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
