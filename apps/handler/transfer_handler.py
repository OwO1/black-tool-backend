from apps.handler.base_handler import BaseHandler
from apps.services.transfer_service import TransferService

transfer_service = TransferService()


class TransferHandler(BaseHandler):
    def get(self):
        transfer_service.transfer()
        # todo_type = self.req_form.get('todoType', 1)
        # data = todo_service.get_list(todo_type)
        return self.success(data=None)
