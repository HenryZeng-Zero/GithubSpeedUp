<div align=center><h1>加速Github访问</h1></div>
<div align=center><p style='font-size:15px'>走出心理阴影(皮)</p></div>


## 好方法：（因为自己的项目速度提升有限，所以给出更快的方法）
使用镜像站点clone或代理下载服务(我只是自己用的方便在这里放出来，真的没有打广告):
+ 带下
     + https://gh.api.99988866.xyz/
     + http://gitd.cc/
+ 镜像（可以clone）
     + https://github.com.cnpmjs.org/
     + https://hub.fastgit.org/  
     ```git clone [镜像]/[用户名]/[仓库名].git```
+ 镜像（不支持clone）
     + https://github.wuyanzheshui.workers.dev

+ 特殊：
     + https://www.gitclone.com/  
     我推荐第一种方法  
     ```
     方法一（替换URL）
     git clone https://gitclone.com/github.com/tendermint/tendermint.git
     方法二（设置git参数）
     git config --global url."https://gitclone.com/".insteadOf https://
     git clone https://github.com/tendermint/tendermint.git
     方法三（使用cgit客户端）
     cgit clone https://github.com/tendermint/tendermint.git
     ```
任意一种镜像只解决下载问题，上传的话需要查看.git文件夹的config检查上传仓库的地址，同时期待自己网速够好。


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





# 整理

下面是hosts整理
```
199.59.148.209 github.global.ssl.fastly.net  
31.13.81.1 github.global.ssl.fastly.net  
66.220.152.17 github.global.ssl.fastly.net  
88.191.249.182 github.global.ssl.fastly.net  
```

```
52.74.223.119 github.com
192.30.255.112 github.com
192.30.255.113 github.com
```

```
185.199.110.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.108.153 assets-cdn.github.com
```

```
185.199.109.153 documentcloud.github.com
185.199.108.153 documentcloud.github.com
185.199.110.153 documentcloud.github.com
```

```
8.7.198.45 gist.github.com
243.185.187.39 gist.github.com
203.98.7.65 gist.github.com
```

```
185.199.109.154 help.github.com
185.199.110.154 help.github.com
185.199.111.154 help.github.com
```

```
54.251.140.56 nodeload.github.com
13.229.189.0 nodeload.github.com
13.250.162.133 nodeload.github.com
```

```
151.101.24.133 raw.github.com
151.101.196.133 raw.github.com
151.101.76.133 raw.github.com
```

```
52.87.114.63 status.github.com
54.85.97.34 status.github.com
52.205.36.92 status.github.com
```

```
140.82.113.17 training.github.com
140.82.113.18 training.github.com
```

```
13.229.188.59 www.github.com
192.30.255.112 www.github.com
52.74.223.119 www.github.com
13.250.177.223 www.github.com
```

```
151.101.40.133 avatars0.githubusercontent.com
151.101.196.133 avatars0.githubusercontent.com
151.101.24.133 avatars0.githubusercontent.com
151.101.76.133 avatars0.githubusercontent.com
```

```
151.101.196.133 avatars1.githubusercontent.com
151.101.40.133 avatars1.githubusercontent.com
151.101.76.133 avatars1.githubusercontent.com
```

```
185.199.108.154 github.githubassets.com
185.199.109.154 github.githubassets.com
185.199.111.154 github.githubassets.com
```

```
52.216.207.123 github-production-release-asset-2e65be.s3.amazonaws.com
52.216.109.203 github-production-release-asset-2e65be.s3.amazonaws.com
52.216.144.131 github-production-release-asset-2e65be.s3.amazonaws.com
52.216.179.51 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.17.252 github-production-release-asset-2e65be.s3.amazonaws.com
```

```
54.169.195.247 api.github.com
13.250.168.23 api.github.com
13.250.94.254 api.github.com
```

```
151.101.40.133 user-images.githubusercontent.com
151.101.196.133 user-images.githubusercontent.com
151.101.24.133 user-images.githubusercontent.com
151.101.76.133 user-images.githubusercontent.com
```

```
151.101.40.133 raw.githubusercontent.com
151.101.24.133 raw.githubusercontent.com
151.101.76.133 raw.githubusercontent.com
```

```
151.101.196.133 gist.githubusercontent.com
151.101.24.133 gist.githubusercontent.com
151.101.40.133 gist.githubusercontent.com
151.101.76.133 gist.githubusercontent.com
```

```

151.101.40.133 cloud.githubusercontent.com
151.101.24.133 cloud.githubusercontent.com
151.101.76.133 cloud.githubusercontent.com
```

```
151.101.40.133 camo.githubusercontent.com
151.101.76.133 camo.githubusercontent.com
```

```
151.101.24.133 avatars2.githubusercontent.com
151.101.196.133 avatars2.githubusercontent.com
151.101.40.133 avatars2.githubusercontent.com
151.101.76.133 avatars2.githubusercontent.com
```

```
151.101.24.133 avatars3.githubusercontent.com
151.101.40.133 avatars3.githubusercontent.com
151.101.76.133 avatars3.githubusercontent.com
```

```
151.101.196.133 avatars4.githubusercontent.com
151.101.40.133 avatars4.githubusercontent.com
151.101.76.133 avatars4.githubusercontent.com
```

```
151.101.196.133 avatars5.githubusercontent.com
151.101.40.133 avatars5.githubusercontent.com
151.101.76.133 avatars5.githubusercontent.com
```

```
151.101.196.133 avatars6.githubusercontent.com
151.101.40.133 avatars6.githubusercontent.com
151.101.24.133 avatars6.githubusercontent.com
151.101.76.133 avatars6.githubusercontent.com
```

```
151.101.196.133 avatars7.githubusercontent.com
151.101.76.133 avatars7.githubusercontent.com
```

```
151.101.40.133 avatars8.githubusercontent.com
151.101.196.133 avatars8.githubusercontent.com
151.101.76.133 avatars8.githubusercontent.com
```

```
185.199.108.153 github.io
185.199.110.153 github.io
185.199.111.153 github.io
```


关键而又时常抽风的地址：
```
github.githubassets.com [负责Github网站的样式和图片资源数据，抽风会导致网页错位]
```
