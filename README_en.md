Lang: [ZH-CN](README.md) ; [EN](README_en.md)
# Cause
In China, due to some problems of network conditions, and because Github does not have a CDN server in China, the speed of accessing Github is quite slow, regardless of uploading, downloading or accessing.

# Elements

Improve local access by requesting locally optimal DNS resolution data from the DNS server that provides the Web request and storing the output data in the hosts file

# Use

Execute using Python3

```
git clone https://github.com/zzh-blog/GithubSpeedUp.git
cd GithubSpeedUp
python GSU.py [command]
```
See the help document
```
python GSU.py help
```

Help document
```
[command]:
     help         (help you find help document)
     add [domain] (add domain for check)
      └┈┈ add -y  (pass the confirm part)
     ls           (print the list of domain )
     rm [id]      (del the domain from the list)
      └┈┈ rm -y   (pass the confirm part)
     do           (print the hosts)
     save [file]  (save hosts to a file)
```