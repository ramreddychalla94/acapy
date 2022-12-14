from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, request_schema, response_schema
import hmac
import hashlib
import json
import os
import hashlib
import uuid
import hmac
from datetime import datetime, timedelta
import base64


async def verify_webhook(data, hmac_header):
    digest = hmac.new(get_secret_key(), data.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    # computed_hmac = base64.b64encode(digest)
    return hmac.compare_digest(digest, hmac_header)

def get_secret_key():
    return os.urandom(64)

@docs(tags=["security"], summary="To provide authentication to ACA-py lib")
async def generate_token(request: web.BaseRequest) -> json:
    body = await request.json()
    data = body.get("message")
    hmac_digest = hmac.new(get_secret_key(), data.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    #to do
    hmac_digest.update()
    return web.json_response({"Token": hmac_digest})


@docs(tags=["security"], summary="To provide authentication to ACA-py lib")
async def fetch_data(request: web.BaseRequest) -> json:
    body = await request.json()
    data = body.get("message")
    verified = verify_webhook(data, request.headers.get('X-Signature-SHA256'))
    if not verified:
        return web.json_response({"message": "Unauthorized Access"})
    else:
        return web.json_response({"message": "Access Granted"})


async def register(app: web.Application):
    """Register routes"""

    app.add_routes(
        [web.post("/provide-security", generate_token),
         web.get("/validate-security", fetch_data, allow_head=False)]
    )


def post_process_routes(app: web.Application):
    """Amend swagger API."""

    # Add top-level tags description
    if "tags" not in app._state["swagger_dict"]:
        app._state["swagger_dict"]["tags"] = []
    app._state["swagger_dict"]["tags"].append(
        {
            "name": "security",
            "description": "testing security"
        }
    )
