import urllib.request , socket
socket.setdefaulttimeout(1)
def getline(pname:str, namep:str):
    with open(pname) as f:
        proxyList = f.readlines()
    proxyList = [x.strip() for x in proxyList]
    if pname == 'psocks4.txt':
        pass
    if pname == 'phttp.txt':
        for item in proxyList:
            if httpcheck(item):
                print("[BAD]", item)     
            else:
                print("[WORK]", item)
                with open(f'workp_{namep}.txt','r') as file:
                    saveproxy = file.read()
                with open(f'workp_{namep}.txt','w') as file:
                    file.write(f'{saveproxy}\n{item}')
    if pname == 'psocks5.txt':
        result = loop.run_until_complete(asyncio.gather(*(check_proxy(host, int(port)) for host, port in proxyList)))
        with open(f"workp_{namep}.txt", "w") as f:
            f.write("\n".join((info["proxy"] for info in filter(lambda d: d["passed"], result))))
              
def httpcheck(pip):
    try:       
        proxy_handler = urllib.request.ProxyHandler({'http': pip})       
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)       
        sock=urllib.request.urlopen('http://www.google.com')
    except urllib.error.HTTPError as e:       
        return e.code
    except Exception as detail:
        return 1
    return 0
