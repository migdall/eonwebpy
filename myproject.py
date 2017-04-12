from flask import Flask, request
app = Flask(__name__)


@app.route("/admin/", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            username, password = str(request.form['username']), str(request.form['password'])
            return "<div>You are logged in!</div>"

    return "<div>Welcome to admin</div>"


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

