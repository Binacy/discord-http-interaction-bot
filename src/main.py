import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from utils import (
    InteractionType,
    InteractionResponseType,
    InteractionResponseFlags,
    CustomHeaderMiddleware,
)
from core import CommandHandler

app = FastAPI(middleware=[Middleware(CustomHeaderMiddleware)])


@app.post("/")
async def interactions(request: Request):
    json_data = await request.json()

    if json_data["type"] == InteractionType.PING:
        # A ping test sent by discord to check if your server works
        return {"type": InteractionResponseType.PONG}

    handler = CommandHandler(json_data)
    result = handler.execute()
    if result is not None:
        return result
    # No result means either the command is not found or the command is not registered
    # Or you havent implemented the command yet
    # Or you forgot to return the result
    # Or idk just check it man i cant do everything for you
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": "Hello Buddy, This is a by default message for any unrecognized interaction.",
            "flags": InteractionResponseFlags.EPHEMERAL,
        },
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
