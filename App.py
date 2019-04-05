
import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
	print(words) # Дополнительно выводим на экран
	os.system("say " + words) # Проговариваем слова


talk("Привет, чем я могу помочь вам?")


def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1

		r.adjust_for_ambient_noise(source, duration=1)

		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений

		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:

		talk("Я вас не поняла")
		zadanie = command()


	return zadanie


def makeSomething(zadanie):

	if 'открыть сайт' in zadanie:
		# Проговариваем текст
		talk("Уже открываю")
		# Указываем сайт для открытия
		url = 'https://vk.com/id70445358'
		# Открываем сайт
		webbrowser.open(url)
	# если было сказано "стоп", то останавливаем прогу
	elif 'стоп' in zadanie:

		talk("Да, конечно, без проблем")
		# Выходим из программы
		sys.exit()

	elif 'имя' in zadanie:
		talk("Меня зовут Сири")


while True:
	makeSomething(command())