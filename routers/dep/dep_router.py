from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.database import get_db
from routers.dep import dep_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/department", tags=["department"])


@router.get("/", dependencies=[Depends(access_user_token)])
def get_all_dep(db: Session = Depends(get_db)):
    return dep_controller.read_deps(db)


@router.get("/{id}", dependencies=[Depends(access_user_token)])
def dep_by_id(id, db: Session = Depends(get_db)):
    return dep_controller.read_dep_by_id(db, id)

