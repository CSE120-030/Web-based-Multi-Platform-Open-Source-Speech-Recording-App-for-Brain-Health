from flask import Flask
import os

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = MEDIA_FOLDER
app.config['SECRET_KEY']=  'this is the key'
app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'
#app.config['MAIL_DEFAULT_SENDER'] = 'smtp.googlemail.com'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ucsfspeechapp@gmail.com'
app.config['MAIL_PASSWORD'] = 'prxzelrcdvjicfvp'
app.config['MAIL_DEFAULT_SENDER'] = 'ucsfspeechapp@gmail.com'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/speechDB.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Flask admin
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'super secret key' # Add this to avoid an error
