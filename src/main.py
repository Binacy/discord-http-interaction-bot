import config
from fastapi import FastAPI, Request
from pydantic import BaseModel
from discord_interactions import InteractionType, InteractionResponseType, InteractionResponseFlags
from constants import InteractionType, InteractionResponseType, InteractionResponseFlags, verify_key_decorator

app = FastAPI()

CLIENT_PUBLIC_KEY = config.CLIENT_PUBLIC_KEY
CLIENT_SECRET_KEY = config.CLIENT_SECRET_KEY


class InteractionData(BaseModel):
    name: str
    options: list


@app.post("/")
async def interactions(request: Request, interaction: InteractionData):
    json_data = await request.json()

    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")

    print("Yaha bhi sex waha vi sex har jagah sex")
    print(signature)

    if not signature or not timestamp:
        raise HTTPException(status_code=401, detail="Unauthorized")

    body = await request.body()
    verify_key = hmac.new(
        CLIENT_SECRET.encode(),
        timestamp.encode() + body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, verify_key):
        raise HTTPException(status_code=401, detail="Unauthorized")

    if json_data["type"] == 1:  # Ping event
        return {"type": 1}

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
