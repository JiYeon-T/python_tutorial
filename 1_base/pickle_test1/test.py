##制作（生成）一個二進制文件
import pickle

##寫入，二進制文件
list1 = [1, 2.34, 'a', [1, 2, 3]]
pickle_file = open('/home/qz/Desktop/python/pickle_test1/my_list.pkl', 'wb')	#寫二進制方式打開
pickle.dump(list1, pickle_file)							#pickle.dump()
pickle_file.close()

##在讀出來
pickle_file = open('/home/qz/Desktop/python/pickle_test1/my_list.pkl', 'rb')
list2 = pickle.load(pickle_file)						#pickle.load()
pickle_file.close()
print(list2)
