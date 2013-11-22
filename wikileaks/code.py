import codecs
#fi=codecs.open('temp.csv','r')
fi=codecs.open('nlp_3.csv', 'r', encoding='utf-8')
fg=fi.read()
fi.close()
#print fg
temp2=fg.split("lineseparator")
#print(temp2[2])
tempo=temp2[2]
tempo=tempo.split("%colseparator%")
print(tempo[1])
