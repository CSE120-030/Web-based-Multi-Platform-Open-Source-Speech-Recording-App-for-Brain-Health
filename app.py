import copy
from flask_mail import Message,Mail
from flask import Flask, render_template, url_for, redirect, abort, request, send_file
from flask_login import current_user, login_user, login_required, LoginManager, logout_user

from e import send_email
from helper_functions import *
from media_bucket import *
from prompt_helper_functions import *
from assignment_helper import *
from registration import *
from database import *
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
#from token import *
from config import promptCounter

import os
import requests
from urllib.request import urlopen

from copy import deepcopy
from flask_paginate import Pagination, get_page_args
#app = Flask(__name__)


app.config.from_pyfile('config.cfg')
#mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'load'
app.secret_key = 'keep it secret, keep it safe' # Add this to avoid an error

prompt_list=[]
list_length=0
MEDIA_FOLDER = os.path.join('static','Images')
app.config['UPLOAD_FOLDER'] = MEDIA_FOLDER
image_name = ""
prompt_counter=0

prompt_counter_aws=-1

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('load'))


@login_manager.user_loader
def load_user(user_id):

	return get_user_by_id(user_id)

@app.route('/')
def load():
    print("in load function")
    if current_user.is_authenticated:
        if current_user.is_patient() and current_user.check_confirmation()==True:
            return redirect(url_for("patientPortal",patient_name=current_user.get_name()))
        elif current_user.is_patient() and current_user.check_confirmation()==False:
            return redirect(url_for("unconfirmed"))

        elif current_user.is_expert():
            return redirect(url_for("expertPortal",expert_name=current_user.get_name()))

    return render_template("signUp.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    print("in login function")
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
    if user.is_patient() and user.check_confirmation()==True:
        print("in user is patient")
        return redirect(url_for('patientPortal', patient_name=user.get_name()))
    elif current_user.is_patient() and user.check_confirmation() == False:
        return redirect(url_for('unconfirmed'))
    elif user.is_expert():
        return redirect(url_for('expertPortal', expert_name=user.get_name()))

    return redirect(url_for('load'))

@app.route('/expertPortal/', methods=['POST','GET'])
@login_required
def expertPortal():
    if request.method=="GET":
        return render_template("expertPortal.html",prompts = get_file_name_expert(), table= info_expert_portal())


@app.route('/patientPortal/', methods=['POST', 'GET'])
@login_required
def patientPortal():
    if request.method == "GET":
        return render_template("patientPortal.html",your_assignments =get_assignments())

    if request.method == "POST":
        print("in post function")
        print(request.json)
        list_returned = asg_to_do(request.json);
        print("right after asg to do was called")
        print(list_returned)
        print("list_length:",list_length)
        for item in list_returned:
            new_dict = copy.deepcopy(item)
            prompt_list.append(new_dict)
        print("after for loop")
        print("printing prompt list")
        print(prompt_list)
        #return render_template("patientPortal.html")#get_asg_name=asg_to_do(request.json))
        return render_template("prompt.html")#redirect(url_for("do_prompts",prompt_id=0))


@app.route('/patientPortal/do_prompts/<prompt_id>', methods=['POST', 'GET'])
@login_required
def do_prompts(prompt_id):
    print("we got prompt id:",prompt_id)
    if request.method=="GET":
        #print("get method")
        #print(get_prompt_from_list(1))
        try:
            global image_name
            image = get_prompt_from_list(prompt_id)

            for i in image:
                print(type(i))
                print("i: ",i)
                imageId = i["imageId"]


            image_path = load_prompt_photo(imageId) # get image name
            image_name = load_prompt_photo(imageId)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], image_path)
            print(image_path)
            print(full_filename)
            return render_template("prompt.html",specific_prompt=get_prompt_from_list(prompt_id),prompt_queue=get_queue_from_prompt_list(),image = image_path)#,promps=group_name)

        except:
            print("An error happened")
            return redirect(url_for("do_prompts", prompt_id=prompt_id))


    if request.method=="POST":
        return render_template("prompt.html", media_sent=get_media(request.files['audio_data']))


@app.route("/load_promp",methods=["GET"])
def load_prompts():
    #asg_obj = assignment()
    #control_asg = asg_obj.get_asg_counter()
    #control_asg +=1
    #asg_obj.set_asg_counter(control_asg)
    #print("asg id: ", control_asg)
    global prompt_counter
    prompt_counter+=1
    return redirect(url_for("do_prompts",prompt_id=prompt_counter))


@app.route("/getimage", methods = ['POST','GET'])
def get_image():
    if request.method == "GET":
        global image_name
        print("in get image")
        print(image_name)
        return image_name

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

@app.route('/expertPortal/download_prompt/<prompt_name>/', methods=['GET','POST'])
@login_required
def get_prompt(prompt_name):
    global prompt_counter_aws
    if request.method=='GET':
        print(prompt_name)
        if prompt_name=="Spontaneous":

            prompt_counter_aws=0
            print(prompt_counter_aws)
            name_file_dowload = get_file_name_expert()
            print("audio to download:" + name_file_dowload[int(prompt_counter_aws)])
            print(name_file_dowload[int(prompt_counter_aws)])
            file=aws_download(name_file_dowload[int(prompt_counter_aws)])
            return redirect(file,code=302)

        elif prompt_name=="Semi-spontaneous":

            prompt_counter_aws=1
            print(prompt_counter_aws)
            name_file_dowload = get_file_name_expert()
            print("audio to download:"+name_file_dowload[int(prompt_counter_aws)])
            file=aws_download(name_file_dowload[int(prompt_counter_aws)])
            return redirect(file,code=302)

        elif prompt_name=="Non-spontaneous":

            prompt_counter_aws=2
            print(prompt_counter_aws)
            name_file_dowload = get_file_name_expert()
            print(name_file_dowload[int(prompt_counter_aws)])
            file=aws_download(name_file_dowload[int(prompt_counter_aws)])
            return redirect(file,code=302)

        elif prompt_name== "Another_type_of_prompt":
            prompt_counter_aws=3
            print(prompt_counter_aws)
            name_file_dowload = get_file_name_expert()
            print(name_file_dowload[int(prompt_counter_aws)])
            file=aws_download(name_file_dowload[int(prompt_counter_aws)])
            return redirect(file,code=302)


@app.route('/expertPortal/download_prompt/<prompt_name>/<language>/<prompt_id>/<first_name>/<last_name>/<patient_id>', methods=['GET','POST'])
@login_required
def get_prompt2(prompt_name,language,prompt_id,first_name,last_name,patient_id):
    if request.method=='GET':
        #print("audio to download:",prompt_name,language,prompt_id,first_name,last_name,patient_id)
        file_name = prompt_name+'_'+get_prefix(language)+'_'+prompt_id+'_'+first_name+'_'+last_name+'_'+patient_id+'.wav'
        print("file to download",file_name)
        file = aws_download(file_name)
        return redirect(file,code=302)



@app.route('/expertPortal/registration/', methods=['GET','POST'])
@login_required
def registration():
    if request.method=='POST':
        register_patient(request.json)
        t = generate_confirmation_token(request.json['email'])
        confirm_url = url_for('confirm_email', token=t, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(request.json['email'], subject, html)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("expertPortal"))
        #return render_template("registration.html", register = register_patient(request.json))

    elif request.method =='GET':

        return render_template("registration.html", languages = get_languages() )


@app.route('/patientPortal/registration/<token>',methods=['GET','POST'])
@login_required
def confirm_email(token):
    if request.method=="GET":
        try:
            email = confirm_token(token)
            print(email)
        except:
            flash('The confirmation link is invalid or has expired.', 'danger')

        user = db.session.query(User).join(Patient,Patient.userId==User.userId).filter(Patient.userId==get_patient_id()).first()
        print(user)
        #change_status = db.session.query(User).filter(User.username==user[1]).first()
        user.confirmed=1
        print(user.confirmed)
        db.session.commit()
        # add confirm column here
        return render_template("registration_done.html")

@app.route('/patientPortal/unconfirmed' ,methods=['GET','POST'])
@login_required
def unconfirmed():

    return render_template('unconfirmed.html')

@app.route('/patientPortal/resend',methods=['GET','POST'])
@login_required
def resend_confirmation():
    patient = db.session.query(Patient).join(User,User.userId==Patient.userId).filter(Patient.userId==current_user.get_id()).first()
    token = generate_confirmation_token(patient.e)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(patient.e, subject, html)
    return redirect(url_for('unconfirmed'))


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Methods", "GET,DELETE,POST,PUT")
  response.headers.add("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
  #response.headers.add('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token')
  return response

if __name__ == '__main__':
    app.run()
