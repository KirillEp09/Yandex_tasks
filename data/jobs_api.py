import flask
from . import db_session
from .jobs import Jobs
from flask import jsonify, make_response, request

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


# Получение одной работы
@blueprint.route('/api/jobs/<int:id>', methods=['GET'])
def get_jobs(id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, id)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'job', 'id', 'work_size'))
        }
    )


# Добавление работы
@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'collaborators', 'id', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        creator=request.json['creator'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        id=request.json['id'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'title_job': job.job})


# Удаление работы
@blueprint.route('/api/jobs/<int:id>', methods=['DELETE'])
def delete_news(id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
