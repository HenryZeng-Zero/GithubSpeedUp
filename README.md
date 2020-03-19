Lang: [ZH-CN](README.md) ; [EN](README_en.md)
# 起因
在中国，因为网络条件的一些问题，同时因为Github没有在中国的CDN服务器，所以访问Github的速度相当的慢，不论上传下载还是访问。

# 原理

通过向提供Web请求的DNS服务器请求针对本地最优的DNS解析数据,把输出数据存入hosts文件，提高本地访问速度

# 使用

请使用Python3执行

```
python GSU.py [command]
```
查看帮助
```
python GSU.py help
```

Help文档
```
[command]:
     help         (帮助你查找帮助文档)
     add [domain] (添加待检测域名)
      └┈┈ add -y  (跳过确认部分)
     ls           (输出域名列表)
     rm [id]      (删除域名)
      └┈┈ rm -y   (跳过确认部分)
     do           (输出hosts)
     save [file]  (保存hosts)
```