import requests

print (" Test (Scan) Dachore ")
imageName = input ('plz imageName = ')
url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
res = requests.get(url)
print (res.text)
