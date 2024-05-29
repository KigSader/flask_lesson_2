from flask import Flask, render_template, request, make_response, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '7442201f29c138299d0eb77efaaadd8fecc87242cbf09e5e1d16c9a68479b819'


@app.route('/')
def index():
    if 'username' in session:
        return render_template('main.html', username=session['username'], email=session['e-mail'])
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', 'NoName')
        email = request.form.get('e-mail', '<EMAIL>')
        session['username'] = username
        session['e-mail'] = email
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', username)
        response.set_cookie('e-mail', email)
        return response
    return render_template('login.html')


@app.route('/logout/', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('e-mail', None)
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('e-mail', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)