from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/admin/", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            username, password = str(request.form['username']), str(request.form['password'])
            return "<div>You are logged in!</div>"

    return render_template('login.html')


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

