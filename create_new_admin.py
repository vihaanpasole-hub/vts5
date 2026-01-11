import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from app import app
from models import db, User
from werkzeug.security import generate_password_hash

NEW_USERNAME = "vtsadmin"
NEW_PASSWORD = "VTS@123"

with app.app_context():
    print("Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

    # Check if user already exists
    user = User.query.filter_by(username=NEW_USERNAME).first()

    if user:
        print("User already exists, updating password")
        user.password = generate_password_hash(NEW_PASSWORD)
    else:
        print("Creating new admin user")
        user = User(
            username=NEW_USERNAME,
            password=generate_password_hash(NEW_PASSWORD)
        )
        db.session.add(user)

    db.session.commit()
    print("New admin ready →", NEW_USERNAME, "/", NEW_PASSWORD)
