from flask import Flask, request
from routes import predict, user
from flask_restx import Api, Resource, fields
from extentions import cache

app = Flask(__name__)

#configure cache
app.config['CACHE_TYPE'] = 'SimpleCache'


#initialize cache
cache.init_app(app)


## import blueprint here and register it
app.register_blueprint(user.user_bp)
app.register_blueprint(predict.predict_bp)




if __name__ == "__main__":
    app.run(debug=True)











# #configure your swagger UI
# api = Api(app, title="Flask API Documentation", description="Test your APIs here",  doc="/docs")


# #create namespace
# hello_ns = api.namespace("Hello", description="Hello World API", path= "/hello")
# user_ns = api.namespace("User", description="User CRUD Operation", path= "/user")
# pred_ns = api.namespace("Prediction", description="Prediction API", path= "/predict")

# #create class for namespace

# @hello_ns.route("/")
# class Hello(Resource):
#     def get(self):
#         return {"message": "Hello, World!"}


#CRUD Operations for user application
# @user_ns.route("/")
# class User(Resource):
#     def get(self):
#         return {"message": "GET Method Called"}

#     def post(self):
#         return {"message": "POST Method Called"}

#     def put(self):
#         return {"message": "PUT Method Called"}

#     def delete(self):
#         return {"message": "DELETE Method Called"}


# input_model = pred_ns.model('PredictionModel', {
#                         'gestation': fields.List(fields.Float, required=True),
#                         'parity': fields.List(fields.Integer, required=True),
#                         'age': fields.List(fields.Float, required=True),
#                         'height': fields.List(fields.Float, required=True),
#                         'weight': fields.List(fields.Float, required=True),
#                         'smoke': fields.List(fields.Float, required=True)
# })






# ##Prediction API Docs
# @pred_ns.route("/")
# class Prediction(Resource):
#     @pred_ns.expect(input_model)
#     def post(self):
#         """
#         predict the baby weight based on user input data
#         Input data should be in JSON format with the following structure:
#         {
#             "gestation": [value1, value2, ...],
#             "parity": [value1, value2, ...],
#             "age": [value1, value2, ...],
#             "height": [value1, value2, ...],
#             "weight": [value1, value2, ...],
#             "smoke": [value1, value2, ...]
#         }
        
        
#         """
#         baby_data_form = request.get_json()
#         # convert data into dataframe
#         baby_df = pd.DataFrame(baby_data_form)
#         baby_df = baby_df[EXPECTED_COLUMNS]

#         # correct file loading
#         path = os.path.join(os.path.dirname(__file__), "model.pkl")
#         with open(path, 'rb') as obj:
#             model = pickle.load(obj)

#         # make prediction on user data
#         prediction = model.predict(baby_df)
#         prediction = round(float(prediction), 2)

#         # return response in a json format
#         response = {"Prediction": prediction}
#         return response















# def get_cleaned_data(form_data):
#     gestation = float(form_data['gestation'])
#     parity = int(form_data['parity'])
#     age = float(form_data['age'])
#     height = float(form_data['height'])
#     weight = float(form_data['weight'])
#     smoke = float(form_data['smoke'])

#     cleaned_Data = {
#         "gestation": [gestation],
#         "parity": [parity],
#         "age": [age],
#         "height": [height],
#         "weight": [weight],
#         "smoke": [smoke]
#     }
#     return cleaned_Data

# @app.route("/", methods = ["GET"])
# def home():
#     return render_template("index.html")


# # @app.route('/hello', methods = ['GET'])
# # def hello():
# #     return "Hello World!"
    
# EXPECTED_COLUMNS = ['gestation', 'parity', 'age', 'height', 'weight', 'smoke']


# ##define the endpoint
# @app.route("/predict", methods = ["POST"])
# def get_prediction():
#     #get data from user
#     # baby_data_form = request.form
#     baby_data_form = request.get_json()

#     # baby_data_cleaned = get_cleaned_data(baby_data_form)

#     #convert data into dataframe
#     baby_df = pd.DataFrame(baby_data_form)
#     baby_df = baby_df[EXPECTED_COLUMNS]

#     path = os.path.join(os.path.dirname(__file__), "model.pkl")
#     #load machine learning model
#     with open(path, 'rb') as obj:
#         model = pickle.load(obj)
    

#     #make prediction on user data
#     prediction = model.predict(baby_df)

#     prediction = round(float(prediction), 2)

#     #return reponse in a json format
#     response = {"Prediction": prediction}

#     # return render_template("index.html", prediction = prediction)
#     return response


# @app.route('/hello', methods=['GET'])
# def hello():
#     return {"message": "Hello, World!"}


