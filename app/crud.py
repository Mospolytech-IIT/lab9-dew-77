"""CRUD operations."""
from sqlalchemy.orm import Session
from .models import User, Post


def create_user(db: Session, username: str, email: str, password: str):
    """User creation."""
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    """Get users."""
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    """Get user."""
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, username: str, email: str):
    """Update user."""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    """User deletion."""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()


def create_post(db: Session, title: str, content: str, user_id: int):
    """Post creation."""
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts(db: Session):
    """Get posts."""
    return db.query(Post).all()


def get_post(db: Session, post_id: int):
    """Get post."""
    return db.query(Post).filter(Post.id == post_id).first()


def update_post(db: Session, post_id: int, title: str, content: str):
    """Update post."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.content = content
        db.commit()
        db.refresh(post)
    return post


def delete_post(db: Session, post_id: int):
    """Post deletion."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
