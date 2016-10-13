from flask import render_template, jsonify, request, url_for, abort, redirect
from . import problem
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from ..models import Program, Choice, Classify
=======
from ..models import Program, Choice
>>>>>>> Stashed changes
=======
from ..models import Program, Choice
>>>>>>> Stashed changes
=======
from ..models import Program, Choice
>>>>>>> Stashed changes
from flask_babel import gettext
from time import sleep


@problem.route('/')
def index():
    return render_template('problem/index.html',
                           title=gettext('Practice Platform'))


@problem.route('/program/')
def show_program():
    pro = Program.query.all()
    return render_template('problem/show_program.html',
                           title=gettext('Program Practice'),
                           problems=pro)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

@problem.route('/choice/')
def show_choice():
    cho = Choice.query.all()
    return render_template('problem/show_choice.html',
                           title=gettext('Choice Practice'),
                           choices=cho)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes

@problem.route('/choice/')
def show_choice():
    classifies = Classify.query.all()
    rows = []
    for c in classifies:
        rows.append([c.name, c.choices.count(), c.id])
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

<<<<<<< Updated upstream
    return render_template('problem/show_choice.html',
                           title=gettext('Choice Practice'),
                           rows=rows)

<<<<<<< Updated upstream
<<<<<<< Updated upstream

@problem.route('/program/<int:pid>/')
def program_view(pid):
    pro = Program.query.filter_by(id=pid).first()
    return render_template('problem/program_detail.html',
                           title=pro.title,
                           problem=pro)


@problem.route('/choice/<int:cid>/')
def choice_view(cid):
    cho = Choice.query.filter_by(id=cid).first()
    return render_template('problem/choice_detail.html',
                           title=cho.title,
                           choice=cho)

=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
@problem.route('/program/<int:pid>/')
def program_view(pid):
    pro = Program.query.filter_by(id=pid).first()
    return render_template('problem/problem_detail.html',
                           title=pro.title,
                           problem=pro)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

@problem.route('/<int:pid>/submit/', methods=['POST'])
def submit(pid):
    source_code = request.form['source_code']
    # TODO here.  Get the result.
    result = dict()
    result['problem_id'] = pid
    result['compiler'] = "Compiling... "                # Get the compiler result
    result['run'] = "Running result... "                # Get the run result

    sleep(2)
    return jsonify(**result)
