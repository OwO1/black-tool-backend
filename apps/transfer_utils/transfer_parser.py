import json
from apps.transfer_utils.base_model import BaseModel
from enums import FieldTypeEnum


class Parser():
    def __init__(self, words):
        self.words = words

    def process(self):
        words = self._prepare(self.words)
        lines = self._split_line(words)
        parser_list = []
        for l in lines:
            key, value, field_type, meta_type = self._split_word(l)
            bm = BaseModel(key, value, field_type, meta_type)
            parser_list.append(bm)
        res = self._combine(parser_list)
        return res

    def _combine(self, parser_list):
        res = {}
        for n in parser_list:
            tmp = n.to_camel_dict()
            res.update(tmp)
        res_str = json.dumps(res, indent=2)
        return res_str

    def _prepare(self, words):
        return self._remove_space(words)

    def _split_line(self, words):
        """
        根据换行符,把句子断开
        """
        lines = []
        line_list = words.split('\n')
        for line in line_list:
            lines.append(self._remove_space(line))
        return lines

    def _split_word(self, line):
        """
        根据 "=" 将关键信息提取出来
        """
        split_word = line.split("=", 1)
        key = split_word[0].strip()
        value = split_word[1].strip()
        field_type = self._get_line_type(line)
        meta_type = ''
        return key, value, field_type, meta_type

    def _remove_space(self, words):
        return words.strip()

    def _get_line_type(self, line):
        """
        目前的判断方法比较粗糙,以后写成一个类来做这件事
        """
        if 'int' in line:
            return FieldTypeEnum.INT
        elif 'string' in line:
            return FieldTypeEnum.STRING
        else:
            return FieldTypeEnum.STRING


"""
    project = models.ForeignKey(Project, verbose_name='项目', null=True, default="")
    visit_name = models.CharField(max_length=50, verbose_name="EDC访视名称", default="")
    visit_num = models.CharField(max_length=100, verbose_name="EDC访视编号", default="")
    status = models.IntegerField(verbose_name="状态", default=1)  # 0:已删除 1：已填加，未上线 2：已上线
    index = models.CharField(max_length=50, verbose_name="序号", default="")  # 自动生成T001
    creator = models.CharField(max_length=50, verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    reviser = models.CharField(max_length=50, verbose_name="修改人", default="")
    revise_time = models.DateTimeField(auto_now=True, verbose_name="修改时间", )
    duration = models.IntegerField(null=True, blank=True, verbose_name='访视持续天数', default=0)
    float_left = models.IntegerField(null=True, blank=True, verbose_name='访视前浮动天数', default=0)
    float_right = models.IntegerField(null=True, blank=True, verbose_name='访视后浮动天数', default=0)
"""
