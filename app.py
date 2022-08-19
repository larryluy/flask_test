from initdb import db, app, User
from flask import render_template, redirect, request

@app.route('/')
def find_all_users():
    users = User.query.all()
    print(users)
    return render_template("list.html", users=users)

@app.route('/get/<int:get_id>')
def get_by_id(get_id):
    get_user = User.query.get(get_id)
    return '编号: {0}, 用户名: {1}, 邮箱: {2}'.format(get_user.id, get_user.username, get_user.email)

@app.route('/add', methods=['POST'])
def add_user():
    new_user = User()
    username = request.form.get('username')
    new_user.username = username
    new_user.email = username + "@163.com"
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:del_id>')
def delete_by_id(del_id):
    del_user = User.query.filter_by(id=del_id).first()
    if del_user:
        db.session.delete(del_user)
        db.session.commit()
    return redirect('/')

@app.route('/update', methods=['POST', 'GET'])
def update_user():
    if request.method == 'POST':
        update_id = request.form['id']
        update_user = User.query.get(int(update_id))
        update_user.username = request.form['username']
        update_user.email = request.form['email']
        db.session.commit()
        return redirect('/')
    else:
        update_id = request.args.get('id')
        user = User.query.get(update_id)
        return render_template('update.html', user_id=update_id, user=user)

if __name__=='__main__':
    app.run(debug=True)