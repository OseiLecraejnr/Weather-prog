from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)      


api_key = "7f80366080690181e5bea3a30e76efd7'"

'''
def cedi_to_oth(amount, curr):
	
	currency1 = "USD"
	currency2 = "GBP"
	currency3 = "EUR"
	
'''
def current_location(f,e):
	print 'Which countryu are you in??' 
	f =raw_input("The Enter your country: ")

	print 'Which city are you in??' 
	e =raw_input("The Enter your city: ")


	owm = pyowm.OWM('7f80366080690181e5bea3a30e76efd7')
	observation = owm.weather_at_place(f+","+e)
	w = observation.get_weather()


	 
	wind = w.get_wind()
	humid = w.get_humidity()
	temperature = w.get_temperature('celsius')
	
	
'''
	if curr == currency1:
		cur = currency1 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	elif curr == currency2:
		cur = currency2 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	elif curr == currency3:
		cur = currency1 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	else:
		print "Sorry please enter a valid option"

	q = requests.get(url)
	json_d = q.json()

	return str(json_d[u'amount'])
	'''
	
	 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def res():
	if request.method == 'POST':
		city = request.form['city']
		country = request.form['country']
	print 'weather in ',e,' and ',f 
		
	print wind
	print humid
	print temperature
	print rain

	fresult = current_location(f,e)
	
	
	return render_template('result.html',fresult = fresult)
	

	
	'''
	if request.method == 'POST':
		value = request.form['value']
		 = request.form['location']
		
		if currency == "USD":
			denom = " Dollars"
		elif currency == "GBP":
			denom = " Pounds"
		elif currency == "EUR":
			denom = " Euros"
		else:
			denom = "Error"
			
			'''
 
if __name__ == '__main__':
  app.run(debug=True)
