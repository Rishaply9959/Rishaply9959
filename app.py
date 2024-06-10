from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Flask-Mailb
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.json.get('email')
    otp = random.randint(100000, 999999)
    session['otp'] = otp
    session['email'] = email
    
    msg = Message('Your OTP', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your OTP is {otp}'
    mail.send(msg)
    
    return jsonify({'message': 'OTP sent'})

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    entered_otp = request.json.get('otp')
    if session.get('otp') == int(entered_otp):
        return jsonify({'message': 'OTP verified'})
    return jsonify({'message': 'Invalid OTP'}), 400

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print(data)  # Handle form submission logic here
    return jsonify({'message': 'Form submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
    
