
from configparser import ConfigParser


class IniLoader(object):
    """加载 ini 文件中的配置信息"""

    def __init__(self, file):
        self.file = file
        self.parser = ConfigParser()

    def get(self, section=None, key=None):
        self.parser.read(self.file, encoding="utf-8")
        try:
            if not section:
                # 返回所有的分类的名称
                return self.parser.sections()
            if not key:
                # 返回所有的item的名称
                return self.parser.options(section)
            if section and key:
                # 返回具体的需要的配置信息
                return self.parser.get(section, key)
        except Exception:
            # 参数有误
            return None


    def add(self, section=None, key=None, value=None):
        """新增配置，直接写入配置文件"""
        if section not in self.get():
            self.parser.add_section(section)
        self.parser.set(section, key, value)
        self.parser.write(open(self.file, 'w'))
