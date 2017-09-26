
import os
import sys
import shutil
# import psutil
#Функция для выбора действия 1 - создать 9 папок в текущей директории
#0 - удаление ранее созданных папок
def set_dir(path):
	"""
	Функция устанавливает текущую дирректорию                                                                                                                                                                                                                                                                                                                                                                                                                                              

	"""
	try:
		os.chdir(path)
	except:
		print("Указанного пути не существует")

def choise(moution, name = "dir_",n = 1):
	"""
	Функция создает moution = 1, или удаляет moution = 0 папку в папке из
	которой запущен скрипт, в необязательном атрибуте name можно указать
	имя папки, 3й(необязательный) атрибут n - количество папок 

	"""
	if moution == 1:
		#Содание директорий dir_1 - dir_9
		try:
			for item in range(1, n + 1):
				new_dir = "%s%d"%(name,item)
				dir_path = os.path.join(os.getcwd(),'{new_dir}'.format(new_dir = new_dir))
				os.mkdir(dir_path)
				print("Директория {d} - {new_dir} создана".format(d = item, new_dir = new_dir))
		except FileExistsError:
			print('Такая директория уже существует')
	elif moution == 0:
		#Удаление директорий dir_1 - dir_9
		try:
			for item in range(1, n+1):
				new_dir = "%s%d"%(name,item)
				dir_path = os.path.join(os.getcwd(),'{new_dir}'.format(new_dir = new_dir))
				if new_dir in dir_path:
					shutil.rmtree(dir_path)
					print("Удаление директории {d} - {new_dir} выполнено".format(d = item, new_dir = new_dir))
		except FileNotFoundError:
			print('Такая директория не существует')
	else:
		print("Некорректно выбрано действие")
# Задача-2:
# Напишите скрипт отображающий папки текущей директории
def look_dir(what_look):
	"""
	Если what_look = 1 - отображаются папки текущей директории, если what_look = 2 - отображаются 
	файлы.Если what_look < 0 то отображается все содержимое директории , если what_look = 0, 
	то отображается абсолютный путь к текущей дирректории

	"""
	if what_look < 0:
		dir_name = list(os.walk(os.getcwd()))[0][1:3]
	else:
		dir_name = list(os.walk(os.getcwd()))[0][what_look]
	return dir_name
def see(path):
	"""
	Просмотреть содержимое текущей папки

	"""
	return os.listdir(path)#список с именами элементов указанного каталога

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт
def copy_file(name = os.path.splitext(sys.argv[0])[0]):#кортеж по разделителю "." базовое имя и расширение
	"""
	По умолчанию скопирует файл текущего скрипта в файл <имя_скрипта>_copy.py

	"""
	shutil.copy(sys.argv[0], '%s_copy.py'%(name))

#Функция удаления директории или файла
def remove_file(name,what = 2):
	if what == 0:
		os.rmdir(os.path.join(os.getcwd(),name))#удаление директории
	elif what == 1:
		os.remove(os.path.join(os.getcwd(),name))#удаление файла
	elif what == 2: pass
	elif what < 0:
		shutil.rmtree(os.path.join(os.getcwd(),name))#удаление дерева папок
	else:
		print("Некорректный ввод данных")
def new_dir(name):
	try:
		dir_path =os.path.join(os.getcwd(), name)
		os.mkdir(dir_path)
		# print("Директория {new_dir} создана".format(new_dir = name))
	except FileExistsError:
		print('Такая директория уже существует')


# os.rename(src,dst)#переименовывает файл или каталог scr в dst

def separator(strk, num, sep):
	print(strk.center(num,sep))
if __name__ == '__main__':
	separator("Задача1", 35, "*")
	choise(1, "Моя папка_", 1)

	separator("Задача2", 35, "*")
	print(look_dir(1))
	# remove_file("hw5e.py_copy.py",1)
	# os.makedirs(os.path.join(os.getcwd(),"new"))
	print(see())

	separator("Задача3", 35, "*")
	# copy_file()
	dir_name = list(os.walk(os.getcwd()))[0][2]
	print(dir_name)