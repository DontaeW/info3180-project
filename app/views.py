"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import flash, render_template, request, jsonify, send_file,send_from_directory
import os,jwt,base64
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.forms import FavouriteForm, LoginForm, SignUpForm, ProfileForm
from app.models import User, Favourite, Profile
from datetime import datetime, timedelta

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()}), 200

@app.route("/api/v1/generate-token")
def generate_token():
    timestamp = datetime.now()
    # do i update to have username and password?
    payload = {
        "sub": 1,
        "iat": timestamp,
        "exp": timestamp + timedelta(hours=24)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return token

@app.route('/api/register', methods=["POST"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            email = request.form['email']
            photo = request.files['photo']

            filename = secure_filename(f"{username}_profile_photo.jpg")
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)
            # with open(photo_path, "wb") as fh:
            #     fh.write(base64.decodebytes(photo.split(",")[1].encode()))

            user = User(username, password, name, email, filename)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': f"Account successfully created for {username}!"})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({"errors": form_errors(form)}), 400

@app.route('/debug/users', methods=['GET'])
def debug_users():
    if app.debug:  # Only works in debug mode
        users = User.query.all()
        user_list = [{"id": user.id, "username": user.username} for user in users]
        return jsonify(user_list)
    return jsonify({"error": "Not available"}), 403

@app.route('/api/auth/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                token = generate_token()
                return jsonify({'message': 'Login successful!', 'token': token}), 200
            return jsonify({'errors': ['Invalid credentials']}), 401
        return jsonify({'errors': form_errors(form)}), 400
    except Exception as e:
        app.logger.error(f"Login error: {e}")
        return jsonify({'errors': ['An unexpected error occurred.']}), 500

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Successfully logged out', 'redirect_url': "/"}), 200

@app.route('/api/profiles', methods=['POST'])
@login_required
def create_profile():
    data = request.json
    try:
        profile = Profile(**data, user_id_fk=current_user.id)
        db.session.add(profile)
        db.session.commit()
        return jsonify({'message': 'Profile created'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/profiles', methods=['GET'])
@login_required
def list_profiles():
    profiles = Profile.query.filter(Profile.user_id_fk != current_user.id).all()
    return jsonify([p.__dict__ for p in profiles])

@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@login_required
def get_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(profile.__dict__)

@app.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
@login_required
def favourite_profile(user_id):
    if user_id == current_user.id:
        return jsonify({'error': 'Cannot favourite yourself'}), 403

    existing = Favourite.query.filter_by(user_id_fk=current_user.id, fav_user_id_fk=user_id).first()
    if existing:
        return jsonify({'message': 'Already favourited'}), 200

    fav = Favourite(user_id_fk=current_user.id, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify({'message': 'User favourited'}), 201

@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@login_required
def user_favourites(user_id):
    if current_user.id != user_id:
        return jsonify({'error': 'Access denied'}), 403

    favourites = Favourite.query.filter_by(user_id_fk=user_id).all()
    result = [f.favourite_user.__dict__ for f in favourites]
    return jsonify(result)

@app.route('/api/users/favourites/top/<int:N>', methods=['GET'])
@login_required
def top_favorited_users(N):
    results = db.session.query(Favourite.fav_user_id_fk, db.func.count(Favourite.id).label('fav_count')).group_by(Favourite.fav_user_id_fk).order_by(db.desc('fav_count')).limit(N).all()

    users = [User.query.get(uid).__dict__ for uid, count in results]
    return jsonify(users)


###
# The functions below should be applicable to all Flask apps.
###


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    # response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
    # response.headers["Content-Type"] = "application/json"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@login_required
def get_matches(profile_id):
    
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Authorization token missing"}), 401
    
    try:
        token = token.split(" ")[1]  # Extract the actual token from "Bearer <token>"
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        if decoded_token.get('user_id') != current_user.id:
            return jsonify({"error": "Unauthorized access"}), 403

        current_profile = Profile.query.get_or_404(profile_id)  # Get the selected profile
        other_profiles = Profile.query.filter(Profile.user_id_fk != current_profile.user_id_fk).all()  # Exclude current user

        matched_profiles = []

        for profile in other_profiles:
            # Age difference check
            if abs(current_profile.birth_year - profile.birth_year) > 5:
                continue

            # Height difference check (must be between 3 to 10 inches)
            if not (3 <= abs(current_profile.height - profile.height) <= 10):
                continue

            # Count shared preferences
            shared_traits = sum([
                current_profile.fav_cuisine.lower() == profile.fav_cuisine.lower(),
                current_profile.fav_color.lower() == profile.fav_color.lower(),
                current_profile.fav_school_subject.lower() == profile.fav_school_subject.lower(),
                current_profile.political == profile.political,
                current_profile.religious == profile.religious,
                current_profile.family_oriented == profile.family_oriented
            ])

            # Minimum 3 shared traits required
            if shared_traits >= 3:
                matched_profiles.append({
                    "profile_id": profile.id,
                    "user_id": profile.user_id_fk,
                    "name": User.query.get(profile.user_id_fk).name,
                    "photo": f"/api/photo/{profile.photo}",
                    "birth_year": profile.birth_year,
                    "height": profile.height,
                    "fav_cuisine": profile.fav_cuisine,
                    "fav_color": profile.fav_color,
                    "fav_school_subject": profile.fav_school_subject,
                    "political": profile.political,
                    "religious": profile.religious,
                    "family_oriented": profile.family_oriented
                })

        return jsonify({"matching_profiles": matched_profiles}), 200
    
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
