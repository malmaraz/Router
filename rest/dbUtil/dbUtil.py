import json

'''
Description: Utility to help communicate with the database
Author: Laura Chavez
'''


class dbUtil():

    def __init__(self):
        '''
        connect to database
        '''
        pass

    def runQuery(self, query):
        '''
        run query, make empty json and return as json file with collumn->value
        tableName-> should be included in the json
        '''

        #this next line creates an empty json string from a python dict {}
        payload = json.dumps({})
        return payload
