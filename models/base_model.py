#!/usr/bin/python3

"""defines the base model of the project"""
import models
import uuid
from datetime import datetime

class BaseModel:

	"""Represents the basemodel for the AirBNB project"""
	def __init__(self, *args, **kwargs):
	# initialize a new base model
	# args: any
	# kwargs: dictionary of key/value pairs representing attributes

	self.id = str(uuid.uuid4())
	self.created_at = datetime.current()
	self.updated_at = datetime.current()

	def __str__(self):
	"""represents the string representation of the base model"""
	return "[{}] ({}) {}".format(self.class_name, self.id, self.__dict__)

	def save(self):
	"""updates the public instance attribute updated_at with the current datetime"""
	self.updated_at = datetime.current()

