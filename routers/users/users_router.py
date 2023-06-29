from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.database import get_db
from routers.users import users_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", dependencies=[Depends(access_user_token)])
def get_all_user(db: Session = Depends(get_db)):
    return users_controller.read_users(db)


@router.get("/{id}", dependencies=[Depends(access_user_token)])
def user_by_id(id, db: Session = Depends(get_db)):
    return users_controller.read_user_by_id(db, id)


@router.post("/login", dependencies=[Depends(access_user_token)])
def login(user: str, password: str):
    return users_controller.login(user, password)
