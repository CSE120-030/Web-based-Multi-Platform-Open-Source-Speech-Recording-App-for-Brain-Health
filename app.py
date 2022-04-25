from flask import Flask, render_template, url_for, redirect, abort, request
from flask_login import current_user, login_user, login_required, LoginManager, logout_user
from helper_functions import *
from media_bucket import *
from prompt_helper_functions import *
from assignment_helper import *
#app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'load'
app.secret_key = 'keep it secret, keep it safe' # Add this to avoid an error

@login_manager.user_loader
def load_user(user_id):
	return get_user_by_id(user_id)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method=="GET":
        return render_template("homePage.html")

@app.route('/authentication')
def load():
    if current_user.is_authenticated:
        if current_user.is_patient():
            return redirect(url_for("patientPortal",patient_name=current_user.get_name()))
        elif current_user.is_expert():
            return redirect(url_for("expertPortal",expert_name=current_user.get_name()))
    return render_template("signUp.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    # User already authenticated - serve appropriate portal page
    if current_user.is_authenticated:
        if current_user.is_patient():
            return redirect(url_for('patientPortal', patient_name=current_user.get_name()))
        elif current_user.is_expert():
            return redirect(url_for('expertPortal', expert_name=current_user.get_name()))

     # Get user - if function doesn't return actual user, abort
    user = get_user_by_name(username=request.json['username'])
    print(user)
    if isinstance(user, int):
        abort(404)
    if not user.check_password(request.json['password']):
        abort(409)

    # If password is correct, serve appropriate portal page
    login_user(user)
    # If password is correct, serve appropriate portal page
    if user.is_patient():
        return redirect(url_for('patientPortal', patient_name=user.get_name()))
    elif user.is_expert():
        return redirect(url_for('expertPortal', expert_name=user.get_name()))
    return redirect(url_for('load'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/expertPortal/', methods=['POST','GET'])
@login_required
def expertPortal():
    if request.method=="GET":
        return render_template("expertPortal.html")


@app.route('/patientPortal/', methods=['POST', 'GET'])
@login_required
def patientPortal():
    if request.method == "GET":
        return render_template("patientPortal.html",your_assignments =get_assignments())

    if request.method == "POST":
        return render_template("patientPortal.html",get_asg_name=asg_to_do(request.json))

@app.route('/patientPortal/do_prompt', methods=['POST', 'GET'])
@login_required
def do_prompts():
    if request.method=="GET":
        return render_template("prompt.html")

@app.route('/media', methods=['POST', 'GET'])
def media():
    if request.method=="GET":
        return render_template("media.html")
    if request.method=="POST":
        print("in post method")

        print(request.files['audio_data'])
        return render_template("media.html",media_sent=get_media(request.files['audio_data']))

@app.route('/expertPortal/createPrompt/', methods=['GET','POST'])
@login_required
def createPrompt():
    if request.method=="GET":
        return render_template("create_prompt.html",top=get_all_prompts(),expert=getExpert(),languages=get_languages())

    if request.method=="POST":
        print("in post method")
        print(request.json)
        return render_template("create_prompt.html", promptCreation=prompt_creation(request.json))

if __name__ == '__main__':
    app.run()
