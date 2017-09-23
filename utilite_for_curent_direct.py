# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py
import functions as fun                                                                                                                                                                                          
import sys
import os
import shutil
print(os.getcwd())
# print(h.look_dir(-1))
# f = open(sys.argv[0], "r")

# print(f.fileno())
# print(f.__getattribute__)
# os.close(f.fileno())
# print(f.fileno())
# print(sys.argv[0])
print("Утилита, позволяющую работать с папками текущей директории\
\n Меню выбора дейстия:\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\
\n3. Удалить папку\n4. Создать папку\n")
# abs_path = os.getcwd()
while True:

	choise = input("Выберите текущее действие\n")
	if int(choise) != 2:
		note = input("Выберите папку\n")

		if int(choise) <=0 or choise == "q":
			break
		elif int(choise) == 1:
			
			# if note == 'root':
			# 	fun.set_dir(note)
			# 	print("Успешный переход в директорию ", path)
			# else:
			# global path
			# path = os.path.join(abs_path, note)
			inspect = os.path.exists(note)#возращает True если указанный path существует в файловой системе
			if inspect == True:
				fun.set_dir(note)
				print("Успешный переход в директорию ", note)
			else:
				print("Указанного пути не существует")
				abs_path = os.getcwd()
				path = os.path.join(abs_path, note)
				fun.set_dir(path)

		
		elif int(choise) == 3:
			try:
				fun.choise(0, note)
				print("Успешное удаление папки ", note)
			except:
				print("Неудачная попытка удаления директории")

		elif int(choise) == 4:
			fun.choise(1, note, 1)
			print("Успешно созданна директория ", note)
		else:
			print("Некорректный ввод данных")
	else:
		path = os.getcwd()
		print(path)
		dirs = fun.see(path)
		print("Содержание текущей папки:\n", dirs)

