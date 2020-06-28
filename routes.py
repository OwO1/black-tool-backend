from flask import Blueprint
from apps.handler.todo_handler import ToDoListHandler
from apps.handler.commands_handler import CommandsListHandler

# bp_commands = Blueprint('commands', __name__, url_prefix='/api/commands/')
# bp_commands.add_url_rule('list/', view_func=ToDoListHandler.as_view('commands_list'))

bp_todo = Blueprint('todo', __name__, url_prefix='/api/todo/')
bp_todo.add_url_rule('list/', view_func=CommandsListHandler.as_view('todo_list'))

bp_list = [
    # bp_commands,
    bp_todo,
]
