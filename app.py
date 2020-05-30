from flask import Flask, render_template, url_for, flash

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '468c710afb86dcbc10f7c3db1aa394f3'
posts = [
    {
        'author': 'Shiwangi Garg',
        'title': 'Blog Post',
        'content': 'First blog post',
        'date_posted': 'May 30, 2020'
    },
    {
        'author': 'Shiwangi Garg',
        'title': 'Blog Post',
        'content': 'First blog post',
        'date_posted': 'May 30, 2020'
    },
    {
        'author': 'Shiwangi Garg',
        'title': 'Blog Post',
        'content': 'First blog post',
        'date_posted': 'May 30, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}')
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
