city = {			
'YinChuan' : '0000',
'WuZhong' : '0001',
'DaWuKou' : '0002',
'YanChi' : '0003',
'ZhongWei' : '0004',
'XiNing' : '0005'
}				#define a dictionary
import os			#change the dicrectory
os.getcwd()
os.chdir('/home/qz/Desktop/python/weather_forecast/')
os.getcwd()


##Write this program to get the city_data.pkl file.  er jin zhi wen jian 
import pickle
pickle_file = open('city_data.pkl', 'wb')
pickle.dump(data, pickle_file)
pickle_file.close()


## use city_data.pkl
pickle_file = open('city_data.pkl', 'rb')
city = pickle.load(pickle_file)
pickle_file.close()



##other program  use this dictionary to accomplish the weather forcast funcion
