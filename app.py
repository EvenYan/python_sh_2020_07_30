from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, not_, func
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
db = SQLAlchemy(app)
# 创建flask脚本管理工具对象
manager = Manager(app)
# 创建数据库迁移工具对象
migrate = Migrate(app, db)
# 想manager对象注册db命令，这样命令行才能支持
manager.add_command('db', MigrateCommand)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qaz@WSX@127.0.0.1:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    passwd = db.Column(db.String(200))


class Demo(db.Model):
    __tablename__ = "Demo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


@app.route("/index")
def index():
    return "Hello Flask!"


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/insert_data")
def insert_data():
    # 添加一条数据
    # name = request.args.get("name")
    # passwd = request.args.get("passwd")
    # user1 = User(name=name, passwd=passwd)
    # db.session.add(user1)
    # db.session.commit()
    # 添加多条数据
    user1 = User(name="Merry", passwd="Merry")
    user2 = User(name="Bob", passwd='Bob')
    db.session.add_all([user1, user2])
    db.session.commit()
    return "数据添加成功！"


@app.route("/delete_data")
def delete_data():
    user = User.query.get(5)
    db.session.delete(user)
    db.session.commit()
    return "删除成功！"


@app.route("/update_data")
def update_data():
    user = User.query.get(7)
    user.name = "Tim"
    db.session.add(user)
    db.session.commit()
    return "修改成功！"


@app.route("/search_data")
def search_data():
    name1 = User.query.get(3).name
    passwd = User.query.first().passwd
    user1 = User.query.filter_by(name="Tim").first()
    user2 = db.session.query(User).first()
    print(name1, passwd, user1.name, user2.name)
    user_list = User.query.all()
    user_list1 = db.session.query(User).all()
    user_list2 = User.query.filter_by(name="Linux", passwd="root").all()
    print(user_list, user_list1, user_list2)
    user_list3 = User.query.filter(or_(User.name=="Tom", User.passwd.startswith('ro'))).all()
    print(user_list3)
    user_list4 = User.query.offset(4).limit(2).all()
    print(user_list4)
    user_list5 = User.query.order_by(User.id.desc()).all()
    print(user_list5)
    user_list6 = db.session.query(User.passwd).group_by(User.passwd).all()
    print(user_list6)
    user_list7 = db.session.query(User.passwd, func.count(User.passwd)).group_by(User.passwd).all()
    print(user_list7)
    return "查找成功"
    

@app.route("/register", methods=["GET", "POST"])
def reigister():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        user1 = User(name=name, passwd=passwd)
        db.session.add(user1)
        db.session.commit()
        return "数据添加成功！"


if __name__ == "__main__":
    manager.run()
