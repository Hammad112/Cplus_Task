from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, weather

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User & Weather API")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    if db.query(models.User).filter(models.User.phone_number == user.phone_number).first():
        raise HTTPException(status_code=400, detail="Phone number already exists")

    new_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        phone_number=user.phone_number,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful"}

@app.get("/weather/{city}")
def weather_forecast(city: str):
    try:
        return weather.get_weather_forecast(city)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
