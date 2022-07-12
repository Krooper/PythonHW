str_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbs=['0','1','2','3','4','5','6','7','8','9']
out_str=''
print('1)Исходный список:', str_list)
length=len(str_list)
i=0
while i < length-1:
  if any(numb in str_list[i+1] for numb in numbs) and str_list[i]!='\"' :
    str_list.insert(i+1, '\"')
    length+=1
  elif any(numb in str_list[i] for numb in numbs):
    str_list.insert(i+1, '\"')
    length+=1
  if any(numb in str_list[i] for numb in numbs) and len(str_list[i])<2:
    str_list.insert(i, '0'+str_list.pop(i))
  if str_list[i][0]=='+' and len(str_list[i])<3:
    str_list.insert(i, str_list.pop(i).replace('+','+0'))
  elif str_list[i][0]=='-' and len(str_list[i])<3:
    str_list.insert(i, str_list.pop(i).replace('-','-0'))
  i+=1

for i in range(len(str_list)):
  if str_list[i]=='\"' and any(numb in str_list[i+1] for numb in numbs) or any(numb in str_list[i] for numb in numbs):
    out_str+=str_list[i]
  else:
    out_str+=str_list[i]+' '
print('\t1.Новый список + добавление элементов-кавычек:', str_list)
print('\t2.Окончательная строка:', out_str)