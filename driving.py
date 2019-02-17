country = input('請問您是哪國人:')
age = input('請問您幾歲:')
if country == "台灣" or country == "韓國" or country == "新加坡":
	if int(age) >= 18:
		print('您可以開車')
	else:
		print('你不能開車')
elif country == "美國" or  country == "加拿大" or  country == "日本" or  country == "英國":
	if int(age) >= 16:
		print('您可以開車')
	else:
		print('您不能開車')
elif country == "泰國":
	if int(age) >= 15:
		print('您可以開車')
	else:
		print('您不能開車')
else:
	print('您只能輸入台灣/韓國/美國/日本/泰國/加拿大/英國/新加坡')