for percent in range(1,101):
  if percent%10==1 and percent!=11:
    declension='процент'
  elif percent%10>=2 and percent%10<=4 and (percent<10 or percent>20):
    declension='процента'
  #elif percent==0 or (percent%10>=5 and percent%10<=9):
    #declension='процентов'
  else:
    declension='процентов'
  print (percent,declension)