import codecs 
import re
fi=codecs.open('final.csv', 'r', encoding='utf-8')
fi2=codecs.open('output.txt', 'w', encoding='utf-8')
fg=fi.read()
fi.close()
fg=fg.replace('\\"',"%QUOTES%")
fg=fg.replace("\\'","%SINGLEQUOTES%")
fg=fg.replace('","',"%colseparator%")
fg=fg.replace('"',"%lineseparator%")
fg=fg.split("%lineseparator%")
for record in fg:
	record2=record.split("%colseparator%")
	flag=0
	for index,j in enumerate(record2):
		if(index==6):
			temporary=j
			temporary1=temporary.split("\n")
			#print(temporary[1])
			fromembassy=temporary1[1]
			fmembassy0=fromembassy.split(" ")
			temporary2=temporary.split("\n")
			toembassy=temporary2[2]
			toembassy0=toembassy.split(" ")
			originembassy=fmembassy0[2]
			targetembassy=toembassy0[2]
			fi2.write(originembassy)
			fi2.write("--originembassy")
			#print(originembassy)
			#print("TEHRAN")
			if not(originembassy=="TEHRAN"):
				fi2.write("yayy   ")
			#print("------------------")
			if(originembassy=="TEHRAN"):
				print("++++++++++++")
				print(originembassy)

				if(targetembassy=='WASHDC'):
					print('hello')
				else:
					continue
fi2.close()
def calltofunction(record2):
	for index,j in enumerate(record2):
				if(index==1):#timestamp
					print('Timestamp:'+j)
				if(index==2):#id
					print('ID:'+j)
				elif(index==4):
					print('Classification:'+j)		#classification
				elif(index==7):
					project=j.split("SUBJECT:")
					for index2,project2 in enumerate(project):
						if(index2==1):	
							subjectheading=project2.split("\n")[0]			
							print('Subject:'+subjectheading)#subjectheading				
							data=project2
							print('Data:'+data)			#body