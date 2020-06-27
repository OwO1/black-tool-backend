from sqlalchemy.orm import Query

from app import db


class BaseService(object):

    def __init__(self):
        self.model_cls = None

    @property
    def session(self):
        session = db.session
        return session


    def add(self, instance):
        session = self.session
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance

    def update(self, instance):
        session = self.session
        instance = session.merge(instance)
        session.commit()
        session.refresh(instance)
        return instance
