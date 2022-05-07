# Web-based, Multi-Platform, Open-Source, Speech Recording App for Brain Health

- CSE120 Spring 2022 | Team 330 
    - Members: 
        - Benita Onyenacho, Betsy Avila Aguilar, Jocelyn Chan, Jose Arias Zuniga, Diego Ponce

---
Table of Contents
[ToC]
## Important Links

| Features          | Tutorials               |
| ----------------- |:----------------------- |
| Github Repository | [:link:][GitHub-repo]   |
| Demo Video        | [:link:][Share-Demo]    |

[GitHub-repo]: https://github.com/CSE120-030/Web-based-Multi-Platform-Open-Source-Speech-Recording-App-for-Brain-Health 
[Share-Demo]: https://ucmerced.box.com/s/ki7ac0cw73bm4d5uafo45zfdsbqmmq5l

## :brain: Project Description
<p> Neurodegenerative diseases affect about 50 million people worldwide (NIH). Doctors use speech and language assessments to help predict and diagnose these diseases in patients.  

However, these assessments tend to only come from English speakers and are very specialist-dependent. In collaboration with the UCSF Memory and Aging Center, Team-330 developed a web based, multi-language, speech-recording application solution that displays text and picture prompts and records patients responses. 

With this web application, UCSF and the UdeSA Cognitive Neuroscience Center will analyze the data as a way to find early signs of these neurodegenerative diseases </p>

### Technologies Used
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
				An S3 bucket is a container that will serve to hold a NoSQL database, perfect for holding the .wav recording files and categorizing different language buckets
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

### Basic File Structure
```
 Web-based, Multi-Platform, Open-Source, Speech Recording App for Brain Health/
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
---

## :computer: Getting Started


### 1: Clone the Github Repository on your device
![](https://i.imgur.com/sdfzbnc.png)


To clone the repository you may use Github Desktop App or your favorite shell using the following command:
```shell
	git clone {copy and paste ssh link here}
``` 

### 2: Install Dependencies
0. Install your favorite IDE, ours is [PyCharm ](https://www.jetbrains.com/pycharm/) or [VSCode](https://code.visualstudio.com/) 
2. Install [Python 3.0+](https://www.python.org/downloads/ )
    - ensure pip is up-to-date:
        ```
        $ python -m pip install --upgrade pip #linux/mac
        C:> py -m pip install --upgrade pip #windows
        ```
4. Install Python Packages
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
	- [Download](https://aws.amazon.com/cli/) the AWS CLI installer for your Win/Mac/Linux OS machine
	-  Go back to the terminal and type the following command:
	```Shell
	$aws configure 
	#access and secretkeys will be given
	AWS Access Key ID [None]: accesskey
	AWS Secret Access Key [None]: secretkey
	
    #you can choose to leave the last two answers empty by pressing "enter"
	Default region name [None]: 
	Default output format [None]:
	```
    
### 3: Running the project
While in the main project directory, the flask-app project can easily be ran with the following command:
```python 
    python3 app.py 
```
Depending on browser settings the project can be viewed at: 
    ``` http://localhost:5000 ```
    
The home page should look like this:     
![](https://i.imgur.com/JcVLaMi.png)

---

## :gear: Troubleshooting

### Troubleshooting
- if experiencing issues running modules, remove the existing venv folder and create a new python virtual environment in the main directory:

```shell
pip install virtualenv # for bash/zsh users
source venv/bin/activate
pip install flask #continue to install required packages this way
``` 
- another issue maybe selecting the appropriate python interpreter in your IDE 

