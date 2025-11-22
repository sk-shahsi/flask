# IMPORTING
from flask import Flask, render_template
#INTRACTION
web =  Flask(__name__)

#MAPING
@web.route('/')
@web.route('/register')

#INPUTS
def home():
    return render_template('register.html')
#MAIN
if __name__ == '__main__':
    web.run(debug=True)

