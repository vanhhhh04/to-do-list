# file models dùng để lưu những tập tin về database 
from flask_login import UserMixin 
# // hiểu về usermixin
# được sử dụng để cung cấp các phương thức và thuộc tính cơ bản liên quan đến người dùng trong các ứng dụng web.
# trong database
# MODELS Việc sử dụng models trong SQLAlchemy cho phép bạn định nghĩa các trường (columns) của bảng,
#  các ràng buộc (constraints), các liên kết (relationships) và các phương thức để thao tác với dữ liệu
#  trong bảng đó. Các trường (columns) của bảng được định nghĩa bởi các thuộc tính của model, với mỗi thuộc
#  tính tương ứng với một trường trong bảng

from appdemo import db    
from sqlalchemy.sql import func 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data  = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    notes = db.relationship("Note")

    def __init__(self,email,password,user_name) :
        self.email = email 
        self.password = password
        self.user_name = user_name