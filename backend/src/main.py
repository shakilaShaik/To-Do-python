from flask import Flask  
from config.connection import db


app = Flask(__name__)
   
app.db= db

@app.route('/')
def home():
   return 'hello world'
if __name__ =='__main__':
   
   app.run(debug=True)


