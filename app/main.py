"""App entrypoint and routing."""
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import SessionLocal
from .crud import (
    create_user, get_users, get_user, update_user, delete_user,
    create_post, get_posts, get_post, update_post, delete_post,
)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


def get_db():
    """Session dependency getter."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
def list_users(request: Request, db: Session = Depends(get_db)):
    """User list endpoint."""
    users = get_users(db)
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users})


@app.post("/users/")
def create_new_user(
    username: str = Form(...), email: str = Form(...),
    password: str = Form(...), db: Session = Depends(get_db)
        ):
    """User creation endpoint."""
    create_user(db, username, email, password)
    return RedirectResponse("/users/", status_code=303)


@app.get("/users/{user_id}/edit/")
def edit_user_form(
    user_id: int, request: Request, db: Session = Depends(get_db)
        ):
    """Form for user edition."""
    user = get_user(db, user_id)
    return templates.TemplateResponse(
        "user_edit.html", {"request": request, "user": user})


@app.post("/users/{user_id}/edit/")
def update_user_data(
    user_id: int, username: str = Form(...),
    email: str = Form(...), db: Session = Depends(get_db)
        ):
    """User data updation."""
    update_user(db, user_id, username, email)
    return RedirectResponse("/users/", status_code=303)


@app.get("/users/{user_id}/delete/")
def delete_user_data(user_id: int, db: Session = Depends(get_db)):
    """User data deletion."""
    delete_user(db, user_id)
    return RedirectResponse("/users/", status_code=303)


@app.get("/posts/")
def list_posts(request: Request, db: Session = Depends(get_db)):
    """List post endpoint."""
    posts = get_posts(db)
    return templates.TemplateResponse(
        "posts.html", {"request": request, "posts": posts})


@app.post("/posts/")
def create_new_post(
    title: str = Form(...), content: str = Form(...),
    user_id: int = Form(...), db: Session = Depends(get_db)
        ):
    """Post creation endpoint."""
    create_post(db, title, content, user_id)
    return RedirectResponse("/posts/", status_code=303)


@app.get("/posts/{post_id}/edit/")
def edit_post_form(
    post_id: int, request: Request, db: Session = Depends(get_db)
        ):
    """Form fro edit post."""
    post = get_post(db, post_id)
    return templates.TemplateResponse(
        "post_edit.html", {"request": request, "post": post})


@app.post("/posts/{post_id}/edit/")
def update_post_data(
    post_id: int, title: str = Form(...),
    content: str = Form(...), db: Session = Depends(get_db)
        ):
    """Post updating endpoint."""
    update_post(db, post_id, title, content)
    return RedirectResponse("/posts/", status_code=303)


@app.get("/posts/{post_id}/delete/")
def delete_post_data(post_id: int, db: Session = Depends(get_db)):
    """Post data deletion."""
    delete_post(db, post_id)
    return RedirectResponse("/posts/", status_code=303)
