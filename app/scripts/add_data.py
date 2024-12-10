"""
Script to add some data.

Launch: $ python -m app.scripts.add_data
"""
from database import SessionLocal
from models import User, Post

db = SessionLocal()

users = [
    User(username="oleg", email="oleg@example.com", password="pass1"),
    User(username="artem", email="artem@mail.com", password="pass2"),
    User(username="satoru_gojo", email="go@jo.com", password="pass3")
]

db.add_all(users)
db.commit()

user1 = db.query(User).filter_by(username="oleg").first()
user2 = db.query(User).filter_by(username="artem").first()

posts = [
    Post(title="Post 1 by oleg", content="Text text text", user_id=user1.id),
    Post(title="Post 2 by oleg", content="Text again", user_id=user1.id),
    Post(title="Post 1 by artem", content="=)(0(0ds0fsf))", user_id=user2.id),
]

db.add_all(posts)
db.commit()

db.close()

print("Data creation finished =)")
