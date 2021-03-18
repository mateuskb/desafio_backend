import json

from flask import (
    Blueprint, request, session, url_for, Response
)
from werkzeug.security import check_password_hash, generate_password_hash

UsersBp = Blueprint('users', __name__, url_prefix='/users')

@UsersBp.route('/create', methods=['GET'])
def login():
    # resp = Request_lib.get_authorization(request, type='Basic', decode64=True)
    # credentials = resp if resp else {}
    # resp = Perfis.r_login(credentials)
    # status = 200 if resp['ok'] else 401    
    # response = app.response_class(
    #     response= json.dumps(resp),
    #     status=status,
    #     mimetype='application/json'
    # )
    response = Response(
        response= json.dumps({"ok":True}),
        status=200,
        mimetype='application/json'
    )
    # return f'{credentials}'
    return response