import codecs 
import re
import unicodedata
#for_a=['q','r','s','t','u','v','w','x','y','z']
##['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
#for l in for_a:
for_b=['a','b','c','d']
for l in for_b:
	fi=codecs.open('b'+l, 'r', encoding='utf-8')
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
					body=body.replace("\\'","'")
					body=body.replace('\\"','"')
					#print(time)
					time2=time
					time2=time2.split(" ")[0]
					time2=time2.split("/")[2]
					time_var=time
					time_var=time_var.split(" ")[0]
					time_var=time_var.split("/")[0]
#					time_month=time2.split("/")[0]
					#print(time2)
	#				print(type(time2))
					time2=int(time2)
					time_month=int(time_var)
#					print(time_month)
					if (time2 >= 1966 and time2 < 1980):
							fi=codecs.open('bodyonly66_80/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
							strtoprint=body+'\n'
							fi.write(strtoprint)
							fi.close
					elif((time2 >= 1980 and time2 < 1990)):
						fi=codecs.open('bodyonly80_90/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 1990 and time2 < 1995)):
						fi=codecs.open('bodyonly90_95/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 1995 and time2 < 2000)):
						fi=codecs.open('bodyonly95_00/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2000 and time2 < 2001)):
						fi=codecs.open('bodyonly00_01/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2001 and time2 < 2002)):
						fi=codecs.open('bodyonly01_02/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2002 and time2 < 2003)):
						fi=codecs.open('bodyonly02_03/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2003 and time2 < 2004)):
						fi=codecs.open('bodyonly03_04/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2004 and time2 < 2005)):
						fi=codecs.open('bodyonly04_05/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2005 and time2 < 2006)):
						fi=codecs.open('bodyonly05_06/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==1)):
						fi=codecs.open('bodyonly06_07_1/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==2)):
						fi=codecs.open('bodyonly06_07_2/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==3)):
						fi=codecs.open('bodyonly06_07_3/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==4)):
						fi=codecs.open('bodyonly06_07_4/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==5)):
						fi=codecs.open('bodyonly06_07_5/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close	
					elif((time2 >= 2006 and time2 < 2007 and time_month==6)):
						fi=codecs.open('bodyonly06_07_6/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==7)):
						fi=codecs.open('bodyonly06_07_7/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==8)):
						fi=codecs.open('bodyonly06_07_8/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==9)):
						fi=codecs.open('bodyonly06_07_9/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==10)):
						fi=codecs.open('bodyonly06_07_10/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==11)):
						fi=codecs.open('bodyonly06_07_11/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2006 and time2 < 2007 and time_month==12)):
						fi=codecs.open('bodyonly06_07_12/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					
					elif((time2 >= 2007 and time2 < 2008 and time_month==1)):
						fi=codecs.open('bodyonly07_08_1/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==2)):
						fi=codecs.open('bodyonly07_08_2/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==3)):
						fi=codecs.open('bodyonly07_08_3/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==4)):
						fi=codecs.open('bodyonly07_08_4/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==5)):
						fi=codecs.open('bodyonly07_08_5/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close	
					elif((time2 >= 2007 and time2 < 2008 and time_month==6)):
						fi=codecs.open('bodyonly07_08_6/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==7)):
						fi=codecs.open('bodyonly07_08_7/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==8)):
						fi=codecs.open('bodyonly07_08_8/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==9)):
						fi=codecs.open('bodyonly07_08_9/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==10)):
						fi=codecs.open('bodyonly07_08_10/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==11)):
						fi=codecs.open('bodyonly07_08_11/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2007 and time2 < 2008 and time_month==12)):
						fi=codecs.open('bodyonly07_08_12/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close

					elif((time2 >= 2008 and time2 < 2009 and time_month==1)):
						fi=codecs.open('bodyonly08_09_1/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==2)):
						fi=codecs.open('bodyonly08_09_2/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==3)):
						fi=codecs.open('bodyonly08_09_3/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==4)):
						fi=codecs.open('bodyonly08_09_4/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==5)):
						fi=codecs.open('bodyonly08_09_5/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close	
					elif((time2 >= 2008 and time2 < 2009 and time_month==6)):
						fi=codecs.open('bodyonly08_09_6/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==7)):
						fi=codecs.open('bodyonly08_09_7/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==8)):
						fi=codecs.open('bodyonly08_09_8/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==9)):
						fi=codecs.open('bodyonly08_09_9/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==10)):
						fi=codecs.open('bodyonly08_09_10/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==11)):
						fi=codecs.open('bodyonly08_09_11/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2008 and time2 < 2009 and time_month==12)):
						fi=codecs.open('bodyonly08_09_12/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==1)):
						fi=codecs.open('bodyonly09_10_1/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==2)):
						fi=codecs.open('bodyonly09_10_2/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==3)):
						fi=codecs.open('bodyonly09_10_3/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==4)):
						fi=codecs.open('bodyonly09_10_4/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==5)):
						fi=codecs.open('bodyonly09_10_5/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close	
					elif((time2 >= 2009 and time2 <  2010 and time_month==6)):
						fi=codecs.open('bodyonly09_10_6/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==7)):
						fi=codecs.open('bodyonly09_10_7/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==8)):
						fi=codecs.open('bodyonly09_10_8/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==9)):
						fi=codecs.open('bodyonly09_10_9/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==10)):
						fi=codecs.open('bodyonly09_10_10/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==11)):
						fi=codecs.open('bodyonly09_10_11/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
					elif((time2 >= 2009 and time2 <  2010 and time_month==12)):
						fi=codecs.open('bodyonly09_10_12/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
						fi.write(strtoprint)
						fi.close
				
					elif(time2 >= 2010):
						fi=codecs.open('bodyonly10onwards/'+name, 'a+', encoding='utf-8')
				
	#				fi.write('\n'+'"'+record+'"')
						strtoprint=body+'\n'
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

