#�������� ���������, � ������� �� ������ ���������� ������������� ������ ��������� ����� ��������� ������.
#� ���� ������ �� ��������� � �������� ������� �������� ������� ������ ����: ������ ������ �������� ������� � �������, 
#��������� ������ �������� ������� � ������, ������� �������� ������� � ������� � ��� �����.
print('������ �����')
txt=input('������� �����: ')
list_word = txt.split()
replace_word1 = input('������ �����: ')
replace_word2 = input('������� ��: ')
index_word = 0
if replace_word1 in list_word:
    index_word = list_word.index(replace_word1)
    list_word[index_word] = replace_word2  
new_string = ''
for l in list_word:
    new_string += l + " "
new_string = new_string.rstrip()
print(new_string)