import shutil
from fastapi import FastAPI, Request, UploadFile, File
from starlette.middleware.cors import CORSMiddleware

from sql.Payment.router import payment_router
from sql.database import db_instance

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/fileupload/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# 서버 시작시 db connect
@app.on_event("startup")
async def startup():
    await db_instance.connect()

# 서버 종료시 db disconnect
@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()

# fastapi middleware, request state 에 db connection 심기
@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response

app.include_router(payment_router)