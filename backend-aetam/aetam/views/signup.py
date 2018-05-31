from flask.views import MethodView
from flask import request
from flask import session
from flask import Response
from flask import json
from flask import g
from aetam import app
from aetam.models import User
from aetam.models import Status

class SignUpView(MethodView):
    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            data = {"errors": []}
            if request.json['username'] == "":
                data['errors'].append('Invalid username')
            if request.json['password'] == "":
                data['errors'].append('Invalid password')

            if data['errors'] == []:
                user_id = self.insert_user(request.json['username'], request.json['password'])
                data['status'] = Status.select_from(g.db, user_id)
                data['user'] = User.select_from(g.db, user_id)
                return Response(
                    status=200,
                    response=json.dumps(data),
                    mimetype='application/json'
                )
            return Response(
                status=400,
                response=json.dumps(data),
                mimetype='application/json'
            )

    def insert_user(self, username, password):
        pass_sha = self.SHA256_pass(password)
        user_id = User(username, pass_sha).insert_to(g.db)
        Status(user_id, "charname", 0, 0, 0, 0, 0).insert_to(g.db)
        return user_id

    # TODO: sha256
    def SHA256_pass(self, password):
        secret_key = app.config['SECRET_KEY']
        return password
