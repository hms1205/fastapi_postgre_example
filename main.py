from fastapi import FastAPI, Depends
from core import models
from core.base import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/")
def root():
    return {"message": "This is backend side API section."}


@app.get("/api/users")
def get_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()


@app.get("/api/createuser")
def create_user(username: str, password: str, email: str, db=Depends(get_db)):
    # User 객체 생성
    db_user = models.User(username=username, password=password, email=email)
    # db에 추가
    db.add(db_user)
    # 반영
    db.commit()
    # 새로고침
    db.refresh(db_user)
    return db_user
