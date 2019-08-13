import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
	print("This is the Entry:", entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		tempf = weather['main']['tempf']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:	
		final_str = 'There was a problem retrieving that information'
	return final_str	

def get_weather(city):
	#print("Hello, city is %s" % format(city))
	#weather_key = '68d36a96656ef7c8884df9eb89b4d5ba'
	# url = 'api.openweathermap.org/data/2.5/forecast/hourly'
	weather_key = '0ff229ce933a829f902541034ef75279'
	url = 'http://api.openweathermap.org/data/2.5/weather/'
	myparams = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=myparams)
	weather = response.json()

	label['text'] = format_response(weather)
	

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#api.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}
#68d36a96656ef7c8884df9eb89b4d5ba
# background_image = tk.PhotoImage (file='landscape.png')

background_image = tk.PhotoImage (file="c:\matt\landscape2.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="get weather", font=('courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, ancho='n')


label = tk.Label(lower_frame, font=('Century', 25))
label.place(relwidth=1, relheight=1)

print(tk.font.families())


root.mainloop()