import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['CORS_HEADERS'] = 'Content-Type'

# Mail SMTP settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

CORS(app)
mail = Mail(app)

# load the views
from app import views