from flask import Flask
from flask_restful import Api
import users_resource
import jobs_resource
from data import db_session

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    api.add_resource(jobs_resource.JobListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobResource, '/api/v2/jobs/<int:job_id>')
    api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(users_resource.UserResource, '/api/v2/users/<int:user_id>')
    app.run()