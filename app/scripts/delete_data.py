"""
Script to delete some data.

Launch: $ python -m app.scripts.delete_data
"""
from database import SessionLocal
from models import User, Post

db = SessionLocal()


def delete_post(post_id: int):
    """Post deletion."""
    post = db.query(Post).filter_by(id=post_id).first()
    if not post:
        print(f"Post with ID '{post_id}' not found.")
        return
    print(f"Deleting post ID '{post_id}' with title '{post.title}'...")
    db.delete(post)
    db.commit()
    print("Post deleted successfully!")


def delete_user_and_posts(username: str):
    """User and post deletion."""
    user = db.query(User).filter_by(username=username).first()
    if not user:
        print(f"User '{username}' not found.")
        return
    print(f"Deleting user '{username}' and all their posts...")

    posts = db.query(Post).filter_by(user_id=user.id).all()
    for post in posts:
        print(f"Deleting post ID '{post.id}' with title '{post.title}'...")
        db.delete(post)

    db.delete(user)
    db.commit()
    print(f"User '{username}' and all their posts deleted successfully!")


if __name__ == "__main__":
    print("Deleting a Post:")
    delete_post(1)

    print("\nDeleting a User and Their Posts:")
    delete_user_and_posts("artem")


db.close()
