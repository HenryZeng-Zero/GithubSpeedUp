import requests
import locale
import json
import sys
import re

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

def OpenHosts():
    with open('hosts.json', 'r+') as f:
        return json.loads(f.read())


def WriteHosts(data):
    try:
        with open('hosts.json', 'w+') as f:
            f.write(data)
    except:
        print('error')


def GetLocalIP():
    try:
        Server = 'https://www.ip.cn/'
        IP = requests.get(Server, headers=headers)
        front = len('<p>您现在的 IP：<code>')
        end = len('</code></p><p>')*(-1)
        return re.search('<p>您现在的 IP：<code>.*?</code></p><p>', IP.text)[0][front:end]
    except:
        return ''

def DNS(domain):
    Server = 'http://119.29.29.29/d?dn='
    Locals = '&ip=' + LocalIP
    back = requests.get(Server + domain + Locals,headers=headers)
    passage = ''
    IP = []
    for i in back.text:
        if i == ';':
            IP.append(passage)
            passage = ''
            continue
        passage += i
    IP.append(passage)
    return IP


def WebDNS(data,mode):
    if mode == 'hosts':
        domain_ip = []
        for i in data:
            domans = data[i]
            domain_ip.append(DNS(domans)[0] + ' ' + domans)
        return domain_ip
    elif mode == 'IPs':
        domain_ip = []
        for i in data:
            domans = data[i]
            domain_ip.append(domans + ' |' + '|'.join(DNS(domans))+'|')
        return domain_ip

def helps():
    language, encoding = locale.getdefaultlocale()
    if language == 'zh_CN':
        print('python GSU.py [command]')
        print('[command]: ')
        print('     help         (帮助你查找帮助文档)')
        print('     add [domain] (添加待检测域名)')
        print('      └┈┈ add -y  (跳过确认部分)')
        print('     ls           (输出域名列表)')
        print('     rm [id]      (删除域名)')
        print('      └┈┈ rm -y   (跳过确认部分)')
        print('     do [id]      (输出hosts,默认是选择全部id)')
        print('     save [file]  (保存hosts)')
        print('     IPs [id]     (输出所有域名的ip,默认是选择全部id)')
    else:
        print('python GSU.py [command]')
        print('[command]: ')
        print('     help         (help you find help document)')
        print('     add [domain] (add domain for check)')
        print('      └┈┈ add -y  (pass the confirm part)')
        print('     ls           (print the list of domain )')
        print('     rm [id]      (del the domain from the list)')
        print('      └┈┈ rm -y   (pass the confirm part)')
        print('     do [id]      (print the hosts,The default select all id)')
        print('     save [file]  (save hosts to a file)')
        print('     IPs [id]     (print the all the domain\'s ip,The default select all id)')


if __name__ == "__main__":
    global LocalIP
    LocalIP = GetLocalIP()

    try:
        data = OpenHosts()
    except:
        data = {}
        print('Base data is broken')
    argv = sys.argv
    try:
        if(argv[1] == 'help'):
            helps()
        # help
        elif argv[1] == 'add':
            try:
                argvID = 2
                confirm = 'n'
                if argv[2] == '-y':
                    argvID += 1
                    confirm = 'y'
                else:
                    print('Your domain:', argv[2])
                    confirm = input('Make sure you want to add this domain (y/n)')
                    
                lens = len(data)
                # len获取元素数量，正好比字典下标多1
                if str(confirm) == 'y':
                    for i in data:
                        if data[i] == argv[argvID]:
                            print('This domain is recorded')
                            break
                    else:
                        data.update({lens: argv[argvID]})
                WriteHosts(json.dumps(data))
            except:
                helps()
                print('please check')
        # add
        elif argv[1] == 'ls':
            print('ID', 'Domain')
            for i in data:
                print(i, data[i])
        # ls
        elif argv[1] == 'rm':
            argvID = 2
            confirm = 'n'
            if argv[2] == '-y':
                argvID += 1
                confirm = 'y'
            else:
                print('Your choose:', argv[2])
                confirm = input('Make sure you want to remove this domain (y/n)')
            lens = len(data)
            if str(confirm) == 'y':
                for i in range(int(argv[argvID]), lens-1):
                    data[str(i)] = data[str(i+1)]
                data.pop(str(lens-1))
                WriteHosts(json.dumps(data))
        # rm
        elif argv[1] == 'do':
            print('=============================================')
            try:
                domain_do = data[argv[2]]
                print(DNS(domain_do)[0] + ' ' + domain_do)
            except:
                for i in WebDNS(data,'hosts'):
                    print(i)
            print('=============================================')
        elif argv[1] == 'save':
            Text = ''
            for i in WebDNS(data,'hosts'):
                Text += i +'\n'
            try:
                with open(argv[2],'w+') as f:
                    f.write(Text)
                print('Successful')
            except:
                print('error')
        # do
        elif argv[1] == 'IPs':
            print('=============================================')
            try:
                domain_IPs = data[argv[2]]
                print(domain_IPs + ' |' + '|'.join(DNS(domain_IPs))+'|')
            except:
                for i in WebDNS(data,'IPs'):
                    print(i)
            print('=============================================')
        # IPs

        else:
            helps()
            print('Please make sure you enter the true command line')
    except:
        helps()
        print('Please make sure you enter the true command line')
