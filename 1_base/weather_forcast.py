import os  # change the dicrectory
import pickle

os.getcwd()
# TODO: 这种写法并不好,代码移植性很差
os.chdir('/home/qz/Desktop/python/weather_forecast/')
os.getcwd()

def weather_forcast_test1():
    city = {
        'YinChuan': '0000',
        'WuZhong': '0001',
        'DaWuKou': '0002',
        'YanChi': '0003',
        'ZhongWei': '0004',
        'XiNing': '0005'
    }  # define a dictionary

    ##Write this program to get the city_data.pkl file.  二进制文件
    pickle_file = open('city_data.pkl', 'wb')
    pickle.dump(city, pickle_file)
    pickle_file.close()

    ## use city_data.pkl
    pickle_file = open('city_data.pkl', 'rb')
    city = pickle.load(pickle_file)
    pickle_file.close()

def weather_forcat_test2():
    pickle_file = open('city_data.pkl', 'rb')
    city = pickle.load(pickle_file)  # type(city) = 'dict'
    pickle_file.close()

# other program  use this dictionary to accomplish the weather forcast funcion

if __name__ == '__main__':
    weather_forcat_test2()