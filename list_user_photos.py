import os
from app import app, db
from app.models import User

def list_user_photos():
    upload_folder = os.path.abspath('uploads')
    users = User.query.all()
    print("User photo filenames and existence in uploads directory:")
    for user in users:
        photo = user.photo
        photo_path = os.path.join(upload_folder, photo) if photo else None
        exists = os.path.isfile(photo_path) if photo else False
        print(f"User: {user.username}, Photo: {photo}, Exists: {exists}")

if __name__ == "__main__":
    with app.app_context():
        list_user_photos()
