from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__, template_folder='template')

@app.route('/success/<user>/<int:score>')
def success(user,score):
   return render_template('hello.html', name = user,marks = score)

@app.route('/hello/<int:score>')
def score(score):
   return render_template('hello.html', marks = score)

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      marks = request.form['mark']
      print(user,marks)

      return redirect(url_for('success',user = user,marks=marks))
   else:
      user = request.args.get('marks')
      print(user)
      return redirect(url_for('success',user = user))

if __name__ == '__main__':
   app.run(debug = True)
