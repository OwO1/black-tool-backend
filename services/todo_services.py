from services.base_service import BaseService
from models import Commands


class TodoService(BaseService):
    def __init__(self):
        super().__init__()
        self.model_cls = Commands
