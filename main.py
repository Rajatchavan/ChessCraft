from flask import *
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__, static_url_path='/static',static_folder='static/')
app.config['SECRET_KEY'] = "jsjbdjndjb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

posts = [
    {
        'source': 'Nibodh Daware',
        'name': 'competetion 1',
        'info': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore .
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor ''',
        'competetion_date': '8 october 2020'
    },
    {
        'source': 'Nibodh Daware',
        'name': 'competetion 1',
        'info': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore .
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor ''',
        'competetion_date': '8 october 2020'
    }
]

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/competetions')
def Matches():
    return render_template("competetions.html", posts=posts, title='Competetions')

if __name__ == "__main__":
    app.run(debug=True)
