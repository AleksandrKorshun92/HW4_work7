from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from model_registr import db, Polzovotel, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db_registr.db"
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

db.init_app(app)

@app.route("/")
def index():
    return render_template('hello.html')


@app.route('/start/', methods=['GET', 'POST'])
def register():
    db.create_all()
    form = RegistrationForm()
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        secret_password = generate_password_hash(password)

        polzovatels = Polzovotel(first_name=f'{first_name}', last_name=f'{last_name}', email=f'{email}',
                                 password=f'{secret_password}')
        db.session.add(polzovatels)
        db.session.commit()
        return redirect('/registered')

    return render_template('registracio.html', form=form)

@app.route('/registered/')
def registered():
    polzovatels=Polzovotel.query.first()
    contex = {"polzovatels": polzovatels}
    return render_template('finish.html', **contex)


if __name__ == '__main__':
    app.run(debug=True)
