from flask import Flask, request, json, Response
from .models.enfoModel import Animal, AnimalSchema
from flask_sqlalchemy import SQLAlchemy
from .config import app_config
from .models import db

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  # This would be a function that accepts a configuration object as an argument, and returns a Flask application instance, configured with those settings.
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)
  animal_schema = AnimalSchema()

#A common pattern with decorators is to use them to register 
# functions as callbacks for certain events. 
# In this case, the @app.route decorator creates an 
# association between the URL given as an argument and the function.
  @app.route('/', methods=['GET'])
  def index():
    # print("inside animal_detail")
    enfo_animal = Animal.query.get('African Bush Elephant')
    result_enfo = animal_schema.dump(enfo_animal, many=False).data
    return custom_response(result_enfo, 200)
    # return 'Congratulations! Your first endpoint is workin'
    # return jsonify(enfo_animal)

    """
    example endpoint
    """
  return app
    
    # return 'Congratulations! Your first endpoint is workin'
def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )