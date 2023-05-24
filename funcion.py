import requests as req
site = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks5.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks4.txt'
]
jar = '1'
jar1 = 'MCBOT.jar'
jar2 = 'KingDoS.jar'
jar3 = 'McStorm2.jar'
jar4 = 'botter.jar'
jar5 = 'java.jar'
alljarlist = [jar1,jar2,jar3,jar4,jar5]
name='1'
name1='MCBOT'
name2='KingDoS'
name3='McStorm'
name4='botter'
name5='Raffic'
allnamelist = [name1,name2,name3,name4,name5]
def updateproxy():
	with open('proxies.txt', 'w') as file:
		file.write('')
	for i in range(len(site)):
		get = req.get(site[i])
		with open('proxies.txt', 'r') as file:
			saveproxy = file.read()
			file.close()
		with open('proxies.txt', 'w') as file:
			file.write(f'{saveproxy}\n{get.text}')
			file.close()
def switchwhile():
	print('1. MCBOT \n2. KingDoS \n3. McStorm \n4. botter \n5. Raffic')
	jarinput = str(input(f'Какой jar файл хочете использовать >> '))
	if jarinput == '1':
		name=name1
		jar = jar1
		
	if jarinput == '2':
		name=name2
		jar = jar2
		
	if jarinput == '3':
		name=name3
		jar = jar3
		
	if jarinput == '4':
		name=name4
		jar = jar4
		
	if jarinput == '5':
		name=name5
		jar = jar5
		
def switch():
	print('1. MCBOT \n2. KingDoS \n3. McStorm \n4. botter \n5. Raffic')
	jarinput = str(input(f'Какой jar файл хочете использовать >> '))
	if jarinput == '1':
		name=name1
		jar = jar1
	if jarinput == '2':
		name=name2
		jar = jar2
	if jarinput == '3':
		name=name3
		jar = jar3
	if jarinput == '4':
		name=name4
		jar = jar4
	if jarinput == '5':
		name=name5
		jar = jar5