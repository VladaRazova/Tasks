#Напишите программу, в которой на основе введенного пользователем текста создается новая текстовая строка.
#В этой строке по сравнению с исходной символы меняются местами «через один»: первый символ меняется местами с третьим, 
#четвертый символ меняется местами с шестым, седьмой меняется местами с девятым и так далее.
print('Добрый вечер')
txt=input('Введите текст: ')
list_word = txt.split()
replace_word1 = input('Меняем слово: ')
replace_word2 = input('Заменим на: ')
index_word = 0
if replace_word1 in list_word:
    index_word = list_word.index(replace_word1)
    list_word[index_word] = replace_word2  
new_string = ''
for l in list_word:
    new_string += l + " "
new_string = new_string.rstrip()
print(new_string)