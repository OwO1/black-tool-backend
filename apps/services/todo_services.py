from apps.services.base_service import BaseService
from apps.db.models import Todo
from enums import TodoStatusEnum, TodoTypeEnum, DeletedStatusEnum


class TodoService(BaseService):
    """
    1.创建
    2.完成
    3.转换类型
    4.删除
    5.获得
    """

    def __init__(self):
        super().__init__()
        self.model_cls = Todo

    def create_todo(self, todo, note, todo_type):
        todo_dict = {
            "todo": todo,
            "note": note,
            "todo_type": todo_type,
        }
        todo = self.model_cls(**todo_dict)
        self.add(todo)

    def update_todo(self, id, todo, note, status, todo_type):
        todo_item = self._get(id)
        todo_item.todo = todo
        todo_item.note = note
        todo_item.status = status
        todo_item.todo_type = todo_type
        self.update(todo_item)

    def get_list(self, todo_type):
        query_dict = {
            "todo_type": todo_type,
            "deleted": DeletedStatusEnum.EXIST.value,
            "status": TodoStatusEnum.UNFINISHED.value,
        }
        todos = self.session.query(self.model_cls).filter_by(**query_dict).all()
        todo_list = []
        for t in todos:
            todo_list.append({
                "id": t.id,
                "todo": t.todo,
                "note": t.note,
                "status": t.status,
                "type": t.todo_type,
                "deleted": t.deleted,
            })
        return todo_list

    def delete_todo(self, id):
        todo = self._get(id)
        todo.deleted = DeletedStatusEnum.DELETED.value
        self.update(todo)

    def _get(self, id):
        query_dict = {
            'id': id,
        }
        todo = self.session.query(self.model_cls).filter_by(**query_dict).first()
        return todo
