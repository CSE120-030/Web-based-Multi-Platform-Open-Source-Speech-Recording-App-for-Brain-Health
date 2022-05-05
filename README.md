# Speech-Recording-Web-App
## 2022-01-Spring-CSE-Team330 


##### Table of Contents  
[Project Description](#About)   <br>
[Requirements](#requirements)   <br>
[Running the Project](#run)	<br>
[Troubleshooting](#troubleshooting) <br>
...  
<a name="Project-description"/>
<a name="requirements"/>
<a name="run"/>

### About 
<p> Neurodegenerative diseases affect about 50 million people worldwide (NIH). Doctors use speech and language assessments to help predict and diagnose these diseases in patients. However, these assessments tend to only come from English speakers and are very specialist-dependent. In collaboration with the UCSF Memory and Aging Center, (insert team name) developed a web based, multi-language, speech-recording application solution that displays text and picture prompts and records patients responses. With this web application, UCSF and the UdeSA Cognitive Neuroscience Center (Argentina) will analyze the data as a way to find early signs of these neurodegenerative diseases </p>

#### What it does  
<p>
Our goal was to create a proof-of-concept web application with basic functionality. 
</p>

#### Technologies implemented and their uses
<p>
The team utilized the following technologies:
	<ul>
		<li>
			HTML5, CSS3 Bootstrap, JS
			<p>
				To keep a simple MVP, the basic web development languages were used while keeping responsiveness in mind. HTML is rendered from the app.py file paired with a CSS to style the page for better user interface and user experience. 
				The functions found in javascript files in the project completed data requests from the backend server and bring it to the frontend.
			</p>
		</li>
		<li>
			Flask
			<p>
				Flask is a lightweight web python framework. The python files in the Flask application make it easy to add packages responsible for handling login authentication, serving as a database interface for both S3 media buckets and SQLite queries, and in handling user management. Routing in the app.py file has made it possible to render HTML files. 
			</p>
		</li>
		<li>
			SQLite3 
			<p>
				SQLite pairs well with Flask and is used to create static schemas that will serve as a patient information database for the web app.
			</p>
		</li>
		<li>
			AWS S3 Buckets 
			<p>
				An S3 bucket is a container that will serve to hold a NoSQL database, perfect for holding the .wav recording files
			</p>
		</li>
		<li>
			Boto3 Python Module
			<p>
				Boto3 is the Python SDK for AWS which will bridge the S3 Buckets to the Flask app
			</p>
		</li>
	</ul>
</p> 

#### Basic File Structure:

```
 Speech-Recording-Web-App/
├─ venv/
├─ templates/
├─ Audios/
├─ static/
│  ├─ Images/
│  ├─ css/
│  ├─ component.js
│  ├─ speechDB.sqlite
├─ .gitignore
├─ database.py
├─ README.md
```

### Testing
<ol>
	<li>Internal Test
{insert database queries or invisible tings} 
Use Postman to verify successful routing for all pages:
	</li>
	
	<li>Unit Test
{considers visible features}
Responsiveness:
	</li>
	
	<li>Application Test
{verifies scenarios to catch potential bugs}
	</li>
	
	<li>Stress Test
{how the app performs on limited resources}
	</li>
</ol>


#### Challenges faced and hope for the future: 


### Requirements
1. Python 3+ is required to run on this project 
2. python packages required to run the project:

	```python
	flask
	flask-login
	flask-mail
	flask-requests
	flask-paginate
	SQLAlchemy
	boto3
	
	```

3. Install AWS CLI:
	-  https://aws.amazon.com/cli/ and download the installer for your Win/Mac/Linux OS machine
	-  Go back to your terminal and type the following command:
	```Shell
	$aws configure 
	#access and secretkeys will be given
	AWS Access Key ID [None]: accesskey
	AWS Secret Access Key [None]: secretkey
	#you choose to leave the last two answers empty by pressing "enter"
	Default region name [None]: 
	Default output format [None]:
	```


### Run 
- After installing your favorite IDE and python packages, the following commands are used to run the flask app project
- app.py is the driver file that runs the flask app project which is found in the main project directory

	```python
	python3 app.py
	``` 

### Troubleshooting
- if experiencing issues, remove the existing venv folder and create a new python virtual environment in the main directory:

```shell
pip install virtualenv # for bash/zsh users
source venv/bin/activate
pip install flask #continue to installl required packages this way
```
