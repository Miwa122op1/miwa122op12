import requests as req
import cheakproxy as check
filename = {
	'http': 'phttp.txt',
	'socks4': 'psocks4.txt',
	'socks5': 'psocks5.txt'
}
sitesocks4 = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks4.txt',
'https://api.openproxylist.xyz/socks4.txt'
]
sitesocks5 = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks5.txt',
'https://api.openproxylist.xyz/socks5.txt'
]
sitehttp = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt',
'https://api.openproxylist.xyz/http.txt',
]
sitehttps = [
'https://advanced.name/freeproxy/646079a732415']
def gethttp():
	with open(filename['http'], 'w') as file:
		file.write('')
	for i in range(len(sitehttp)):
		get = req.get(sitehttp[i])
		with open(filename['http'], 'r') as file:
			saveproxy = file.read()
			file.close()
		with open(filename['http'], 'w') as file:
			file.write(f'{saveproxy}\n{get.text}')
			file.close()
	check.getline(filename['http'], 'http')

def getsocks5():
	with open(filename['socks5'], 'w') as file:
		file.write('')
	for i in range(len(sitesocks5)):
		get = req.get(sitesocks5[i])
		with open(filename['socks5'], 'r') as file:
			saveproxy = file.read()
			file.close()
		with open(filename['socks5'], 'w') as file:
			file.write(f'{saveproxy}\n{get.text}')
			file.close()	
def getsocks4():
	with open(filename['socks4'], 'w') as file:
		file.write('')
	for i in range(len(sitesocks4)):
		get = req.get(sitesocks4[i])
		with open(filename['socks4'], 'r') as file:
			saveproxy = file.read()
			file.close()
		with open(filename['socks4'], 'w') as file:
			file.write(f'{saveproxy}\n{get.text}')
			file.close()
		check.getline(filename['socks4'], 'socks4')
def saveproxy1x1(proxy1,proxy2):
    with open(f'{proxy1}','r') as file:
        saveproxy1 = file.read()
        file.close()
    with open(f'{proxy2}','r') as file:
        saveproxy2 = file.read()
        file.close()
    with open(f'proxies.txt','w') as file:
        file.write(f'{saveproxy1}\n{saveproxy2}')
        file.close()

if __name__ == '__main__':
	print('socks4 - для майнкрафт ддос\nsocks5 - для майнкрафт ддос\nhttp - для захода на http сайты\nДля майнкрафт ддос пропишите minecraft')
	proxie = input('Какой вам нужен прокси? >> ')
	if proxie == 'socks4':
		getsocks4()
	if proxie == 'socks5':
		getsocks5()
	if proxie == 'http':
		gethttp()
	if proxie == 'minecraft':
		getsocks4()
		getsocks5()
		saveproxy1x1(filename['socks5'],filename['socks4'])	