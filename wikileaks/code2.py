import codecs
import re
fi=codecs.open('final.csv', 'r', encoding='utf-8')
fg=fi.read()
fi.close()
strs=fg.replace('\"[0-9]*',"lineseparator")
print(strs)
