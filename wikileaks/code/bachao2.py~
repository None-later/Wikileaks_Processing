import codecs 
import re
fi=codecs.open('bd', 'r', encoding='utf-8')
fg=fi.read()
fi.close()
fg=fg.replace('\\"',"%QUOTES%")
fg=fg.replace("\\'","%SINGLEQUOTES%")
fg=fg.replace('","',"%colseparator%")
fg=fg.replace('"\r\n20"',"%lineseparator%")
fg=fg.split("#lineseparator#")
for recordindex,record in enumerate(fg):
	#print(str(recordindex)+record)
	if recordindex>=1:
		record2=record.split("%colseparator%")
		for index,j in enumerate(record2):
	#	print()"
		#print("helli")
#		output='output'+str(recordindex+2)
#		fi=codecs.open(output, 'w', encoding='utf-8')
#		fi.write(record)
#		fi.close
			if index==1:
				global time
				time=j
			if index==3:
				global name
				name=record2[index]
			if index==4:
				global classification
				classification=j
			if index==5:
				global _id
				_id=j
			if index==7:
				global body
				body=j
				body=body.replace("%SINGLEQUOTES%","\\'")
				body=body.replace("%QUOTES%",'\\"')
				body=body.replace("%colseparator%",'","')
				body=body.replace("\n",'')
				fi=codecs.open('/home/hp/Downloads/nlp_phase1/iitd_nlp/oct28/output_json/'+name, 'a+', encoding='utf-8')
				
#				fi.write('\n'+'"'+record+'"')
				strtoprint='{ "_id" : "'+_id+'", "origin" : "'+name+'", "date_time" : "'+time+'", "classification" : "'+classification+'", "body" : "'+body+'" }'+'\n'
				fi.write(strtoprint)
				fi.close
#			if index==3:
			#print(record)
			
#		if(index==6):
#			temporary=j
#			temporary1=temporary.split("\n")
#			fromembassy=temporary1[1]
#			fmembassy0=fromembassy.split(" ")
#			temporary2=temporary.split("\n")
#			toembassy=temporary2[2]
#			toembassy0=toembassy.split(" ")
#			originembassy=fmembassy0[2]
#			toembassy0=toembassy0[2]
#			targetembassy=toembassy0
#			output=originembassy+'2'+targetembassy
#			fi=codecs.open(output, 'a+', encoding='utf-8')
#			record=record.replace("%SINGLEQUOTES%","\\'")
#			record=record.replace("%QUOTES%",'\\"')
#			record=record.replace("%colseparator%",'","')
#			fi.write('\n'+'"'+record+'"')
#			fi.close
#			print('from'+originembassy)
#			print('target'+targetembassy)

