"""
Script to fetch some data.

Launch: $ python -m app.scripts.fetch_data
"""
from app.database import SessionLocal
from app.models import User, Post

db = SessionLocal()


def fetch_all_users():
    """Query to fetch users."""
    users = db.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")


def fetch_all_posts_with_users():
    """Query to fetch posts with users."""
    posts = db.query(Post).all()
    for post in posts:
        user = post.user
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}, "
              f"User: {user.username} ({user.email})")


def fetch_posts_by_user(username: str):
    """Query to fetch posts by user."""
    user = db.query(User).filter_by(username=username).first()
    if not user:
        print(f"User '{username}' not found.")
        return
    posts = db.query(Post).filter_by(user_id=user.id).all()
    if not posts:
        print(f"No posts found for user '{username}'.")
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")


if __name__ == "__main__":
    print("All Users:")
    fetch_all_users()

    print("\nAll Posts with Users:")
    fetch_all_posts_with_users()

    print("\nPosts by specific user (e.g., 'oleg'):")
    fetch_posts_by_user("oleg")


db.close()
