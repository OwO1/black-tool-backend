from apps.services.base_service import BaseService
from apps.db.models import Commands


class CommandsService:
    def __init__(self):
        super().__init__()
        self.model_cls = Commands

    def get_commands_list(self):
        commands = Commands.query.all()
        command_list = []
        for c in commands:
            command_list.append({
                'about': c.about,
                'command': c.command,
                'introduce': c.introduce,
            })
        return command_list
