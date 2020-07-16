from apps.services.base_service import BaseService
from apps.transfer_utils.transfer_parser import Parser

class TransferService(BaseService):
    def __init__(self):
        super().__init__()

    def transfer(self):
        """
        1.接受的参数
        model的数据
        变量=变量
        普通字典

        增加驼峰和下划线的转换 日后加

        2.输出
        输出成字典格式

        3.完成步骤
        4.
        5.
        6.
        """
        words = """
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
        p = Parser(words)
        r = p.process()
        print('1'*30)
