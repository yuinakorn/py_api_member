from sqlalchemy.orm import Session

from models.dep.dep_model import DbDep


def read_deps(db: Session):
    return db.query(DbDep).all()


def read_dep_by_id(db: Session, id: int):
    return db.query(DbDep).filter(DbDep.div_code == id).first()
