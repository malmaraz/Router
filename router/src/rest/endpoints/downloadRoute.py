#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Author: Martin Almaraz
Description: Endpoint to download a certain route based on routId
'''

downloadRouteBlueprint = Blueprint('downloadRoute', __name__, template_folder='templates')
@downloadRouteBlueprint.route("/downloadRoute/", methods=['POST'])
def downloadRoute(routeId = None):

    if routeId is None:
        routeId = request.json['routeId']

    query = "SELECT * FROM `routes` WHERE `idroutes` = %s"
    cursor = dbconnect.__change_data(query, (routeId,))
    try:
        route = cursor
        return json.dumps(route[0])
    except Exception as e:
        print(e)
        return codes.JSON_FAILURE
