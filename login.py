from flask import Flask, redirect, url_for, render_template, request

designapp = Flask(__name__)


@designapp.route("/", methods=['GET'])
def index():
    return render_template('login.html')


if __name__ == '__main__':
    designapp.run(debug=True, host='0.0.0.0', port=5050)
