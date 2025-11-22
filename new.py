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
        PhoneNumber = request.form['Phone Number']
        return render_template('conform.html',name=name,city=city,PhoneNumber=PhoneNumber)
#MAIN
if __name__ == '__main__':
    web.run(debug=True)

