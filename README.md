<div align=center><h1>加速Github访问</h1></div>
<div align=center><p style='font-size:15px'>走出心理阴影(皮)</p></div>

## 原理

通过向提供Web请求的DNS服务器请求针对本地最优的DNS解析数据,把输出数据存入hosts文件，提高本地访问速度

## 使用

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

地址列表
1. 可能存在多组地址
2. 不同地区的不同时间，获取的高速地址可能不同]

# 补充的代替方案
> 使用镜像站点clone或代理下载服务

## 前置声明
1. 收录此处的地址仅为我所使用过的，连接稳定性由提供方保证，与本项目无关。
2. 收录的站点的服务政策不一，可能会收集使用者的信息，如果您不希望被收集信息，请提前查看相关镜像渠道的相关条款。
     + （but: clone github上的仓库不是依然会被收集信息吗 :D ）
3. 请尽量不要在修改任何下载自镜像站的仓库后直接push，存在使账号密码泄露的风险。
4. 如果发现镜像站地址已经失效，在条件允许的情况下，可以在Issues告知我，我在看到信息后会立即撤除相关地址。

+ 带下
     + https://gh.api.99988866.xyz/
+ 镜像（可以clone）
     + https://hub.fastgit.xyz/
     + https://mirror.ghproxy.com/

+ GitHub缓存加速网站
     + https://www.gitclone.com/
     ```
     方法一（替换URL）
     git clone https://gitclone.com/github.com/tendermint/tendermint.git
     方法二（设置git参数）
     git config --global url."https://gitclone.com/".insteadOf https://
     git clone https://github.com/tendermint/tendermint.git
     方法三（使用cgit客户端）
     cgit clone https://github.com/tendermint/tendermint.git
     ```
+ GitCode 《Github 加速计划》
     + https://gitcode.net/mirrors/
     
     > 《Github 加速计划》通过 mirror 镜像仓库来同步 github 上的开源项目
     
     ```
     使用：
     git clone https://gitcode.net/mirrors/用户名/仓库
     ```
     
任意一种镜像只解决下载问题，上传的话需要查看.git文件夹的config检查上传仓库的地址，同时期待自己网速够好。

