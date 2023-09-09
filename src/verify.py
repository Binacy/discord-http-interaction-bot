from nacl.signing import VerifyKey
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_PUBLIC_KEY = os.getenv("CLIENT_PUBLIC_KEY")


def verify_key(
    raw_body: bytes, signature: str, timestamp: str, client_public_key: str
) -> bool:
    message = timestamp.encode() + raw_body
    try:
        vk = VerifyKey(bytes.fromhex(client_public_key))
        vk.verify(message, bytes.fromhex(signature))
        return True
    except Exception as ex:
        print(ex)
    return False


async def set_body(request: Request, body: bytes):
    async def receive():
        return {"type": "http.request", "body": body}

    request._receive = receive


async def get_body(request: Request) -> bytes:
    body = await request.body()
    await set_body(request, body)
    return body


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        signature = request.headers["X-Signature-Ed25519"]
        timestamp = request.headers["X-Signature-Timestamp"]
        request_body = await get_body(request)
        if (
            signature is None
            or timestamp is None
            or not verify_key(request_body, signature, timestamp, CLIENT_PUBLIC_KEY)
        ):
            return Response("Bad request signature", status_code=401)
        response = await call_next(request)
        return response
