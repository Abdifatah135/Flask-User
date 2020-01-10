from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginnForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a133f208dfd894d11376be44fa77417a'

posts = [
    {
        'author': 'Mike Tyson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
        
    },
    {
        'author': 'Abdi Kenya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2020'
        
    }             
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   
    return render_template('about.html', titl = "About")
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acoount Created for {form.username.data}!', 'success ')
        return redirect(url_for('home'))
    return render_template('register.html', titl = "Register", form = form)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', titl = "Login", form = form)


if __name__ == '__main__':
    app.run(debug=True)