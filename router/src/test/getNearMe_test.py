#!/usr/bin/env python3.5
from . import preTest
import getNearMe
import dbconnect
import json

'''
Description: test for getNearMe api endpoint
Author: Pearce Reinsch
'''

class TestGetNearMe():
	userLat = "36.65"
	userLon = "-121.8"
	dist = "10"
	route1 = "this is a route XD"
	route2 = "this is another route XP"
	routeId1 = "-1"
	routeId2 = "-1"
	startPointLat1 = "36.67"
	startPointLat2 = "-12.8"
	startPointLon1 = "-121.81"
	startPointLon2 = "21.8"
	userid = "123"
	routeName1 = "route1"
	routeName2 = "route2"

	def test_getNearMe(self):
		response = json.loads(getNearMe.getNearMe(self.userLat, self.userLon, self.dist))
		assert response[0]['idroutes'] != self.routeId2
		assert response[0]['idroutes'] == self.routeId1

	def setup_method(self):
		self.routeId1 = dbconnect.insert_data_routes(self.route1,self.startPointLat1,self.startPointLon1,self.userid,self.routeName1)
		self.routeId2 = dbconnect.insert_data_routes(self.route2,self.startPointLat2,self.startPointLon2,self.userid,self.routeName2)
		self.routeId1 = int(self.routeId1[0]['idroutes'])
		self.routeId2 = int(self.routeId2[0]['idroutes'])

	def teardown_method(self):
		dbconnect.delete_data('routes', 'userid', self.userid)