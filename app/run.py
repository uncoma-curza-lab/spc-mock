from flask import Flask
from flask_restful import Api

from resources.utils import Version, Health

from resources.resource_factory  import All, One, OneOf

app = Flask(__name__)
api = Api(app)

utils_prefix = '/utils'
application_prefix = '/api/v1'

api.add_resource(Health, utils_prefix + '/health')
api.add_resource(Version, utils_prefix + '/version')

api.add_resource(All, application_prefix + '/<string:resource>')
api.add_resource(One, application_prefix + '/<string:resource>/<int:resourceId>')
api.add_resource(OneOf, application_prefix + '/<string:resource>/<string:depends>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
