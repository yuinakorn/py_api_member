from dotenv import dotenv_values
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.database import get_connection
from models.users.users_model import DbUser
import hashlib
import pymysql

config_env = dotenv_values(".env")


def read_users(db: Session):
    return db.query(DbUser).all()


def read_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.pid == id).first()


def login(user: str, password: str):
    pass01 = int(len(password) * 90 / 2 * 54 - 68)
    password_hash = hashlib.md5((password + str(pass01) + config_env['HASH_STRING']).encode()).hexdigest()
    print(password_hash)
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT pid,username,t_name,f_name,s_name,position,off_id,div_code,status_id,date_register,date_approve " \
                  " FROM member WHERE username = %s AND password = %s"
            cursor.execute(sql, (user, password_hash))
            result = cursor.fetchone()
            if result is not None:
                return result
            else:
                raise HTTPException(status_code=401, detail="Username or Password is incorrect!!")
    except pymysql.Error as e:
        print("Error => ", e)
        raise HTTPException(status_code=500, detail="Internal server error, Code Error: " + str(e))
