from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/speechDB.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Flask admin
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'super secret key' # Add this to avoid an error
