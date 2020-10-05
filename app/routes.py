from flask import current_app as app, jsonify

from app.contoller import get_tutors, get_subjects as subjects

config = app.config['config']
logger = config.get_logger()


@app.route('/')
def get_mentors_root():
    logger.info('GET /')
    return jsonify(get_tutors())


@app.route('/subjects')
def get_subjects():
    logger.info('GET /subjects')
    return jsonify(subjects())
