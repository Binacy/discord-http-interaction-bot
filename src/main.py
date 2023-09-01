import config, uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from constants import InteractionType, InteractionResponseType, InteractionResponseFlags, verify_key

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        signature = request.headers['X-Signature-Ed25519']
        timestamp = request.headers['X-Signature-Timestamp']
        bomdy = await request.body()
        if signature is None or timestamp is None or not verify_key(bomdy, signature, timestamp, CLIENT_PUBLIC_KEY):
            return JSONResponse(status_code=401, content={'reason': "Bad request signature"})
        response = await call_next(request)
        return response

app = FastAPI(middleware=[Middleware(CustomHeaderMiddleware)])

CLIENT_PUBLIC_KEY = config.CLIENT_PUBLIC_KEY

@app.post("/")
async def interactions(request: Request):
    json_data = await request.json()
    if json_data['type'] == InteractionType.PING:
        return {
            'type': InteractionResponseType.PONG
        }
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
    uvicorn.run(app, host="0.0.0.0", port=3000)
