from fastapi import Query, Request
from starlette_context import context


def skip_limit(
        skip: int = Query(
            default=0,
            description="How much to skip",
            ge=0,
        ),
        limit: int = Query(
            default=10,
            description="How much to limit",
            ge=1,
        )
) -> tuple:
    return skip, limit


async def parse_request_body(request: Request):
    """Parse Request Body as JSON"""
    method = str(request.method).upper()
    # only RESTful API support body
    if method in ('GET', 'DELETE', 'POST', 'PUT'):
        context.update(body=await request.body())
