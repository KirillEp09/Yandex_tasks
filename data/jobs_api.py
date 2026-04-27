import flask
from . import db_session
from .jobs import Jobs
from flask import jsonify, make_response, request

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


# Получение всех работ
@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'id', 'user.name'))
                 for item in jobs]
        }
    )


# Получение одной работы
@blueprint.route('/api/jobs/<int:id>', methods=['GET'])
def get_job(id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, id)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'job', 'id', 'user.name'))
        }
    )


# Добавление работы
@blueprint.route('/api/jobs/<int:id>', methods=['POST'])
def create_job(id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        id=id,
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'title_job': job.job})


# Удаление работы
@blueprint.route('/api/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})

# Изменение работ
@blueprint.route('/api/jobs/<int:id>', methods=['PUT'])
def change_job(id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(id)
    jobs.job = request.json['job']
    jobs.team_leader = request.json['team_leader']
    jobs.work_size = request.json['work_size']
    jobs.collaborators = request.json['collaborators']
    jobs.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'success': 'OK'})
