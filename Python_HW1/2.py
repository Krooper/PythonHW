acc_sum=0
i_arr=[]
for i in range(1,1001,2):
  sum=0
  if i>=1:
    i_arr.append(i**3)
    degree=i**3
    degree_s=degree
    while degree_s>=1:
      sum+=degree_s%10
      degree_s=degree_s//10
    if sum%7==0:
      acc_sum+=+degree
      print(i,'^3 =',degree,'[',sum,'] накоп. сумма:',acc_sum)
print('Массив кубов:', i_arr)