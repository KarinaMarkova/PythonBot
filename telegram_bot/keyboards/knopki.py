from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

a1 = KeyboardButton('/Узнать_подробнее')
a2 = KeyboardButton('/Начать_обучение')
kb_otvet1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_otvet2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_otvet1.add(a1).add(a2)
kb_otvet2.add(a2)

#Перечисление тем
tema1 = KeyboardButton('/Тема_1')
tema2 = KeyboardButton('/Тема_2')
tema3 = KeyboardButton('/Тема_3')
tema4 = KeyboardButton('/Тема_4')
obzor = KeyboardButton('/Обзор_новых_тем')


kb_tema = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_tema.row(tema1, tema2).row(tema3, tema4).add(obzor)

#Кнопки по первой теме
tema1_zad1 = KeyboardButton ('/Проверочное_задание_Тема1_1')
tema1_zad2 = KeyboardButton ('/Проверочное_задание_Тема1_2')
test1 = KeyboardButton ('/Тест1')
tema1_zad1_pom = KeyboardButton ('/Нужна_помощь_Тема1_1')
tema1_zad1_otvet = KeyboardButton ('/Узнать_ответ_Тема1_1')
tema1_zad2_pom = KeyboardButton ('/Нужна_помощь_Тема1_2')
tema1_zad2_otvet = KeyboardButton ('/Узнать_ответ_Тема1_2')
kb_tema1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema1.add(tema1_zad1).add(tema1_zad2).add(test1)
kb_tema11 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema11.add(tema1_zad1_pom).add(tema1_zad1_otvet)
kb_tema12 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema12.add(tema1_zad2_pom).add(tema1_zad2_otvet)
#Кнопки для теста по первой теме
test1_1_otvet1 = KeyboardButton('/Привет_Teacher_C#')
test1_1_otvet2 = KeyboardButton('/Привет,Teacher_C#')
test1_1_otvet3 = KeyboardButton('/Нет_верного_ответа')
test1_2_otvet1 = KeyboardButton('/1')
test1_2_otvet2 = KeyboardButton('/2')
test1_2_otvet3 = KeyboardButton('/3')

kb_test1_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test1_2.row(test1_2_otvet1,test1_2_otvet2,test1_2_otvet3)
kb_test1_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test1_1.add(test1_1_otvet1).add(test1_1_otvet2).add(test1_1_otvet3)

#Кнопки по второй  теме
tema2_zad1 = KeyboardButton ('/Проверочное_задание_Тема2')
test2 = KeyboardButton ('/Тест2')
tema2_zad1_pom = KeyboardButton ('/Нужна_помощь_Тема2')
tema2_zad1_otvet = KeyboardButton ('/Узнать_ответ_Тема2')
kb_tema2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema2.add(tema2_zad1).add(test2)
kb_tema21 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema21.add(tema2_zad1_pom).add(tema2_zad1_otvet)

#Кнопки для теста по второй теме
test2_1_otvet1 = KeyboardButton('/Console.ReadLine(name)')
test2_1_otvet2 = KeyboardButton('/name=Console.ReadLine()')
test2_2_otvet1 = KeyboardButton('/1.Console.WriteLine("Привет_мир!");')
test2_2_otvet2 = KeyboardButton('/2.Console.ReadLine();')

kb_test2_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test2_2.row(test2_2_otvet1).row(test2_2_otvet2)
kb_test2_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test2_1.row(test2_1_otvet1).row(test2_1_otvet2)

#Кнопки по третьей теме
tema3_zad1 = KeyboardButton ('/Проверочное_задание_Тема3_1')
tema3_zad2 = KeyboardButton ('/Проверочное_задание_Тема3_2')
test3 = KeyboardButton ('/Тест3')

tema3_zad1_otvet = KeyboardButton ('/Узнать_ответ_Тема3_1')
tema3_zad2_pom = KeyboardButton ('/Нужна_помощь_Тема3_2')
tema3_zad2_otvet = KeyboardButton ('/Узнать_ответ_Тема3_2')
kb_tema3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema3.add(tema3_zad1).add(tema3_zad2).add(test3)
kb_tema31 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema31.add(tema3_zad1_otvet)
kb_tema32 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema32.add(tema3_zad2_pom).add(tema3_zad2_otvet)
#Кнопки для теста по первой теме
test3_1_otvet1 = KeyboardButton('/Числа')
test3_1_otvet2 = KeyboardButton('/Строки')
test3_1_otvet3 = KeyboardButton('/Какие-либо_данные')
test3_2_otvet1 = KeyboardButton('/char')
test3_2_otvet2 = KeyboardButton('/bool')
test3_2_otvet3 = KeyboardButton('/uint')

kb_test3_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test3_2.row(test3_2_otvet1,test3_2_otvet2,test3_2_otvet3)
kb_test3_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test3_1.add(test3_1_otvet1).add(test3_1_otvet2).add(test3_1_otvet3)


#Кнопки по четвертой теме
tema4_zad1 = KeyboardButton ('/Проверочное_задание_Тема4_1')
tema4_zad2 = KeyboardButton ('/Проверочное_задание_Тема4_2')
test4 = KeyboardButton ('/Тест4')
tema4_zad1_pom = KeyboardButton ('/Нужна_помощь_Тема4_1')
tema4_zad1_otvet = KeyboardButton ('/Узнать_ответ_Тема4_1')
tema4_zad2_pom = KeyboardButton ('/Нужна_помощь_Тема4_2')
tema4_zad2_otvet = KeyboardButton ('/Узнать_ответ_Тема4_2')
kb_tema4 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema4.add(tema4_zad1).add(tema4_zad2).add(test4)
kb_tema41 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema41.add(tema4_zad1_pom).add(tema4_zad1_otvet)
kb_tema42 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tema42.add(tema4_zad2_pom).add(tema4_zad2_otvet)

#Кнопки для теста по четвертой теме
test4_1_otvet1 = KeyboardButton('/Ответ1')
test4_1_otvet2 = KeyboardButton('/Ответ2')
test4_1_otvet3 = KeyboardButton('/Ответ3')
test4_2_otvet1 = KeyboardButton('/string')
test4_2_otvet2 = KeyboardButton('/byte')
test4_2_otvet3 = KeyboardButton('/double')

kb_test4_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test4_2.row(test4_2_otvet1,test4_2_otvet2,test4_2_otvet3)
kb_test4_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_test4_1.add(test4_1_otvet1).add(test4_1_otvet2).add(test4_1_otvet3)