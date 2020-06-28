from apps.handler.base_handler import BaseHandler
from apps.services.commands_services import CommandsService


command_service = CommandsService()


class CommandsListHandler(BaseHandler):
    def get(self):
        res = command_service.get_commands_list()
        return self.success(data=res)
