#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconnect
import codes
import logging

'''
Author: Angel Soriano
Description: Endpoint to remove a friend
'''

removeFriendBlueprint = Blueprint('removeFriend', __name__, template_folder='templates')
@removeFriendBlueprint.route("/removeFriend/", methods=['POST'])
def removeFriend(user_id = None, friend_id = None):
    if user_id is None:
        logging.info('removeFriend: ' + str(request.json))
        payload = request.json
        user_id = payload["user_id"]
        friend_id = payload["friend_id"]

    query = "DELETE  FROM friend WHERE user_id = %s AND friend_id = %s"
    args = (user_id, friend_id)
    args2 = (friend_id, user_id)
    try:
        # execute query
        dbconnect.__change_data(query, args)
        dbconnect.__change_data(query, args2)
        return codes.JSON_SUCCESS

    except:
        logging.error('removeFriend: ' + str(e))
        return codes.JSON_FAILURE
