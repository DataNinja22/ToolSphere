from flask import Flask,render_template,request,redirect,session
from db import Database



data_ops=Database()
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    mobile=request.form.get('mobile')
    city=request.form.get('city')
    state=request.form.get('state')
    country=request.form.get('country')
    response = data_ops.insert(email, password, name, mobile, city, state, country)
    if response == "exists":
        return render_template('register.html', error="Email already exists. Please login or register with a different email.")
    elif response:
        return render_template('login.html', message="Registration successful. Please log in.")
    else:
        return render_template('register.html', error="Registration failed. Please try again.")
    

@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if the user exists in the database
    user = data_ops.get_user_by_email(email)
    
    if user is None:
        # Email doesn't exist in database
        return render_template('login.html', error="Email not found. Please register first or check your email address.")
    elif user['password'] != password:
        # Email exists but password is incorrect
        return render_template('login.html', error="Incorrect password. Please try again or use 'Forgot Password' to reset.")
    else:
        # Successful login
        session['user_email'] = email
        return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    if 'user_email' not in session:
        return redirect('/')
    user = data_ops.get_user_by_email(session['user_email'])
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect('/')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forget_pass.html')

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form.get('email')
    # For now, just show a message that the feature is coming soon
    return render_template('forget_pass.html', message="Password reset feature coming soon! Please contact support.")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('term.html')

@app.route('/update_phone')
def update_phone():
    if 'user_email' not in session:
        return redirect('/')
    user = data_ops.get_user_by_email(session['user_email'])
    return render_template('update_phone.html', user=user)

@app.route('/update_password')
def update_password():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('update_password.html')

@app.route('/update_location')
def update_location():
    if 'user_email' not in session:
        return redirect('/')
    user = data_ops.get_user_by_email(session['user_email'])
    return render_template('update_location.html', user=user)

@app.route('/perform_phone_update', methods=['POST'])
def perform_phone_update():
    if 'user_email' not in session:
        return redirect('/')
    
    new_phone = request.form.get('mobile')
    email = session['user_email']
    
    if data_ops.update_user_phone(email, new_phone):
        user = data_ops.get_user_by_email(email)
        return render_template('profile.html', user=user, message="Phone number updated successfully!")
    else:
        user = data_ops.get_user_by_email(email)
        return render_template('update_phone.html', user=user, error="Failed to update phone number. Please try again.")

@app.route('/perform_password_update', methods=['POST'])
def perform_password_update():
    if 'user_email' not in session:
        return redirect('/')
    
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    email = session['user_email']
    
    user = data_ops.get_user_by_email(email)
    
    if user['password'] != current_password:
        return render_template('update_password.html', error="Current password is incorrect.")
    
    if new_password != confirm_password:
        return render_template('update_password.html', error="New passwords do not match.")
    
    if len(new_password) < 6:
        return render_template('update_password.html', error="Password must be at least 6 characters long.")
    
    if data_ops.update_user_password(email, new_password):
        user = data_ops.get_user_by_email(email)
        return render_template('profile.html', user=user, message="Password updated successfully!")
    else:
        return render_template('update_password.html', error="Failed to update password. Please try again.")

@app.route('/perform_location_update', methods=['POST'])
def perform_location_update():
    if 'user_email' not in session:
        return redirect('/')
    
    city = request.form.get('city')
    state = request.form.get('state')
    country = request.form.get('country')
    email = session['user_email']
    
    if data_ops.update_user_location(email, city, state, country):
        user = data_ops.get_user_by_email(email)
        return render_template('profile.html', user=user, message="Location updated successfully!")
    else:
        user = data_ops.get_user_by_email(email)
        return render_template('update_location.html', user=user, error="Failed to update location. Please try again.")

# AI Tools Routes - Under Development
@app.route('/text-summarizer')
def text_summarizer():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('under_development.html', tool_name="Text Summarizer")

@app.route('/translator')
def translator():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('under_development.html', tool_name="Language Translator")

@app.route('/linkedin-generator')
def linkedin_generator():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('under_development.html', tool_name="LinkedIn Post Generator")

@app.route('/data-analysis')
def data_analysis():
    if 'user_email' not in session:
        return redirect('/')
    return render_template('under_development.html', tool_name="Data Analysis Tool")

@app.route('/notify_me', methods=['POST'])
def notify_me():
    if 'user_email' not in session:
        return redirect('/')
    
    tool_name = request.form.get('tool')
    user_email = session['user_email']
    
    # Here you could add the user to a notification list
    # For now, we'll just show a success message
    return render_template('under_development.html', 
                         tool_name=tool_name, 
                         message=f"Great! We'll notify you at {user_email} when {tool_name} is ready.")
    
app.run(debug=True)