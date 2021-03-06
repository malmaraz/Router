#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes
import logging

'''
Description: Rest endpoint for updating a user
Author: Martin Almaraz
'''

updateUserBlueprint = Blueprint('updateUser', __name__, template_folder='templates')
@updateUserBlueprint.route("/updateUser/", methods=['POST'])
def updateUser(username = None, password = None, bio = None, privacy = None, userid = None, email = None):

    if username is None:
        logging.info('updateUser: ' + str(request.json))
        username = request.json['username']
        bio = request.json['bio']
        email = request.json['email']
        privacy = request.json['privacy']
        userid = request.json['user_id']
    query = "UPDATE `users` SET `username` = %s, `bio` = %s, `email` = %s, `privacy` = %s WHERE `idusers` = %s"
    args = (username, bio, email, privacy, userid)

    try:
        dbconnect.__change_data(query, args)
        return codes.JSON_SUCCESS
    except Exception as e:
        logging.error('updateUser: ' + str(e))
        return codes.JSON_FAILURE
