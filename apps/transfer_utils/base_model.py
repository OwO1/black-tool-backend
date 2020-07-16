from apps.utils.named_util import NamedTransfer


class BaseModel:
    def __init__(self, key, value, field_type, meta_type):
        self.key = key
        self.value = value
        self.field_type = field_type
        self.meta_type = meta_type

    def to_normal_dict(self):
        return {
            self.key: str(self.key)
        }

    def to_camel_dict(self):
        return {
            NamedTransfer.to_camel(self.key): str(self.key)
        }
