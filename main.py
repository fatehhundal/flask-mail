from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "your_email@gmail.com"
app.config['MAIL_PASSWORD'] = "your_app_password" # NOT normal password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    email = request.form.get('email')
    
    msg = Message(
        subject = 'Email Verification',
        recipients = [email],
        body = "Your email has been successfully verified!"
    )

    mail.send(msg)

    return "Email sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)