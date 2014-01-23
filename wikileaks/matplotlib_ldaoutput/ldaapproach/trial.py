#import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import nltk
import os
import glob
import pylab
import codecs
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }
embassies=[]
yearlist=['00_01','01_02','02_03','03_04','04_05','05_06','06_07_1','06_07_2','06_07_3','06_07_4','06_07_5','06_07_6','06_07_7','06_07_8','06_07_9','06_07_10','06_07_11','06_07_12','08_09_1','08_09_2','08_09_3','08_09_4','08_09_5','08_09_6','08_09_7','08_09_8','08_09_9','08_09_10','08_09_11','08_09_12','07_08_1','07_08_2','07_08_3','07_08_4','07_08_5','07_08_6','07_08_7','07_08_8','07_08_9','07_08_10','07_08_11','07_08_12','09_10_1','09_10_2','09_10_3','09_10_4','09_10_5','09_10_6','09_10_7','09_10_8','09_10_9','09_10_10','09_10_11','09_10_12']
for year in yearlist:
	for files in glob.glob("result"+year+"/"+"*"):
		nameoffiles=files
		nameoffiles=nameoffiles.replace("result"+year+"/","")
		if nameoffiles not in embassies:
			embassies.append(nameoffiles)
for i in embassies:
#	i=i.replace(" ","")
#	print 'y_'+i+'=[]'
	print i

