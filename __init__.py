# khởi tạo các thư viện và các đối tượng module trong blueprint sẵn sàng để chạy app.py và thêm nữa là lấy các 
# thông tin được bảo mật trong file env
from flask import Flask
import os 
# thư viện os là thư viện dùng để tương tác với hệ thống tệp và môi trường 
from dotenv import load_dotenv
# thư viện dotenv dùng để đọc các biến từ tệp tin env 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
# thư viện loginmanager được nhập và khởi tạo để sử dụng thư viện flask-login

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
DB_NAME = os.environ.get("DB_NAME")
#  3 dòng lệnh trên để lấy dữ liệu từ file .env 
db = SQLAlchemy() 
 #  tạo đối tượng SQLALchemy để tương tác với cơ sở dữ liệu thông qua biến db 
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:vanhkhongphe@localhost/vanh'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    # cũng là 1 câu lệnh khởi tạo đối tượng db như câu lệnh db=sqlalchemy(app) nhưng ở đây init_app cho phép khởi 
    # tạo 2 đối tượng db và app ở những vị trí khác nhau còn lệnh db=sqlalchemy(app) buộc 2 lệnh db =SQLALchemy(app)
    # phải đi liền với nhau 
    from .models import Note,User 
    # lệnh trên để nhập 2 bảng note và user vào quá trình khởi tạo 
    # db = SQLAlchemy(app)
    from appdemo.user import user
    from appdemo.views import views

  
    
    
    # with app.app_context():
    #     db.create_all()
    # lệnh để tạo bảng 
    
    from appdemo.user import user 
    from appdemo.views import views
    app.register_blueprint(user)
    app.register_blueprint(views)
    # 2 lệnh đănng kí blue print vừa tạo vào app 

    login_manager = LoginManager()
    # khởi tạo đối tượng LoginManager để sử dụng flask-login
    login_manager.login_view='user.login'
    login_manager.init_app(app)

    @login_manager.user_loader 
    def load_user(id) :
        return User.query.get(int(id))
    # thiết lập trang đăng nhập mặc định cho ứng dụng
    #'user.login' là tên của route (đường dẫn) mà Flask Login
    # sẽ chuyển hướng đến nếu người dùng cần phải đăng nhập để truy cập vào một trang cụ thể.
    # Nếu người dùng chưa đăng nhập, Flask Login sẽ tự động chuyển hướng họ đến trang đăng nhập này. 

    return app 
# đây là hàm khởi tạo chính để file app.py  