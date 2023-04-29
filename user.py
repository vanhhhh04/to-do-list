# tạo 1 module nhỏ về các chức năng của người dùng sử dung blueprint  
# và các route url dẫn link trên web
from flask import Blueprint,render_template,redirect,url_for,request,flash
from .models import User,Note
from flask_login import login_user, logout_user,login_required,current_user 
# current_user là một biến global mà bạn có thể sử dụng để truy cập thông tin
# của người dùng hiện tại đang đăng nhập vào ứng dụng của bạn
from werkzeug.security import generate_password_hash,check_password_hash
from .import db 

user =Blueprint("user" , __name__)
@user.route('/login', methods = ["POST","GET"])
def login() :
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first() 
        if user :
            if check_password_hash(user.password,password) :
                login_user(user,remember=True)
                # login_user là một hàm trong Flask-Login, một thư viện phổ biến trong Flask 
                # để xây dựng hệ thống đăng nhập và bảo mật cho ứng dụng web. Hàm này được sử
                # dụng để đăng nhập người dùng và lưu trữ thông tin đăng nhập của họ trong phiên làm việc.
                flash('login successed',category='success')
                return redirect(url_for('views.home'))
            else :
                flash('check your password again',category='error')
        else :
            flash('user does not exit',category='error')
    return render_template('login.html',user = current_user) 


@user.route('/signup',methods = ["POST","GET"])
def signup() :
    if request.method == 'POST' :
        email = request.form.get('email') 
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            flash("User existed!", category="error")
        else :
            password = generate_password_hash(password, method="sha256")
            new_user = User(email, password, user_name)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("User created!", category="success")
            except:
                "Error when create user!"
    return render_template("signup.html",user = current_user) 

@user.route('/logout')
@login_required
def logout() :
    logout_user()
    return redirect(url_for("user.login"))
    