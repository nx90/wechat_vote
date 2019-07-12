# wechat_vote
可将多微信群抽象为一个集群，并以集群为单位发起投票

该项目使用Python2.7开发，利用wxpy库完成微信端消息的接收，使用yaml文件做轻量的持久化存储，wxpy项目github地址:

> https://github.com/youfou/wxpy

运行main文件来发起投票，发起投票不会自动发送微信群通知，所以需要手动通知群成员投票已开始，这个特性以后可以加一下
```
python main.py
```

若共有M种投票选项，则在投票范围内的微信群成员可输入##n(即以双井号为前缀，n为[0,M)之间的整数)进行投票，若投票记录成功则会自动发送记录成功提醒，若记录失败则不会发送任何提醒，若n为除[0,M)间整数外的非法输入，则会自动发送失败提示
