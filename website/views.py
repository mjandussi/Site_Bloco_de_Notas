from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note1,Note2
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note1 = request.form.get('note1')
        note2 = request.form.get('note2')

        if note1:  # Verifica se a nota para o lado 1 foi preenchida
            new_note1 = Note1(data=note1, user_id=current_user.id)
            db.session.add(new_note1)

        if note2:  # Verifica se a nota para o lado 2 foi preenchida
            new_note2 = Note2(data=note2, user_id=current_user.id)
            db.session.add(new_note2)

        db.session.commit()
        flash('Note added!', category='success')

    return render_template("home.html", user=current_user)



@views.route('/delete-note1', methods=['POST'])
def delete_note1():
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note1.query.get(noteId)
    if note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
    return jsonify({})

@views.route('/delete-note2', methods=['POST'])
def delete_note2():
    note = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note2.query.get(noteId)
    if note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
    return jsonify({})