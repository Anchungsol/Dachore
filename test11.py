
import requests


def main():
	print ("docker image vuln scan progarm")
	imageName = input ('plz imageName = ')
	url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
	res = requests.get(url)
	print (res.text)

if __name__ == '__main__':
	main()
