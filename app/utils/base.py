import uuid
import requests
import aiohttp
from fastapi import HTTPException, status
from app.utils.logger import logger
from app.config import configs as p

def request_api(
    method: str,
    url: str,
    body: dict = None,
    headers: dict = None,
    verify=p.IS_TLS_ENABLE,
    timeout=60,
) -> dict:
    response = requests.request(
        method,
        url,
        json=body,
        headers=headers,
        verify=verify,
        timeout=timeout,
    )
    # response.raise_for_status()
    status_code = response.status_code
    if str(status_code).startswith('2'):
        response_data = response.json()
    else:
        response_data = {}
    return response_data, status_code

async def async_request_api(method: str, url: str, body: dict = None, headers: dict = None, timeout=60) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=body, headers=headers, timeout=timeout) as response:
                response.raise_for_status()
                data = await response.json()
                return data
    except Exception as e:
        error_message = f"Request to {url} failed: {e}"
        logger.error(error_message)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=error_message,
        )

def get_uuid():
    return str(uuid.uuid4())

def message_exists(key, value):
    return f"{key} exists: The {key} '{value}' already exists"

def message_not_found(key, value):
    return f"{key} not found: The {key} '{value}' was not found"