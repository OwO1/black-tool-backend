from tool.base_handler import BaseHandler


class ToDoListHandler(BaseHandler):
    def get(self):
        return self.success(data={})
