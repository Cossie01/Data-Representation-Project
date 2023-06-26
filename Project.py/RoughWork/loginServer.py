from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'someSecretKey'

def validate_credentials(email, password):
    if email == 'example@example.com' and password == 'password':
        return True
    else:
        return False

@app.route('/loginPage', methods=['GET', 'POST'])
def loginPage():
    session.clear()  

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if validate_credentials(email, password):
            session['username'] = email  
            return redirect(url_for('vote'))
        else:
            error_message = "Invalid credentials. Please try again."
            return render_template('loginPage.html', error=error_message)

    return render_template('loginPage.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('loginPage'))


@app.route('/vote')
def vote():
    if 'username' not in session:
        return redirect(url_for('loginPage'))

    return render_template('vote.html')


if __name__ == '__main__':
    app.run(debug=True)

