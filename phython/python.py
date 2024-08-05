from flask import Flask, render_template, request

app = Flask (name_)

@app.route('/', methods=['GET', 'POST'])

def register():

if request.method == 'POST':

name = request.form['name']

email = request.form['email']

age = request.form['age']
return "Registration successful! Thank you for registering."

else:

return render_template('register.html')

if_name__ == '_main_':

app.run(host='0.0.0.0', port-5000, debug=True)

