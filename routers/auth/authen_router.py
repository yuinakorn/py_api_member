from dotenv import dotenv_values
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils.oauth2 import create_access_token

config_env = dotenv_values(".env")

router = APIRouter(
    tags=["authentication"]
)


@router.post("/token")
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = request.username == config_env["SYS_USER"] and request.password == config_env["SYS_PASSWORD"]

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    else:
        access_token = create_access_token(data={"sub": request.username})

    return {
        "access_token": access_token,
    }
