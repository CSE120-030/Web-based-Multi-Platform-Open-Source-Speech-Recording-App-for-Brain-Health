from flask import json
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from myapp import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Users"
    userId = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable= False)

class Language(db.Model):
    __tablename__ = "Languages"
    languageId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    prefix = db.Column(db.String(50))



class Expert(db.Model):
    __tablename__ = "Experts"
    expertId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable= False)
    lastName = db.Column(db.String(100), nullable= False)
    licenseNumber = db.Column(db.String(50), nullable=False)
    # relationship to user table one to one
    userId = db.Column(db.Integer, db.ForeignKey("Users.userId", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref= db.backref("Experts", useList = False, cascade="all, delete, delete-orphan"))

class Patient(db.Model):
    __tablename__ = "Patients"
    patientId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    # relationship to language. One to Many
    languageId = db.Column(db.Integer, db.ForeignKey("Languages.languageId", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    language = db.relationship("Language", backref = "Patients", lazy=True, cascade = "all,delete, delete-orphan")
    # relationship to expert. One to Many
    expertId = db.Column(db.Integer, db.ForeignKey("Experts.expertId", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    expert = db.relationship("Expert", backref=db.backref("Patients",lazy=True, cascade="all, delete, delete-orphan"))
    # relationship to user one to one
    userId = db.Column(db.Integer, db.ForeignKey("Users.userId", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("Patients", useList=False, cascade="all, delete, delete-orphan"))

class Image(db.Model):
    __tablename__ = "Images"
    imageId = db.Column(db.Integer, primary_key=True)
    filePath =db.Column(db.Text, nullable=False)
    name = db.Column(db.String(100), nullable= False)

class TypeOfPrompt(db.Model):
    __tablename__ = "TypeOfPrompts"
    typeOfPromptId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)

class GroupOfPrompt(db.Model):
    __tablename__ = "GroupOfPrompts"
    groupOfPromptId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

class Prompt(db.Model):
    __tablename__ = "Prompts"
    promptId = db.Column(db.Integer, primary_key=True)
    descriptionPrompt = db.Column(db.Text, nullable=False)
    # relationship to language One to Many
    languageId = db.Column(db.Integer, db.ForeignKey("Languages.languageId", onupdate="CASCADE", ondelete="CASCADE"),
                         nullable=False)
    language = db.relationship("Language", backref=db.backref("Prompts", lazy=True, cascade="all, delete, delete-orphan"))
    # relationship to expert table. One to many
    expertId = db.Column(db.Integer, db.ForeignKey("Experts.expertId", onupdate="CASCADE", ondelete="CASCADE"),
                           nullable=False)
    expert = db.relationship("Expert",
                               backref=db.backref("Prompts", lazy=True, cascade="all, delete, delete-orphan"))

    # relationship to image One to many
    imageId = db.Column(db.Integer, db.ForeignKey("Images.imageId", onupdate="CASCADE", ondelete="CASCADE"),
                           nullable=False)
    image = db.relationship("Image",
                               backref=db.backref("Prompts", lazy=True, cascade="all, delete, delete-orphan"))

    # relationship to type of prompt One to many
    typeOfPromptId = db.Column(db.Integer, db.ForeignKey("TypeOfPrompts.typeOfPromptId", onupdate="CASCADE", ondelete="CASCADE"),
                        nullable=False)
    image = db.relationship("TypeOfPrompt",
                            backref=db.backref("Prompts", lazy=True, cascade="all, delete, delete-orphan"))


#relationship to prompt to group_of_prompt Many to manny
class ListGroup(db.Model):
    __tablename__ = 'ListGroups'
    listGroupId = db.Column(db.Integer, primary_key=True)
    # relationship to group of prompt
    groupOfPromptId = db.Column(db.ForeignKey("GroupOfPrompts.groupOfPromptId"),primary_key=True)
    promptId = db.Column(db.ForeignKey("Prompts.promptId"),primary_key=True)
    groupOfPrompt = db.relationship("GroupOfPrompt", back_populates="Prompts")
    prompt = db.relationship("Prompt", back_populates="GroupOfPrompts")


class Assignment(db.Model):
    __tablename__ = 'Assignments'
    assignmentId = db.Column(db.Integer, primary_key=True)
    dateOfAssignment = db.Column(db.DateTime, nullable=False)
    stateOfPrompt = db.Column(db.Boolean, nullable=False)
    expertNote = db.Column(db.Text, nullable=False)
    # relationship to group of prompts One to many
    groupOfPromptsId = db.Column(db.Integer, db.ForeignKey("GroupOfPrompts.groupOfPromptId", onupdate="CASCADE", ondelete="CASCADE"),
                        nullable=False)
    groupOfPrompts = db.relationship("GroupOfPrompt",
                            backref=db.backref("Assignments", lazy=True, cascade="all, delete, delete-orphan"))

    # relationship to expert One to many
    expertId = db.Column(db.Integer, db.ForeignKey("Experts.expertId", onupdate="CASCADE", ondelete="CASCADE"),
                                 nullable=False)
    expert = db.relationship("Expert",
                                     backref=db.backref("Assignments", lazy=True, cascade="all, delete, delete-orphan"))

    # relationship to patient One to many
    patientId = db.Column(db.Integer, db.ForeignKey("Experts.expertId", onupdate="CASCADE", ondelete="CASCADE"),
                         nullable=False)
    patient = db.relationship("Patient",
                             backref=db.backref("Assignments", lazy=True, cascade="all, delete, delete-orphan"))

class TypeOfMedia(db.Model):
    __tablename__ = 'TypeOfMedias'
    typeOfMediaId = db.Column(db.Integer, primary_key=True)
    nameMedia = db.Column(db.String(50), nullable=False)
    extension= db.Column(db.String(10),nullable=False)




class Media(db.Model):
    __tablename__ = 'Medias'
    mediaId = db.Column(db.Integer, primary_key=True)
    mediaNote = db.Column(db.Text, nullable=False)
    filePath = db.Column(db.Text, nullable=False)
    # relationship to assignment table One to Many
    assignmentId = db.Column(db.Integer, db.ForeignKey("Assignments.assignmentId", onupdate="CASCADE", ondelete="CASCADE"),
                          nullable=False)
    assignment = db.relationship("Assignment",
                              backref=db.backref("Medias", lazy=True, cascade="all, delete, delete-orphan"))
    # relationship to prompt id
    promptId = db.Column(db.Integer, db.ForeignKey("Prompts.promptId", onupdate="CASCADE", ondelete="CASCADE"),
                             nullable=False)
    prompt = db.relationship("Prompt",
                                 backref=db.backref("Medias", lazy=True, cascade="all, delete, delete-orphan"))

    # relationship to type of media One to many
    typeOfMediaId = db.Column(db.Integer, db.ForeignKey("TypeOfMedias.typeOfMediaId", onupdate="CASCADE", ondelete="CASCADE"),
                             nullable=False)

    typeOfMedia = db.relationship("TypeOfMedia",
                             backref=db.backref("Medias", lazy=True, cascade="all, delete, delete-orphan"))

db.create_all() # create_db








