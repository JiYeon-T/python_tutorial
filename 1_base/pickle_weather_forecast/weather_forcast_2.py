## use city_data.pkl
import pickle

pickle_file = open('city_data.pkl', 'rb')
city = pickle.load(pickle_file)			#type(city) = 'dict'
pickle_file.close()	



##We can see that the program place is smaller than before.
