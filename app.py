from flask import Flask, render_template, request, url_for, redirect
from controllers.member_controller import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ECrrSOfhX1'

# Homepage and the member list page
@app.route("/")
def index():
    return render_template('members/index.html', members=get_members())

#Member detail page
@app.route('/member/<int:member_id>')
def member(member_id):
    member = get_member(member_id)
    return render_template('members/member.html', member=member)

#Form to create a new team member
@app.route('/create', methods=('GET', 'POST'))
def create():
    return create_member(request)

#Edit a member
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    return edit_member(id, request)

#Delete a member
@app.route('/<int:member_id>/delete', methods=('POST',))
def delete(member_id):
    delete_member(member_id)
    return redirect(url_for('index'))

#Display about page
@app.route("/about")
def about():
    return render_template('about.html')

