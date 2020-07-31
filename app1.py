from flask import Flask, request, render_template, \
    jsonify, redirect, url_for, request
from tools import gen_secret


app = Flask(__name__)


@app.route('/get_data')
def get_data():
    goods_info = {"name": "Alice", "age": 30}
    # return jsonify(goods_info)
    url = url_for("get_data_v1")
    return redirect(url)
    


@app.route("/v2/get_data")
def get_data_v1():
    return "新的接口"


@app.route("/post/<post_id>")
def get_post(post_id):
    return post_id

@app.route("/index")
def index():
    return "Hello Flask!"


@app.route("/")
def homepage():
    return render_template('homepage.html')



@app.route("/register")
def register():
    return render_template("register.html")


@app.route('/deal_register', methods=["POST"])
def deal_register():
    name = request.form.get("name")
    passwd = request.form.get("passwd")
    passwd = gen_secret(passwd)
    return name + ":" + passwd



if __name__ == "__main__":
    app.run(debug=True)
