from typing import Optional

from fastapi import Header, HTTPException


async def get_auth_token(x_auth_token: Optional[str] = Header(...)):
    return {}


async def limit_params(skip: int = 0, limit: int = 100):
    return {
        "skip": skip,
        "limit": limit,
    }
