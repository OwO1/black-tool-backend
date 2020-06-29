from flask import Blueprint
from apps.handler.todo_handler import *
from apps.handler.commands_handler import CommandsListHandler

# bp_commands = Blueprint('commands', __name__, url_prefix='/api/commands/')
# bp_commands.add_url_rule('list/', view_func=ToDoListHandler.as_view('commands_list'))

bp_todo = Blueprint('todo', __name__, url_prefix='/api/todo/')
bp_todo.add_url_rule('list/', view_func=ToDoListHandler.as_view('todo_list'))
bp_todo.add_url_rule('create/', view_func=ToDoCreateHandler.as_view('todo_create'))
bp_todo.add_url_rule('update/', view_func=ToDoUpdateHandler.as_view('todo_update'))
bp_todo.add_url_rule('delete/', view_func=ToDoDeleteHandler.as_view('todo_delete'))

bp_list = [
    # bp_commands,
    bp_todo,
]
