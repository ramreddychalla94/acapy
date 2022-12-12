from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, request_schema, response_schema

from marshmallow import fields

from ....admin.request_context import AdminRequestContext
from ....connections.models.conn_record import ConnRecord
from ....messaging.models.openapi import OpenAPISchema
from ....messaging.valid import UUIDFour
from ....storage.error import StorageNotFoundError


@docs(tags=["Security"], summary="To provide authentication to ACA-py lib")
async def add_security(request: web.BaseRequest):
    return web.json_response({"message": "This is sample security endpoint"})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [web.post("/provide-security", add_security)]
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
