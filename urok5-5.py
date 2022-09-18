# import random
#
# def func():
#     pass
#
# class Human:
#     pass
#
# rq = random
# func = func
# nick = Human
# print(random.__name__) #ИНТРОСПЕКЦИЯ ПО ИМЕНИ
# print(rq.__name__)
# print(func.__name__)
# print(nick.__name__)

# list_1 = []
# for method in dir(list_1):
#     print(method) #интроспекция в методы выбранного элемента

# test = "test"
# def func():
#     pass
#
# print(callable(test)) #проверить можно ли выполнить элемент сам по себе
# print(callable(func))

#ПОДКЛАССЬІ И ИНСТАНСЬІ
# class Father:
#     pass
#
# class Son(Father):
#     pass
#
# class Pet:
#     pass
#
# obj_son = Son()
#
# print(issubclass(Father, Son))
# print(issubclass(Son, Father))
# print(isinstance(obj_son, Son))
# print(isinstance(obj_son, Father))
# print(isinstance(obj_son, Pet))

#ПРОВЕРКА НА ТО ЧЕМ ЯВЛЯЕТСЯ ЭЛЕМЕНТ
# import inspect
# import random
#
# print(inspect.ismodule(random))
# print(inspect.isclass(random))
# print(inspect.isfunction(random))

#SYS
# import sys
#
# for method in dir(sys):
#      print(method)
#
# print(sys.executable)
# print(sys.version_info)
# print(sys.platform)
# print(sys.argv)

#BUILTIN
# for _ in dir(__builtins__):
#     print(_)
