from flask import Flask, request, redirect, url_for, flash, session

app = Flask(__name__)

app.secret_key = 'agri_secure_secret_key'

USERS = {
    "test@farmer.com": "password123"
}

def login_required(user_session):
    return 'user' in user_session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if action == 'register':
            if email in USERS:
                flash("Account already exists! Please log in.", "danger")
            elif not email or not password:
                flash("Email and password fields cannot be empty.", "danger")
            else:
                USERS[email] = password
                flash("Account created successfully! Please log in.", "success")
                
        else:
            if email in USERS and USERS[email] == password:
                session['user'] = email
                return redirect(url_for('home'))
            else:
                flash("Invalid credentials. Try again.", "danger")
                
    from flask import render_template
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been successfully logged out.", "success")
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if not login_required(session):
        flash("Access Denied. Please log in first.", "danger")
        return redirect(url_for('login'))
        
    from flask import render_template
    weather_data = {"temp": "24°C", "condition": "Light Showers Expected", "humidity": "78%"}
    market_prices = {"Maize": "$25 / Bag", "Beans": "$45 / Bag"}
    return render_template('home.html', weather=weather_data, prices=market_prices)

@app.route('/')
def index():
    if login_required(session):
        return redirect(url_for('home'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)