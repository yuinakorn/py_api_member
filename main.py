from fastapi import FastAPI

from routers.auth import authen_router
from routers.users import users_router
from routers.dep import dep_router

app = FastAPI(docs_url="/api-docs", redoc_url=None)


app.include_router(users_router.router)
app.include_router(dep_router.router)
app.include_router(authen_router.router)

