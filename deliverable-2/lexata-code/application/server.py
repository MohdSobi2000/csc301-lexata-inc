from flask import Flask, request, send_from_directory
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS, cross_origin
from backend.lexata import Lexata
import json

# Instantiating the application
# The static folder argument points to the build folder in the frontend directory, which basically
# stores all the data and information to successfully render the frontend
app = Flask(__name__, static_folder='frontend/build', static_url_path='')  # whatever folder the frontend is in, we use
# that path
api = Api(app)
CORS(app)


# Frontend
@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


# Class which represents the search application
class SearchEngine(Resource):

    # API Methods
    @cross_origin()
    def post(self):
        k = 20
        sectors = None

        # Get arguments from request
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('num_results', type=int, help="Number of risk factors you want in your search results. Should be an integer.")
        parser.add_argument('sectors', type=str, action='append', help="Sectors through which you want to filter the"
                                                                       " risk factors. Should be a list of sectors separated by commas.")
        args = parser.parse_args()
        # Parsing through the arguments
        if args['num_results']:
            k = args['num_results']
        if args['sectors']:
            sectors = args['sectors'][0].split(',')
            for i in range(len(sectors)):
                sectors[i] = sectors[i].strip()

        # Get Query from the body
        query = request.get_data().decode('utf-8').replace('\n', '')

        # Call the backend to get search results to send to the request caller
        lexata = Lexata()
        try:
            results = lexata.get_closest_to(query, k, sectors)
        except Exception:
            abort(400, message="Error occured during search")
        else:
            output = json.dumps(results)
            return output, 200


# Command to add search engine route to api
api.add_resource(SearchEngine, "/api/search")

if __name__ == "__main__":
    app.run(debug=True)  # Change debug to False during deployment
