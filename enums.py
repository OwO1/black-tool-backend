from enum import Enum, unique


@unique
class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        """
        判断枚举类型是否包含枚举值 value
        :param value: 枚举值
        :return: True or False
        """
        return any(value == item.value for item in cls)

    @classmethod
    def value_list(cls):
        """
        值列表
        :return: tuple
        """
        return [item.value for item in cls]

    @classmethod
    def parse_value(cls, value):
        """
        值转换为枚举
        :param value: 值
        :return: enum
        """
        for item in cls:
            if value == item.value:
                return item
        return None


class TodoStatusEnum(BaseEnum):
    """todo状态枚举"""
    # 未完成
    UNFINISHED = 0
    # 完成
    FINISHED = 1


class TodoTypeEnum(BaseEnum):
    """todo类型枚举"""
    # 今日代办
    TODAY = 0
    # 日后代办
    AFTER = 1

class DeletedStatusEnum(BaseEnum):
    DELETED = 0
    EXIST = 1

class FieldTypeEnum(BaseEnum):
    INT = 1
    STRING = 1
    DATE = 1