import http
import http.client

path= input("Enter path of meta-data")

metadataAddress ="169.254.169.254"
connectionObj = http.client.HTTPConnection(metadataAddress)
connectionObj.request('GET',path)
response = connectionObj.getresponse()

if response.status == http.HTTPStatus.OK:
    s =response.read().decode().strip()
    print(s)
else:
  print("oops some error occured")