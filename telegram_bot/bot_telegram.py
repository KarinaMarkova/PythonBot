from aiogram import Bot,types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import sqlite3 as sq
from keyboards.knopki import kb_otvet1, kb_otvet2, kb_tema, kb_tema1, kb_tema11, kb_tema12, kb_test1_1, kb_test1_2
from keyboards.knopki import kb_tema2, kb_tema21, kb_test2_1, kb_test2_2
from keyboards.knopki import kb_tema3, kb_tema31, kb_tema32, kb_test3_1, kb_test3_2
from keyboards.knopki import kb_tema4, kb_tema41, kb_tema42, kb_test4_1, kb_test4_2


storage=MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp=Dispatcher(bot, storage=storage)

'''*****************ДЕЙСТВИЯ ДЛЯ АДМИНА***********************'''
class FSMAdmin(StatesGroup):
	name = State()
	tema = State()

#команда отмены(выхода из состояний)
@dp.message_handler(state="*",commands = ['отмена'])
@dp.message_handler(Text(equals = 'отмена', ignore_case = True),state = "*")
async def cancel_hadler(message: types.Message, state:FSMContext):
	if message.from_user.id == 692990040:
		current_state =await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.reply('ОК')

#Начало диалога загрузки новой темы
@dp.message_handler(commands=['Загрузить'],state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == 692990040:
		await FSMAdmin.name.set()
		await message.reply('Напиши название новой темы')
	else:
		await message.reply('У тебя нет доступа к этому разделу')

#Получаем название и записываем в словарь
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == 692990040:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin.next()
		await message.reply("Отправь мне материал по этой теме")
	else:
		await message.reply('У тебя нет доступа к этому разделу')	

#Получаем материал и записываем в словарь
@dp.message_handler(state=FSMAdmin.tema)
async def load_tema(message: types.Message, state: FSMContext):
	if message.from_user.id == 692990040:	
		async with state.proxy() as data:
			data['tema'] = message.text

		await sqlite_bd.sql_add_command(state)

		await state.finish()


'''*****************БАЗА ДАННЫХ*********************'''

#создание (подключение) базы данных

def sql_start():
	global base,cur
	base = sq.connect('new_tema')
	cur = base.cursor()
	if base:
		print('База данных успешно подключена!')
	base.execute('CREATE TABLE IF NOT EXISTS info(name 	TEXT, tema TEXT)')
	base.commit()

async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO info VALUES(?, ?)', tuple(data.values()))
		base.commit()


'''*************ДEЙСТВИЯ ДЛЯ ПОЛЬЗОВАТЕЛЯ**************'''


####Сообщение об успешном подключении бота и базы данных
async def on_startup(_):
	print('Бот успешно подключен')
	sql_start()


@dp.message_handler(commands=['start' , 'help'])
async def command_start(message : types.Message):
	name = message.from_user.first_name
	ID = message.from_user.id
	await message.answer(f'Привет ,{name}'
						f'\nЯ - телеграм-бот Teacher_C#, и моя главная цель - помочь тебе приобрести начальные навыки владения языком С#'
						f'🎓\nНаше обучение будет состоять из нескольких этапов (теория, практика и закрепление материала с помощью тестов). Если хочешь узнать об этом поподробнее, нажми соответствующую кнопку или же переходи прямиком к обучению \nДумаю, занятия будут не скучными и весьма познавательными. Удачи!🍀' , reply_markup=kb_otvet1)

@dp.message_handler(commands=['Узнать_подробнее'])
async def command_podrobn(message : types.Message):
	await message.answer('Отлично! Я рад, что тебе интересно.😄\nИтак, всего в план обучения входит 8 уроков, по которым я буду выдавать теорию. Изучив теорию, ты сможешь пройти практику, самостоятельно выполнив предложенное задание и, в случае затруднения или желания сверить свой ответ, попросить у меня правильное решение. \nВ конце каждой из тем, тебя будет ожидать тест по пройденному материалу.\nНу что, начнем наше обучение?🤓 ', reply_markup=kb_otvet2)

@dp.message_handler(commands=['Начать_обучение'])
async def command_nach_obuch(message : types.Message):
	await message.answer('Замечательно! Ученье — свет, а неученье — тьма🔎. Какую тему начнем изучать?\n Тема 1 - Вывод данных\n Тема 2 - Ввод данных\n Тема 3 - Типы данных в С# и инициализация переменной\n Тема 4 - Конвертация данных ',reply_markup=kb_tema)


'''*************ИЗУЧЕНИЕ ПЕРВОЙ ТЕМЫ**************'''


@dp.message_handler(commands=['Тема_1'])
async def command_tema1(message : types.Message):
	await message.answer(f'Для вывода данных на консоль используется метод "Console.WriteLine(); '
						f'\nДля вывода информации на консоль внутри круглых скобок метода "Console.WriteLine();" '
						f'мы пишем то, что хотим вывести на экран.'
						f'\n\nПри написании текста, заключаем его в кавычки.Кавычки должны быть двойными(" ").\nПосле закрытия скобки ставим точку с запятой (в С# после любой строчки кода ставится ";" )'
						f'\n\n Каждая последующая команда "Console.WriteLine();" выводит указанный текст с новой строки. Например, результатом работы следующей программы'
						f'\n\n   Console.WriteLine("Привет!");\n   Console.WriteLine("Как твои дела?");\n\nБудет код\n\n   Привет!\n   Как твои дела?\n\n'
						f'Для того, чтобы вывести ответ в одной строке, следует воспользоваться методом Console.Write(); Таким образом, программа: \n\n   Console.Write("Привет!");\n   Console.Write("Как дела?");'
						f'\n\nВыведет результат:\n\n   Привет!Как дела?\n\nИтак, теорию по первой теме можно считать успешно пройденной, поэтому смело переходим к практике. Если ты уверен в своих силах, то можешь сразу переходить к контрольному тесту.',reply_markup=kb_tema1)


@dp.message_handler(commands=['Проверочное_задание_Тема1_1'])
async def command_prov_tema1(message : types.Message):
	await message.answer('Напиши программу для вывода следующих строчек:\n\n   Привет, Teacher_C#!\n   Я успешно справляюсь со своим первым заданием',reply_markup=kb_tema11)

@dp.message_handler(commands=['Нужна_помощь_Тема1_1'])
async def command_tema1(message : types.Message):
	await message.answer('Обрати внимание, что каждое предложение написано с новой строки и вспомни теоретический материал.', reply_markup=kb_tema11)

@dp.message_handler(commands=['Узнать_ответ_Тема1_1'])
async def command_tema1(message : types.Message):
	await message.answer('Console.WriteLine("Привет,Teacher_C#!");\nConsole.WriteLine("Я успешно справляюсь со своим первым заданием");', reply_markup=kb_tema1)

@dp.message_handler(commands=['Проверочное_задание_Тема1_2'])
async def command_tema1(message : types.Message):
	await message.answer('Напиши программу для вывода следующих строчек:\n\n   Привет, Teacher_C#!Я успешно справляюсь со своим вторым заданием',reply_markup=kb_tema12)

@dp.message_handler(commands=['Нужна_помощь_Тема1_2'])
async def command_tema1(message : types.Message):
	await message.answer('Обрати внимание, что предложения написаны в одной строке и вспомни теоретический материал.', reply_markup=kb_tema12)

@dp.message_handler(commands=['Узнать_ответ_Тема1_2'])
async def command_tema1(message : types.Message):
	await message.answer('Console.Write("Привет,Teacher_C#!");\nConsole.Write("Я успешно справляюсь со своим вторым заданием");', reply_markup=kb_tema1)
	
	############ТЕСТ ПО ПЕРВОЙ ТЕМЕ###############

@dp.message_handler(commands=['Тест1'])
async def command_test(message : types.Message):
	await message.answer('Браво!\nМы перешли к тесту, а это значит, что изучение первой темы подошло к концу и не за горами переход ко второй.Однако перед этим, давай посмотрим, чему же ты научился \nИтак, в тесте будет 2 вопроса,за правильный ответ на каждый из которых ты получаешь балл. Желаю успехов!\n\n   Вопрос №1:\n'
						f'Каким будет вывод этих команд?\n   Console.WriteLine("Привет")\n   Console.WriteLine("Teacher_C#"") ?',reply_markup=kb_test1_1)

@dp.message_handler(commands=['Привет_Teacher_C#','Привет,Teacher_C#'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз\n')

@dp.message_handler(commands=['Нет_верного_ответа'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ!\nВопрос №2:\n'
						f'Какой из вариантов корректный?\n\n1.Console.WriteLine("Привет мир!");\n2.Console.Writeline("Привет мир!");\n3.Console.WriteLine(Привет мир!);', reply_markup=kb_test1_2)	
	
@dp.message_handler(commands=['3','2'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз')

@dp.message_handler(commands=['1'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ\n\nПервая тема успешно изучена и ты можешь переходить к следующей,но помни, что всегда можешь вернуться обратно, если что-то забудешь', reply_markup=kb_tema)


'''****************ИЗУЧЕНИЕ ВТОРОЙ ТЕМЫ**************'''


@dp.message_handler(commands=['Тема_2'])
async def command_tema1(message : types.Message):
		await message.answer(f'Для ввода данных используется метод Console.ReadLine();\n\n'
						f'\nДавай рассмотрим следующую программу:\n\n   Console.WriteLine("Введите свое имя:");\n   var name = Console.ReadLine();'
						f'Метод Console.ReadLine(); работает следующим образом: когда программа вывела на экран текст, известный в момент запуска программы, "Введите свое имя:", программа ждет ввода данных у пользователя. Как только пользователь ввел данные и нажал Enter программа, как бы подставляет данные вместо метода Console.ReadLine()'
						f'Таким образом метод Console.ReadLine(); получает данные от пользователя и отправляет их в переменную name. О том, что такое переменная, ты узнаешь в следующем уроке.\n\nЗапомни: при выполнении следующего задания приписка var обязательна.',reply_markup=kb_tema2)
	
@dp.message_handler(commands=['Проверочное_задание_Тема2'])
async def command_tema1(message : types.Message):
	await message.answer('Что выведет следующая программа, если пользователь введет Teacher_C#:\n\n   var name = Console.ReadLine();',reply_markup=kb_tema21)

@dp.message_handler(commands=['Нужна_помощь_Тема2'])
async def command_tema1(message : types.Message):
	await message.answer('Обрати внимание, какой именно метод представлен в примере и вспомни его функции', reply_markup=kb_tema21)

@dp.message_handler(commands=['Узнать_ответ_Тема2'])
async def command_tema1(message : types.Message):
	await message.answer('Программа ничего не выведет, так как метод вывода информации отсутствует', reply_markup=kb_tema2)


	############ТЕСТ ПО ВТОРОЙ ТЕМЕ###############

@dp.message_handler(commands=['Тест2']) 
async def command_test(message : types.Message):
	await message.answer('Браво!\nМы перешли к тесту, а это значит, что изучение второй темы подошло к концу и не за горами переход к третьей.Однако перед этим, давай посмотрим, чему же ты научился \nИтак, в тесте будет 2 вопроса,за правильный ответ на каждый из которых ты получаешь балл. Желаю успехов!\n\n   Вопрос №1:\n'
						f'Выбери рабочую команду из представленных ниже:\n',reply_markup=kb_test2_1)

@dp.message_handler(commands=['Console.ReadLine(name)'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз\n')

@dp.message_handler(commands=['name=Console.ReadLine()'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! \nВопрос №2(очень легкий):\n'
						f'Какой из вариантов корректный?\n\n1.Console.WriteLine("Привет_мир!");\n2.Console.ReadLine();', reply_markup=kb_test2_2)	
	
@dp.message_handler(commands=['1.Console.WriteLine("Привет_мир!");'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз\n')

@dp.message_handler(commands=['2.Console.ReadLine();'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Ты получаешь балл\n\n Вторая тема успешно изучена и ты можешь переходить к следующей,но помни, что всегда можешь вернуться обратно, если что-то забудешь', reply_markup=kb_tema)
	
'''****************ИЗУЧЕНИЕ ТРЕТЬЕЙ ТЕМЫ**************'''

@dp.message_handler(commands=['Тема_3'])
async def command_tema1(message : types.Message):
	await message.answer(f'С точки зрения программиста данные — это часть программы, совокупность значений определённых ячеек памяти, преобразование которых осуществляет код.Переменная - именованный объект, который содержит в себе какие-либо данные. \nСохранить в переменной - значит поместить данные где-либо в оперативной памяти, для их дальнейшего использования.'
						f'\nДля создания переменной используется следующая формула:\n\n  тип_данных имя_переменной;\n\nНапример, следующая программа:\n\n   int a;\n\nВ данном примере, для создания переменной, мы взяли числовой тип данных int и назвали нашу переменную a'
						f'Для инициализации/присвоения значения переменной в программировании используется оператор присваивания - знак =. Для присвоения значения переменной используется следующая формула:\n\n   тип_данных имя_переменной = значение_переменной;\n\nРассмотрим следующую строчку кода:\n\n   int a = 1;\n\nВ данном примере мы присвоили переменной a, изначально зная ее тип данных(int), значение 1.'
						f'\n\nТИПЫ ДЫННЫХ )'
						f'\n\nЧисловой тип: byte a = 123;\nЧисловой тип (с плавающей точкой): double b = 1.5;\nСимвольный тип: char; string d = "Привет, мир!"; \nЗапомни: данные, помещаемые в переменную с типом char, обрамляются одинарными кавычками, а с типом string - двойными.\nЛогический тип: bool e = true; '
						f'\n\nТакже мы можем присвоить одной переменной значение другой (если эти переменные имеют одинаковы типы данных).\n\nИтак, теорию по третьей теме можно считать успешно пройденной, поэтому смело переходим к практике. Если ты уверен в своих силах, то можешь сразу переходить к контрольному тесту.',reply_markup=kb_tema3)

@dp.message_handler(commands=['Проверочное_задание_Тема3_1'])
async def command_prov_tema1(message : types.Message):
	await message.answer('Как присвоить переменной с значение 25?',reply_markup=kb_tema31)

@dp.message_handler(commands=['Узнать_ответ_Тема3_1'])
async def command_tema1(message : types.Message):
	await message.answer('int c = 25;\nМы присвоили переменной с, изначально зная ее тип данных(int), значение 25.', reply_markup=kb_tema3)

@dp.message_handler(commands=['Проверочное_задание_Тема3_2'])
async def command_tema1(message : types.Message):
	await message.answer('Как переменной а присвоить значение переменной с из предыдущего проверочного задания?',reply_markup=kb_tema32)

@dp.message_handler(commands=['Нужна_помощь_Тема3_2'])
async def command_tema1(message : types.Message):
	await message.answer('Следует не забыть, что сначала все же нужно присвоить значение переменной с', reply_markup=kb_tema32)

@dp.message_handler(commands=['Узнать_ответ_Тема3_2'])
async def command_tema1(message : types.Message):
	await message.answer('int с = 25;\nint a = c;\nВ данном примере мы вначале присвоили переменной с значение 25, после чего присвоили переменной j значение i.', reply_markup=kb_tema3)

	
############ТЕСТ ПО ТРЕТЬЕЙ ТЕМЕ###############

@dp.message_handler(commands=['Тест3'])
async def command_test(message : types.Message):
	await message.answer('Браво!\nМы перешли к тесту, а это значит, что изучение третьей темы подошло к концу и не за горами переход к четвертой.Однако перед этим, давай посмотрим, чему же ты научился \nИтак, в тесте будет 2 вопроса. Желаю успехов!\n\n   Вопрос №1:\n'
						f'Что содержит в себе переменная?',reply_markup=kb_test3_1)

@dp.message_handler(commands=['Числа','Строки'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз\n')

@dp.message_handler(commands=['Какие-либо_данные'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ!\nВопрос №2:\n'
						f'Какой из вариантов является логическим типом данных?', reply_markup=kb_test3_2)	
	
@dp.message_handler(commands=['char','uint'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз')

@dp.message_handler(commands=['bool'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ\n\nТретья тема успешно изучена и ты можешь переходить к следующей,но помни, что всегда можешь вернуться обратно, если что-то забудешь', reply_markup=kb_tema)

'''*************ИЗУЧЕНИЕ ЧЕТВЕРТОЙ ТЕМЫ**************'''
@dp.message_handler(commands=['Тема_4'])
async def command_tema1(message : types.Message):
	await message.answer(f'Конвертация данных — преобразование данных из одного формата в другой.'
						f'\nНо зачем конвертировать данные в C#? При вводе данных в консоль, они автоматически преобразуются в формат string. Рассмотрим следующую программу:'
						f'\n\n   Console.WriteLine("Введите число:");\n\n   string number = Console.ReadLine();\nПеременная number будет иметь тип данных string, несмотря на то< что в консоль мы введем число.'
						f'\n\nЕсли мы попробуем заменить string на var, object или dynamic, то формат данных все равно останется string. Это будет выглядеть следующим образом:\n\n   string number = "34";'
						f'\n\n Но нам нужно использовать число 34, например, для сложения (более подробнее арифметические вычисления мы изучим позже), для этого нам надо переменную number с типом string конвертировать в числовой тип данных. '
						f'\n\nДля конвертации данных при помощи класса Convert используется следующая формула:\n\n   string имя_переменной1 = значение_переменной1;\n\n'
						f'Название_типа_данных(в который хотим конвертировать) имя_переменной2 = Convert.To_название_типа_в библиотеке_.NET_(название_переменной1);'
						f'Для конвертации строк при помощи метода Parse используется следующая формула:\n\n   string имя_переменной1 = значение_переменной1;\n\n   Название_типа_данных(в который хотим конвертировать) имя_переменной2 = название_типа_данных(в который хотим конвертировать).Parse(название_переменной1);',reply_markup=kb_tema4)

@dp.message_handler(commands=['Проверочное_задание_Тема4_1'])
async def command_prov_tema1(message : types.Message):
	await message.answer('Зачем конвертировать данные?',reply_markup=kb_tema41)

@dp.message_handler(commands=['Нужна_помощь_Тема4_1'])
async def command_tema1(message : types.Message):
	await message.answer('Посмотри на строку ниже и подумай, сможем ли мы использовать ее как число?\nstring number = "34";', reply_markup=kb_tema41)

@dp.message_handler(commands=['Узнать_ответ_Тема4_1'])
async def command_tema1(message : types.Message):
	await message.answer(f'При вводе данных в консоль, они автоматически преобразуются в формат string.Рассмотрим следующую программу:\n\nConsole.WriteLine("Введите число:");\nstring number = Console.ReadLine();\n\nПеременная number будет иметь тип данных string, несмотря на то что в консоль мы введем число.Если мы попробуем заменить string на var, object или dynamic, то формат данных все равно останется string.'
						f'Но нам нужно использовать число 34, например, для сложения (более подробнее арифметические вычисления мы изучим позже), для этого нам надо переменную number с типом string конвертировать в числовой тип данных.', reply_markup=kb_tema4)

@dp.message_handler(commands=['Проверочное_задание_Тема4_2'])
async def command_tema1(message : types.Message):
	await message.answer('Какая формула импользуется для конвертации строк при помощи метода Parse?',reply_markup=kb_tema42)

@dp.message_handler(commands=['Нужна_помощь_Тема4_2'])
async def command_tema1(message : types.Message):
	await message.answer('Если ты затрудняешься ответить на этот вопрос, тебе стоит заглянуть в теорию', reply_markup=kb_tema42)

@dp.message_handler(commands=['Узнать_ответ_Тема4_2'])
async def command_tema1(message : types.Message):
	await message.answer('Для конвертации строк при помощи метода Parse используется следующая формула:\n\nstring имя_переменной1 = значение_переменной1;\nНазвание_типа_данных(в который хотим конвертировать) имя_переменной2 = название_типа_данных(в который хотим конвертировать).Parse(название_переменной1);");', reply_markup=kb_tema4)
	

	############ТЕСТ ПО ЧЕТВЕРТОЙ ТЕМЕ###############

@dp.message_handler(commands=['Тест4'])
async def command_test(message : types.Message):
	await message.answer('Браво!\nМы перешли к тесту, а это значит, что изучение четвертой темы подошло к концу и не за горами переход ко второй.Однако перед этим, давай посмотрим, чему же ты научился \nИтак, в тесте будет 2 вопроса,за правильный ответ на каждый из которых ты получаешь балл. Желаю успехов!\n\n   Вопрос №1:\n'
						f'Конвертация данных - это...\n\n1)сохранение данных в операционной системе\n2)преобразование данных из одногоформата в другой\n3)вывод данных на консоль',reply_markup=kb_test4_1)

@dp.message_handler(commands=['Ответ1','Ответ3'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз\n')

@dp.message_handler(commands=['Ответ2'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ!\nВопрос №2:\n'
						f'Какой формат будут иметь данные при вводе в консоль?', reply_markup=kb_test4_2)	
	
@dp.message_handler(commands=['byte','double'])
async def command_tema1(message : types.Message):
	await message.answer(f'Не верно!\nПопробуй еще раз')

@dp.message_handler(commands=['string'])
async def command_tema1(message : types.Message):
	await message.answer(f'Поздравляю! Это абсолютно правильный ответ\n\nЧетвертая тема успешно изучена,но помни, что всегда можешь вернуться обратно, если что-то забудешь. К сожалению, это последняя добавленная тема с функцией проверочных заданий, но ты можешь проверить обновления отправив мне команду /Обзор_новых_тем', reply_markup=kb_tema)

#обзор новых тем из базы данных, которые загрузил админ
@dp.message_handler(commands=['Обзор_новых_тем'])
async def new_tema_command(message: types.Message):
	for ret in cur.execute('SELECT*FROM info').fetchall():
		await bot.send_message(message.from_user.id,f'{ret[0]}\n\n{ret[1]}')
		
	#await sql_read(message)

#Действия при отправке пользователем не существующей команды
@dp.message_handler()
async def delete_message(message : types.Message):
	await message.answer('Такой команды не существует!\n Попробуй /start или /help')
	await message.delete()

executor.start_polling(dp,skip_updates=True, on_startup=on_startup)