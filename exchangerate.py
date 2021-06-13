import requests

#Base Url
url = 'http://data.fixer.io/api/latest?access_key=4099109ea30c1f56f557c65dfb0a0051&format=1'

class Converter():
	def __init__(self,url):
		self.data = requests.get(url).json()
		self.currency = self.data['rates']

	def converting(self, from_currency, to_currency, amount):
		if from_currency == 'EUR' and to_currency == 'USD' :
			amount = round(amount * self.currency[to_currency], 2)

		return amount

#user INPUTS
amount = int(input("AMOUNT TO EXCHANGE FROM EUR TO USD: "))
c = Converter(url)
print(c.converting('EUR', 'USD', amount))




