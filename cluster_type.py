# coding: utf-8
import yaml_handler
import project_config
class cluster():
    def __init__(self, bot, cluster_name, config_file = None):
        """
        :param bot: 负责该集群的微信机器人
        :param config_file: 集群的yaml文件
        该函数中，如果存在对应的yaml文件，则不初始化yaml，如果没有，就初始化
        """
        self.name = cluster_name
        self.config_file = config_file
        self.bot = bot
        if not config_file:
            yaml_handler.yaml_init(self.bot, self.name, project_config.FILE_PATH)
        file_data = yaml_handler.read_existing_datas(self.name)
        self.wx_groups = file_data['wx_groups']
        self.count_each_type = file_data['count']
        self.members_each_type = file_data['members']
        self.capacity_each_type = file_data['capacity']
        self.voters = file_data['voters']
        self.types = {'count': self.count_each_type, 'members': self.members_each_type, 'capacity': self.capacity_each_type}
        self._cluster_regist()

    def _cluster_regist(self):
        self.bot.groups().search()
        groups = []
        for i in self.wx_groups:
            groups.append(self.bot.groups().search(i)[0])

        @self.bot.register(chats=groups, except_self=False)
        def reply_my_friend(msg):
            if msg.text[:2] == '##':
                try:
                    choose = int(msg.text[2])
                    if choose < len(self.count_each_type):
                        if msg.sender.nick_name not in self.voters:
                            if self.count_each_type[choose] < self.capacity_each_type[choose]:
                                self.members_each_type[choose].append(msg.sender.nick_name)
                                self.count_each_type[choose] += 1
                                self.voters.append(msg.sender.nick_name)
                                yaml_handler.write_datas(self.name, {'wx_groups':self.wx_groups}, self.types, {'voters':self.voters})
                                return u'已记录您的选择!\n目前选择与人数情况如下：\n' + str(self.count_each_type)
                            else:
                                return u'当前选项人数已满，请选择其他选项'
                        else:
                            return u'您已做过选择了'
                    else:
                        return u'请输入正确的选项号'
                except:
                    pass
"""
    def send_result_now(self):
        result = ''
        for i in range(len(self.count_each_type)):
            result += (u'##' + str(i) + u': ' + str(self.count_each_type) + u'\n')
        return result
"""
##Unit Testing
#from wxpy import *
#cluster(Bot(cache_path=True), 'cluster1')
#cluster(Bot(cache_path=True), 'cluster1','cluster1')
#embed()
