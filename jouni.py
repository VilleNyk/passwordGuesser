# importing the requests library
from concurrent.futures import thread
import requests
import json
import string
import random
from time import sleep
import itertools
import threading

words = {"v1lle", "hahaa"}

exitFlag = 0

def keyGenerator():
	guess = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
	if not guess in words:
		print(words)
		print("kokeillaan: " + guess)
		words.add(guess)
		return guess
		
	
  
# defining the api-endpoint 
url = "https://jolammi.me/apis/bday/"

def requester(avain):
	data = {'key': avain}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

	# sending post request and saving response as response object
	r = requests.post(url, data=json.dumps(data), headers=headers)

	# extracting response text 
	response = json.loads(r.text)
	response = response['data']
	expectedResponse = json.loads('{"data": "Ei ollu taeae, try again"}') 
	expectedResponse = expectedResponse['data']
	print(response)
	if response != expectedResponse:
		print("Voitto!, Avain on: " + avain)
		exitFlag = 1
		return True
	return False

def randomGuesser():
	arvattu = False 
	while not arvattu:
		sleep(0.01)
		
		# data to be sent to api
		avain = keyGenerator()
		arvattu = requester(avain)
	

def letsIterate():
	arvattu = False
	avain = ""
	chars = 'abcdefghijklmnopqrstuvwxyz123456789'
	while not arvattu:
			sleep(0.01)
			for c1 in chars:
				for c2 in chars:
					for c3 in chars:
						for c4 in chars:
							for c5 in chars:
								avain = (c1+c2+c3+c4+c5)
								print("kokeillaan " + avain)
								arvattu = requester(avain)


#letsIterate()



class myThread (threading.Thread):
	def __init__(self, threadID, name, chars) -> None:
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.chars = chars
	def run(self):
		print("Starting " + self.name)
		letsIterateMultiThread(self.name, self.chars)
		print("Exiting " + self.name)
	
		super().__init__()


def letsIterateMultiThread(threadName, chars):
	arvattu = False
	avain = ""
	while not arvattu:
		if exitFlag:
			threadName.exit()
		sleep(0.01) 
		for c1 in chars:
			for c2 in chars:
				for c3 in chars:
					for c4 in chars:
						for c5 in chars:
							avain = (c1+c2+c3+c4+c5)
							print("kokeillaan " + avain)
							arvattu = requester(avain)


thread1 = myThread(1, "Thread-1", "abcdefghijklmnopqrstuvwxyz123456789")
thread2 = myThread(2, "Thread-2", "987654321zyxwvutsrqponmlkjihgfedcba")

thread1.start()
thread2.start()