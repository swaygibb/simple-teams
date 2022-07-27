from database.database import *
from werkzeug.exceptions import abort
from flask import render_template, url_for, flash, redirect

#Get all members from the database
def get_members():
    conn = get_db_connection()
    members = conn.execute('SELECT * FROM members').fetchall()
    conn.close()
    return members

#Get member by id
def get_member(member_id):
    conn = get_db_connection()
    member = conn.execute('SELECT * FROM members WHERE id = ?', (member_id,)).fetchone()
    conn.close()
    if member is None:
        abort(404)
    return member

#Create member if we can, otherwise send back an error
def create_member(request):
    if request.method == 'POST':
        fullname = request.form['fullname']
        bio = request.form['bio']

        if not fullname:
            flash('Full Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO members (fullname, bio) VALUES (?, ?)', (fullname, bio))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('members/create.html')

#Edit member if we can, otherwise send back error
def edit_member(member_id, request):
    member = get_member(member_id)

    if request.method == 'POST':
        fullname = request.form['fullname']
        bio = request.form['bio']

        if not fullname:
            flash('Fullname is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE members SET fullname = ?, bio = ?'
                         ' WHERE id = ?', (fullname, bio, member_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('members/edit.html', member=member)

#Delete member record
def delete_member(member_id):
    member = get_member(member_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(member['fullname']))