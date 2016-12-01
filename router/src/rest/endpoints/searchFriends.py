#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconnect
import codes

'''
Author: Angel Soriano
Description: Endpoint to return all users matching a certain string
'''

searchFriendsBlueprint = Blueprint('searchFriends', __name__, template_folder='templates')
@searchFriendsBlueprint.route("/searchFriends/", methods=['POST'])
def searchFriends(username = None):
    if username is None:
        payload = request.json
        username = payload['username']
    
    query = "SELECT `username`, `bio`, `idusers` FROM `users` WHERE `username` LIKE '\%%s\%' AND `privacy` = 'PUBLIC'"
    
    try:
        cursor = dbconnect.__change_data(query, (username,))
        return json.dumps(cursor)
    except:
        return codes.JSON_FAILURE
