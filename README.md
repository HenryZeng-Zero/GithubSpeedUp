<center style='font-size:30px'>加速Github访问</center>
<center style='font-size:15px'>走出心理阴影(皮)</center>

# 原理

通过向提供Web请求的DNS服务器请求针对本地最优的DNS解析数据,把输出数据存入hosts文件，提高本地访问速度

# 使用

请使用Python3执行

```
git clone https://github.com/zzh-blog/GithubSpeedUp.git
cd GithubSpeedUp
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
     do [id]      (输出hosts,默认是选择全部id)
     save [file]  (保存hosts)
     IPs [id]     (输出所有域名的ip,默认是选择全部id)
```