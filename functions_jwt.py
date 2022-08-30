from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from jwt import encode, decode
from datetime import datetime, timedelta
from os import getenv

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2) }, key=getenv('SECRET'), algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output:
            decode(token, key=getenv('SECRET'), algorithms=["HS256"])
        decode(token, key=getenv('SECRET'), algorithms=["HS256"])
    except:
        pass
