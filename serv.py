from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer,primary_key = True)
	key = db.Column(db.String(80),unique = True, nullable = False)
	val = db.Column(db.String(80),unique = True,nullable = False)
	def __init__(self,k,v):
		self.key = k
		self.val = v
	def __repr__(self):
		return '<User %r>' % self.key


@app.route('/')
def index():
    return 'Index Page'

@app.route('/show')
def show():
	users = User.query.all()
	out = ''
	for u in users:
		out += u.key + '' + u.val + '<br>'
	return out
	
@app.route('/request',methods=['GET' ,'POST'])
def processreq():
	if request.method == 'GET':
		return "Get key: %s,val: %s" % (request.args.get('key'),request.args.get('val'))
	else:
		return "Post key: %s,val: %s" % (request.form['key'],request.form['val'])

@app.route('/postpage/')
@app.route('/postpage/<pname>')
def postpage(pname = "No_name"):
	return render_template('postform.html',name = pname)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = true)
    
