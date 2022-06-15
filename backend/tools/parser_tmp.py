# -*- coding: utf-8 -*-
"""
临时(暂定)

"""
import re
import os
import logging
from ttp import ttp
from textfsm import TextFSM
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from netmiko._textfsm import _clitable as clitable
from netmiko._textfsm._clitable import CliTableError
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from application.settings import BASE_DIR, MEDIA_ROOT

logger = logging.getLogger("netmiko")
template_dir = os.path.join(BASE_DIR, MEDIA_ROOT, 'textfsm_templates')
os.environ["NTC_TEMPLATES_DIR"] = template_dir


# 解析器类
class BatManFsm(object):
    # 解析器
    @staticmethod
    def clitable_to_dict(cli_table):
        """Converts TextFSM cli_table object to list of dictionaries."""
        objs = []
        for row in cli_table:
            temp_dict = {}
            for index, element in enumerate(row):
                temp_dict[cli_table.header[index].lower()] = element
            objs.append(temp_dict)
        return objs

    # 解析器主程序
    @staticmethod
    def get_structured_data(raw_output, platform, command):
        """Convert raw CLI output to structured data using TextFSM template."""
        template_dir = os.environ["NTC_TEMPLATES_DIR"]
        index_file = os.path.join(template_dir, "index")
        textfsm_obj = clitable.CliTable(index_file, template_dir)
        attrs = {"Command": command, "Platform": platform}
        try:
            # Parse output through template
            textfsm_obj.ParseCmd(raw_output, attrs)
            structured_data = BatManFsm.clitable_to_dict(textfsm_obj)
            output = raw_output if structured_data == [] else structured_data
            return output
        except CliTableError:
            return raw_output

    @staticmethod  # 解析数据
    def info_fsm(path, fsm_platform):
        if default_storage.exists(path):
            tmp = path.split('/')[-1]
            _cmd = tmp.split('.')[0]
            cmd = ' '.join(_cmd.split('_'))
            _content = default_storage.open(path).read()
            _content = _content.decode('utf-8')
            # print(cmd)
            res = BatManFsm.get_structured_data(platform=fsm_platform,
                                                command=cmd,
                                                raw_output=_content)
            return res
        else:
            raise Exception("path file not found")


def test():
    res = BatManFsm.info_fsm(path='config_files/10.254.13.11/show_interface.txt', fsm_platform='maipu')
    if isinstance(res, list):
        for i in res:
            print(i)
        print(len(res))
    else:
        print(res)
        print('没有匹配成功')


if __name__ == '__main__':
    pass
    # filename = 'config_files/10.254.13.11/test.txt'
    # path = default_storage.save(filename, ContentFile('112233344'))
    # print(path)
    # from backend.tools.parser_tmp import test
    # test()
