from app import db
from app.models import Profile

def list_profiles():
    profiles = Profile.query.all()
    if not profiles:
        print("No profiles found in the database.")
    else:
        for profile in profiles:
            print(f"Profile ID: {profile.id}, User ID: {profile.user_id_fk}, Description: {profile.description}")

if __name__ == "__main__":
    list_profiles()
