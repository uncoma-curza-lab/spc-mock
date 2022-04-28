from flask_restful import Resource

class Version(Resource):
    def get(self):
        return {
            'version': '1.0',
            'comment': 'You are running SPC MOCK application'
        }, 200

class Health(Resource):
    def get(self):
        return {
            'status': 'SPC MOCK is up and running'
        }, 200
