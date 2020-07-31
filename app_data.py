from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qaz@WSX@127.0.0.1:3306/sh_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    passwd = db.Column(db.String(50))

@app.route("/insert_data")
def insert_data():
    name = "Tom"
    passwd = "1234"
    user1 = User(name=name, passwd=passwd)
    db.session.add(user1)
    db.session.commit()
    return "新建数据成功！"


@app.route("/search_data")
def search_data():
    user1 = User.query.get(2)
    user_list = User.query.filter_by(name="Tom").all()
    print(user1.name, user1.passwd)
    print(user_list)
    return "查找成功！"

if __name__ == "__main__":
    # 清除数据库中所有数据(第一次)
    # db.drop_all()
    # 创建所有的表
    # db.create_all()
    app.run(debug=True, port=5555)
