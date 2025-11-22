#IMPORT
from flask import Flask,render_template
import os

#Intraction
app = Flask(__name__)

picfolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = picfolder


#Mapping
@app.route('/')

#INPUT
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'],'py.jpeg')
    return render_template('index.html',user_image=pic)
@app.route('/second')
def second():
    # return "Welcome to Second Page"
    return render_template('second.html')


#Main
if  __name__ == '__main__':
    app.run(debug=True)