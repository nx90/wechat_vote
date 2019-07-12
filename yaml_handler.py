# coding: utf-8
import yaml
import input_params
import project_config

def yaml_init(bot, cluster_name, yaml_path = project_config.FILE_PATH):
    """

    :param bot: 微信机器人
    :param cluster_name: 多微信群组成的一个组
    :param yaml_path: 持久化存储文件路径
    :return:
    第一次发起投票时会初始化做存储用的yaml文件
    """
    wx_groups = {'wx_groups': input_params.input_vote_group(bot, cluster_name)}
    types_num = input_params.input_types_num(cluster_name)
    types_capacity_tmp = input_params.input_types_capacity(cluster_name, types_num)
    types_and_nums = {}
    types_and_members = {}
    types_and_capacity = {}
    voters = {'voters':[]}


    for i in range(types_num):
        types_and_nums[i] = 0
        types_and_members[i] = []
        types_and_capacity[i] = types_capacity_tmp[i]

    types = {'count': types_and_nums, 'members': types_and_members, 'capacity': types_and_capacity}
    write_datas(cluster_name, wx_groups, types, voters, yaml_path)

def read_existing_datas(cluster_name, yaml_path = project_config.FILE_PATH):
    with open(yaml_path + unicode(cluster_name) + '.yaml','r') as data_file:
        data = yaml.load(data_file)
    return data

def write_datas(cluster_name, wx_groups, types, voters, yaml_path = project_config.FILE_PATH):
    with open(yaml_path + unicode(cluster_name) + '.yaml', 'w') as data_file:
        yaml.dump(wx_groups, data_file)
        yaml.dump(types, data_file)
        yaml.dump(voters, data_file)


##Unit Testing
#from wxpy import *
#yaml_init(bot = Bot(cache_path=True), cluster_name = '尖子1')
#read_existing_datas(cluster_name = '尖子1')