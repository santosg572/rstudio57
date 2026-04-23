from deep_translator import GoogleTranslator

#file = 'The_R_Base_Package'

import sys

file = sys.argv[1]

fil = open(file+'.txt', 'r')
filo = open(file+'_2.txt', 'w')

datos = fil.readlines()

for ss in datos:
  ss = ss.replace('\n','')
  i = ss.find("\t")  
  if i>1:
    ss2 = ss[0:i]
    ss3 = ss[i:]
    translated = GoogleTranslator(source='en', target='es').translate(ss3)
    ss4 = ss2 + ' - ' + translated
    print(ss4)
    filo.write(ss4+'\n')

filo.close()



