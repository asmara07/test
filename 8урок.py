import requests
url =" https://kanstik.uz/catalog/gigienicheskie_tovary/"
response = requests.get(url)
print(response.text)




nums = [1,3,4,6,8,20]
test = map(lambda a : a**2, nums)
print(list(test))

