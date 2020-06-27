from flask import Blueprint

bp_project = Blueprint('project', __name__, url_prefix='/api/project/')
bp_project.add_url_rule('list/', view_func=ProjectListHandler.as_view('project_list'))

bp_list = [
    bp_project,
]
