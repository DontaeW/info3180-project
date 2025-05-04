import os

uploads_dir = os.path.join(os.getcwd(), 'app', 'uploads')

def list_photos():
    if not os.path.exists(uploads_dir):
        print(f"Uploads directory not found: {uploads_dir}")
        return
    files = os.listdir(uploads_dir)
    print(f"Files in uploads directory ({uploads_dir}):")
    for f in files:
        print(f)

if __name__ == "__main__":
    list_photos()
