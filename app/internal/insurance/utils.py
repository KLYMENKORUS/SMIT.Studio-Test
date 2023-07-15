from functools import wraps
from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist


def doesnt_exist(message):

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except DoesNotExist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=message.format(args[0].cargo_type.value, args[0].date)
                )
        return wrapper

    return decorator


