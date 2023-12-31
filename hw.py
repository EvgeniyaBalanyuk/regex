import re
from pprint import pprint
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# Тестирование работы регулярного выражения
text = 'lastname,firstname,surname,organization,position,phone,email Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037, Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168, Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,  Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792), Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru'
pattern = r'(\+7|8)\s*?\(?(\d{3})\)?[-\s]?(\d{3})-?(\d{2})-?(\d{2})\s?\(?[доб.\s]*(\d{4})?\)?'
result = re.findall(pattern, text)
print(result)
# Тестирование замены номеров
rename = '+7(\2)\3-\4-\5 доб.\6'
result_sub = re.sub(pattern, rename, text)
pprint(result_sub)
