import os

from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  print(env_name)
  app = create_app(env_name)
  # run app
  #flask run() method
  app.run()