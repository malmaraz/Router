#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes
import logging

'''
Description: Rest endpoint for processing a friend request
Author: Pearce Reinsch
'''

processRequestBlueprint = Blueprint('processRequest', __name__, template_folder='templates')
@processRequestBlueprint.route("/processRequest/", methods=['POST'])
# takes the Ids of the users of the request and the response
# returns a success/failure response
def processRequest(user_id = None, friend_id = None, response = None):
	insertQuery = "INSERT INTO friend(user_id, friend_id) VALUES(%s,%s)"
	deleteqQuery = "DELETE FROM request WHERE sender_id = %s AND receiver_id = %s"
	
	if(user_id is None):
		user_id = request.json['user_id']
		friend_id = request.json['friend_id']
		response = request.json['response']
		logging.info("processRequest: " + str(payload))
	
	response = response.lower()
	args1 = (user_id, friend_id)
	args2 = (friend_id, user_id)
	if(response == codes.YES):
		try:
			dbconnect.__change_data(insertQuery,args1)
			dbconnect.__change_data(insertQuery,args2)
			dbconnect.__change_data(deleteqQuery,args1)
			return json.dumps(codes.SUCCESS)
		except Exception as e:
			logging.error("processRequest: " + str(e))
			return json.dumps(codes.FAILURE)
	elif(response == codes.NO):
		try:
			dbconnect.__change_data(deleteqQuery,args1)
			return json.dumps(codes.SUCCESS)
		except Exception as e:
			logging.error("processRequest: " + str(e))
			return json.dumps(codes.FAILURE)
