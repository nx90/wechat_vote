# coding: utf-8
from wxpy import *
import os
import sys
import input_params
import project_config
from cluster_type import cluster

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)



def main():
    """
    每个集群只支持10种选择，如果想重新开始一个集群的选课，需要进project_config.FILE_PATH目录，
    删除里面对应集群的文件
    """
    bot = Bot(cache_path=True)
    print bot.groups().search()
    #embed()

    bot.file_helper.send('Hello World!')

    file_path = project_config.FILE_PATH
    cluster_nums = input_params.input_cluster_nums()

    for i in range(cluster_nums):
        cluster_name = 'cluster' + str(i)
        if os.path.exists(file_path):
            if os.path.exists(file_path + cluster_name + '.yaml'):
                config_file = cluster_name
            else:
                config_file = None
            cluster(bot, cluster_name, config_file)
        else:
            os.mkdir(file_path)
            cluster(bot, cluster_name)
    embed()

if __name__ == '__main__':
    defaultencoding = 'utf-8'
    if sys.getdefaultencoding() != defaultencoding:
        reload(sys)
        sys.setdefaultencoding(defaultencoding)
    main()