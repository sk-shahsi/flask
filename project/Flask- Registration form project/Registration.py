# IMPORTING
from flask import Flask, render_template,request
#INTRACTION
web =  Flask(__name__)

#MAPING
@web.route('/')
@web.route('/register')

#INPUTS
def home():
    return render_template('register.html')

@web.route("/conform" ,methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        return render_template('conformation.html',name=name,city=city,email=email,phone=phone)
#MAIN
if __name__ == '__main__':
    web.run(debug=True)