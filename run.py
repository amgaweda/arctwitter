#!flask/bin/python
# Instead of 'nf start', just use 'nf run python app.py' 
# if you want to debug your application in development.
from app import app

if __name__=="__main__":
    app.run()