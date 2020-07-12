class BaseModel:
    def __init__(self, key, value, field_type, meta_type):
        self.key = key
        self.value = value
        self.field_type = field_type
        self.meta_type = meta_type
