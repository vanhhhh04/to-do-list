#  tạo 1 module về trình duyệt home để phục vụ cho các chức năng của người dùng sử dụng blueprint
#trang web tạo chức năng của trang web đối với người dùng 
from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from . import db
import json 
from .models import Note  
views = Blueprint("views", __name__)

@views.route("/home" ,methods = ['POST','GET'])

@views.route('/',methods = ['POST','GET'])
@login_required
def home():
    if request.method == 'POST' :
        note = request.form.get("note") 
        if note :
            new_note = Note(data = note,user_id = current_user.id)
            db.session.add(new_note) 
            db.session.commit()
            flash('note added' ,category= 'success')
    return render_template("index.html",user = current_user) 

@views.route('/delete-note' , methods = ["POST"]) 
def delete_note() :
    note = json.loads(request.data)
    print(note) 
    note_id = note["note_id"]
    result = Note.query.get(note_id)
    if result : 
        if result.user_id == current_user.id : 
            db.session.delete(result)
            db.session.commit() 
    return jsonify({"code" : 200})