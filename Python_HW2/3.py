workers_list=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(workers_list)):
  worker_name_letters_list=list(workers_list[i].split()[len(workers_list[i].split()  )-1])
  name_str=''
  for j in range (len(worker_name_letters_list)):
    if j==0:
      worker_name_letters_list[j]=worker_name_letters_list[j].upper()
      name_str+=worker_name_letters_list[j]
    else:
      worker_name_letters_list[j]=worker_name_letters_list[j].lower()
      name_str+=worker_name_letters_list[j]
    if j==len(worker_name_letters_list)-1:
      print('Привет,', name_str+'!')