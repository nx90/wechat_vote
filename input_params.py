# coding: utf-8
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def input_cluster_nums(cluster_nums=None):
    while not cluster_nums:
        print("请输入班级类型数:")
        cluster_nums = sys.stdin.readline()
        try:
            cluster_nums = int(cluster_nums)
            if cluster_nums > 0:
                print("班级类型数记录成功!")
                break
            else:
                cluster_nums = None
                print("请输入一个正整数")
        except:
            cluster_nums = None
            print("请输入一个正整数")
    return cluster_nums


def input_vote_group(bot, cluster_name):
    """

    :param bot: 负责该集群的微信机器人
    :param cluster_name: 集群名称
    :return: 一个列表，每项为每个该集群下的微信群名
    """
    vote_group = []
    while True:
        print("请输入属于集群[" + cluster_name + "]的微信群名\n（输入一个群名后按回车，再输第二个群名，若无微信群需要继续添加则输入N）：")
        GROUP_NAME = sys.stdin.readline()
        if GROUP_NAME[:-1] == 'N' or GROUP_NAME[:-1] == 'n':
            print("记录的属于集群[" + unicode(cluster_name)+ "]的微信群如下：")
            print(vote_group)
            break
        print "所有微信群名如下："
        print bot.groups().search()
        searched_vote_group = bot.groups().search(unicode(GROUP_NAME))
        match_list_length = len(searched_vote_group)
        if match_list_length == 0:
            print("没有查询到群名称为：[" + GROUP_NAME[:-1] + "]的群，请重新输入正确的群名")
        elif match_list_length > 1:
            print("查询到多个符合要求的群：\n")
            print(searched_vote_group)
            #for i in searched_vote_group:
            #    print(i)
            while True:
                print("请输入您想选择的群的序号：")
                tmp = sys.stdin.readline()
                try:
                    tmp = int(tmp)
                    if tmp < len(searched_vote_group):
                        GROUP_NAME = str(searched_vote_group[tmp])
                        break
                    else:
                        print("请输入正确的序号，第一个用0表示")
                        continue
                except:
                    print("请输入正整数")
                #GROUP_NAME = str(searched_vote_group[])
            vote_group.append(unicode(GROUP_NAME[7:-1]))
            print("投票群记录成功！群名称为：" + GROUP_NAME[7:-1])
        else:
            vote_group.append(unicode(GROUP_NAME[:-1]))
            print("投票群记录成功！群名称为：" + GROUP_NAME[:-1])
    return vote_group


def input_types_num(cluster_name, vote_type_nums=0):
    while not vote_type_nums:
        print("请输入集群[" + cluster_name + "]的投票种类总数：")
        vote_type_nums = sys.stdin.readline()
        try:
            vote_type_nums = int(vote_type_nums)
            if vote_type_nums > 0:
                print("集群[" + cluster_name + "]投票种类数已记录，种类数为：" + str(vote_type_nums))
            else:
                vote_type_nums = 0
                print("请重新输入合理的种类数!")
        except:
            vote_type_nums = 0
            print("请输入一个正整数作为投票种类数")
    return vote_type_nums

def input_types_capacity(cluster_name, types_num):
    vote_type_capacity = []
    for i in range(types_num):
        tmp = 0
        while not tmp:
            print ("请输入集群[" + cluster_name + "]，第" + str(i) + "种选择的人数上限：")
            tmp = sys.stdin.readline()
            try:
                tmp = int(tmp)
                if tmp > 0:
                    vote_type_capacity.append(tmp)
                    print("集群[" + cluster_name + "]，第" + str(i) + "种选择的人数上限已记录，上限为：" + str(tmp))
                else:
                    tmp = 0
                    print("请重新输入合理的人数上限!")
            except:
                tmp = 0
                print("请输入一个正整数作为人数上限")
    return vote_type_capacity
