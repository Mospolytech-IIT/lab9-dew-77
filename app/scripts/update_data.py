"""
Script to update some data.

Launch: $ python -m app.scripts.update_data
"""
from database import SessionLocal
from models import User, Post

db = SessionLocal()


def update_user_email(username: str, new_email: str):
    """Query to update email field on user."""
    user = db.query(User).filter_by(username=username).first()
    if not user:
        print(f"User '{username}' not found.")
        return
    print(f"Updating email for user '{username}' from '{user.email}' to '{new_email}'...")
    user.email = new_email
    db.commit()
    print("Email updated successfully!")


def update_post_content(post_id: int, new_content: str):
    """Query to update post content."""
    post = db.query(Post).filter_by(id=post_id).first()
    if not post:
        print(f"Post with ID '{post_id}' not found.")
        return
    print(f"Updating content for post ID '{post_id}'...")
    print(f"Old Content: {post.content}")
    post.content = new_content
    db.commit()
    print("Content updated successfully!")
    print(f"New Content: {post.content}")


# Вызываем функции для демонстрации
if __name__ == "__main__":
    print("Updating User Email:")
    update_user_email("oleg", "new_oleg@example.com")

    print("\nUpdating Post Content:")
    update_post_content(2, "Sunlight closed!")

# Закрываем сессию
db.close()
