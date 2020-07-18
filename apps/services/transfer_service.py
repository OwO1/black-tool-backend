from apps.services.base_service import BaseService
from apps.transfer_utils.transfer_parser import Parser


class TransferService(BaseService):
    def __init__(self):
        super().__init__()

    def transfer(self, words):
        p = Parser(words)
        res = p.process()
        
        return res
