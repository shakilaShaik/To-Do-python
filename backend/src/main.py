from flask import Flask  
from config.connection import db
from routes.routes import task_bp


app = Flask(__name__)
   
app.db= db

@app.route('/')
def home():
   return 'hello world'
if __name__ =='__main__':
   app.register_blueprint(task_bp) 
   app.run(debug=True)
  
   


