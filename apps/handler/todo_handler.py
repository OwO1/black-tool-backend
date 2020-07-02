from apps.handler.base_handler import BaseHandler
from apps.services.todo_services import TodoService

todo_service = TodoService()


class ToDoListHandler(BaseHandler):
    def get(self):
        todo_type = self.req_form.get('todoType', 1)
        data = todo_service.get_list(todo_type)
        return self.success(data=data)


class ToDoCreateHandler(BaseHandler):
    def post(self):
        todo = self.req_form['todo']
        todo_type = self.req_form['type']
        note = self.req_form['todoNote']
        todo_service.create_todo(todo, note, todo_type)
        return self.success(data={})


class ToDoUpdateHandler(BaseHandler):
    def post(self):
        id = self.req_form['id']
        todo = self.req_form['todo']
        todo_type = self.req_form['type']
        note = self.req_form['note']
        status = self.req_form['status']
        todo_service.update_todo(id, todo, note, status, todo_type)
        return self.success(data={})


class ToDoDeleteHandler(BaseHandler):
    def post(self):
        data_id = self.req_form['id']
        todo_service.delete_todo(data_id)
        return self.success(data={})
