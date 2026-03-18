from typing import Generator

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, EmailStr
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


# -----------------------------
# Database configuration
# -----------------------------
DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# -----------------------------
# SQLAlchemy base
# -----------------------------
class Base(DeclarativeBase):
    pass


# -----------------------------
# SQLAlchemy model (table)
# -----------------------------
class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    course: Mapped[str] = mapped_column(String(100))


# -----------------------------
# Pydantic schemas
# -----------------------------
class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    course: str


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None
    course: str | None = None


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    email: EmailStr
    course: str


# -----------------------------
# Create database tables
# -----------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------
# Dependency: DB session
# -----------------------------
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(title="Dummy Student API")


@app.get("/")
def home():
    return {"message": "Student API is running"}


@app.post("/students", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.scalar(
        select(Student).where(Student.email == student.email)
    )

    if existing_student:
        raise HTTPException(status_code=400, detail="Email already exists")

    db_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


@app.get("/students", response_model=list[StudentRead])
def list_students(db: Session = Depends(get_db)):
    students = db.scalars(select(Student)).all()
    return students


@app.get("/students/{student_id}", response_model=StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.scalar(select(Student).where(Student.id == student_id))

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.put("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, student_data: StudentUpdate, db: Session = Depends(get_db)):
    student = db.scalar(select(Student).where(Student.id == student_id))

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if student_data.email is not None:
        existing_email = db.scalar(
            select(Student).where(
                Student.email == student_data.email,
                Student.id != student_id
            )
        )
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

    if student_data.name is not None:
        student.name = student_data.name
    if student_data.age is not None:
        student.age = student_data.age
    if student_data.email is not None:
        student.email = student_data.email
    if student_data.course is not None:
        student.course = student_data.course

    db.commit()
    db.refresh(student)

    return student


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.scalar(select(Student).where(Student.id == student_id))

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return None