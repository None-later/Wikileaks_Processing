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
embassies=['EmbassyLondon','EmbassyBeirut','EmbassyPretoria','EmbassyAthens','EmbassyTashkent','EmbassyRiyadh','EmbassyDamascus','EmbassyBucharest','EmbassyAbuDhabi','EmbassyAnkara','ConsulateHoChiMinhCity','EmbassyJakarta','EmbassyTheHague','EmbassyBandarSeriBegawan','EmbassyKinshasa','EmbassyHarare','EmbassyRabat','EmbassyLima','EmbassyTelAviv','EmbassyHelsinki','EmbassyHanoi','EmbassyBogota','EmbassyGaborone','EmbassyColombo','EmbassyBeijing','EmbassyUlaanbaatar','SecretaryofState','EmbassySanaa','USInterestsSectionHavana','ConsulateDubai','EmbassyCairo','EmbassyLusaka','EmbassyManila','EmbassyDoha','EmbassyTunis','EmbassyVatican','EmbassyCaracas','EmbassyAshgabat','EmbassyDakar','EmbassyBanjul','EmbassyLibreville','EmbassyLilongwe','EmbassyParis','EmbassyPhnomPenh','EmbassyRangoon','EmbassyIslamabad','EmbassyAbuja','EmbassyDjibouti','EmbassyPrague','EmbassyKuwait','EmbassyAccra','EmbassySofia','EmbassyKualaLumpur','EmbassyManama','EmbassyPristina','EmbassyKhartoum','EmbassyAddisAbaba','ConsulateLagos','EmbassyAmman','ConsulateMilan','ConsulateAdana','EmbassyAlgiers','EmbassyRome','ConsulateFrankfurt','ConsulateIstanbul','EmbassyMaputo','EmbassyMadrid','EmbassyMuscat','EmbassyBrasilia','EmbassyTegucigalpa','EmbassyKathmandu','ConsulateJerusalem','EmbassySingapore','ConsulateHalifax','EmbassyZagreb','EmbassyYerevan','USDelegation,Secretary','EmbassyBelgrade','EmbassyBuenosAires','ConsulateJeddah','EmbassyBrussels','USUNNewYork','EmbassyKabul','EmbassyOttawa','EmbassySantiago','EmbassyKampala','EmbassySantoDomingo','ConsulateMontreal','EmbassyNassau','ConsulateVancouver','EmbassyMbabane','USEUBrussels','EmbassyGuatemala','EmbassySeoul','EmbassyDushanbe','EmbassyBangkok','EmbassyNewDelhi','EmbassyAsuncion','EmbassyMaseru','ConsulateChennai','EmbassyLaPaz','EmbassyTripoli','EmbassyParamaribo','EmbassyBerlin','EmbassyWellington','ConsulateKolkata','EmbassyBratislava','EmbassyManagua','ConsulateGuayaquil','EmbassyDhaka','ConsulateSaoPaulo','EmbassyKigali','EmbassyVilnius','EmbassyLjubljana','EmbassyBaghdad','EmbassyDublin','ConsulateRioDeJaneiro','EmbassySanJose','ConsulateQuebec','EmbassyPanama','ConsulateMumbai','EmbassyAsmara','EmbassyQuito','EmbassyPortAuPrince','EmbassyMoscow','AmericanInstituteTaiwan,Taipei','ConsulateCalgary','EmbassyTokyo','MissionGeneva','MissionUSNATO','EmbassyVienna','EmbassyTbilisi','ConsulateToronto','ConsulateRecife','ConsulateHongKong','ConsulateChiangMai','REOKirkuk','ConsulateAuckland','ConsulateMarseille','EmbassyCopenhagen','REOHillah','ConsulateHermosillo','EmbassyNicosia','EmbassyKingston','EmbassySanSalvador','EmbassyDili','EmbassyNouakchott','EmbassyWarsaw','EmbassyMexico','USOfficeAlmaty','EmbassyBern','EmbassyKyiv','ConsulateThessaloniki','EmbassyNdjamena','EmbassyGeorgetown','EmbassyDarEsSalaam','EmbassyMinsk','EmbassyNairobi','REOBasrah','USMissionGeneva','EmbassyCanberra','EmbassyAbidjan','EmbassyReykjavik','ConsulateCasablanca','EmbassyOslo','EmbassyFreetown','EmbassyMontevideo','EmbassyStockholm','EmbassyConakry','EmbassyBridgetown','ConsulatePeshawar','REOMosul','EmbassySkopje','EmbassyBelmopan','ConsulateFlorence','ConsulateCuracao','EmbassyPortOfSpain','EmbassyBaku','ConsulateOsakaKobe','ConsulateFukuoka','EmbassySuva','EmbassyWindhoek','ConsulateAmsterdam','ConsulateMunich','ConsulateGuangzhou','EmbassyLuanda','EmbassyAntananarivo','ConsulateNaples','EmbassyPortMoresby','EmbassyBudapest','EmbassyLome','EmbassyTallinn','EmbassySarajevo','ConsulateLahore','ConsulateNaha','MissionUSOSCE','EmbassyVientiane','EmbassyRiga','EmbassyAstana','EmbassyBishkek','ConsulateJohannesburg','EmbassyTirana','EmbassyBamako','EmbassyPortLouis','EmbassyNiamey','EmbassyYaounde','EmbassyLisbon','ConsulateDusseldorf','EmbassyBujumbura','ConsulateMelbourne','EmbassyLuxembourg','EmbassyCotonou','UNVIE','EmbassyOuagadougou','ConsulateShanghai','EmbassyBangui','EmbassyPodgorica','ConsulateBarcelona','IranRPODubai','ConsulateKrakow','ConsulateHamburg','ConsulateChengdu','EmbassyMonrovia','EmbassyChisinau','ConsulateMonterrey','EmbassyGrenada','ConsulateGuadalajara','EmbassyKolonia','ConsulateVladivostok','ConsulateShenyang','ConsulateSurabaya','ConsulateKarachi','USDelegationFESTTWO','EmbassyKoror','EmbassyValletta','ConsulateCapeTown','ConsulateNagoya','EmbassyPraia','ConsulateSapporo','ConsulateDurban','MissionUNESCO','ConsulateTijuana','EmbassyBrazzaville','EmbassyApia','ConsulateStPetersburg','EmbassyMajuro','ConsulateMatamoros','USOFFICEFSCCHARLESTON','ConsulateMerida','ConsulateBelfast','ConsulateYekaterinburg','ConsulateCiudadJuarez','ConsulateLeipzig','ConsulateSydney','EmbassyMalabo','ConsulateNogales','ConsulatePontaDelgada','ConsulateNuevoLaredo','ConsulateStrasbourg','ConsulatePerth','**Dhahran','UNRome','ConsulateDhahran','AmericanConsulateHyderabad','DIRFSINFATC','ConsulateHamilton']
yearlist2=['00_01','01_02','02_03','03_04','04_05','05_06','06_07_1','06_07_2','06_07_3','06_07_4','06_07_5','06_07_6','06_07_7','06_07_8','06_07_9','06_07_10','06_07_11','06_07_12','08_09_1','08_09_2','08_09_3','08_09_4','08_09_5','08_09_6','08_09_7','08_09_8','08_09_9','08_09_10','08_09_11','08_09_12','07_08_1','07_08_2','07_08_3','07_08_4','07_08_5','07_08_6','07_08_7','07_08_8','07_08_9','07_08_10','07_08_11','07_08_12','09_10_1','09_10_2','09_10_3','09_10_4','09_10_5','09_10_6','09_10_7','09_10_8','09_10_9','09_10_10','09_10_11','09_10_12']
x_EmbassyLondon=[]
x_EmbassyBeirut=[]
x_EmbassyPretoria=[]
x_EmbassyAthens=[]
x_EmbassyTashkent=[]
x_EmbassyRiyadh=[]
x_EmbassyDamascus=[]
x_EmbassyBucharest=[]
x_EmbassyAbuDhabi=[]
x_EmbassyAnkara=[]
x_ConsulateHoChiMinhCity=[]
x_EmbassyJakarta=[]
x_EmbassyTheHague=[]
x_EmbassyBandarSeriBegawan=[]
x_EmbassyKinshasa=[]
x_EmbassyHarare=[]
x_EmbassyRabat=[]
x_EmbassyLima=[]
x_EmbassyTelAviv=[]
x_EmbassyHelsinki=[]
x_EmbassyHanoi=[]
x_EmbassyBogota=[]
x_EmbassyGaborone=[]
x_EmbassyColombo=[]
x_EmbassyBeijing=[]
x_EmbassyUlaanbaatar=[]
x_SecretaryofState=[]
x_EmbassySanaa=[]
x_USInterestsSectionHavana=[]
x_ConsulateDubai=[]
x_EmbassyCairo=[]
x_EmbassyLusaka=[]
x_EmbassyManila=[]
x_EmbassyDoha=[]
x_EmbassyTunis=[]
x_EmbassyVatican=[]
x_EmbassyCaracas=[]
x_EmbassyAshgabat=[]
x_EmbassyDakar=[]
x_EmbassyBanjul=[]
x_EmbassyLibreville=[]
x_EmbassyLilongwe=[]
x_EmbassyParis=[]
x_EmbassyPhnomPenh=[]
x_EmbassyRangoon=[]
x_EmbassyIslamabad=[]
x_EmbassyAbuja=[]
x_EmbassyDjibouti=[]
x_EmbassyPrague=[]
x_EmbassyKuwait=[]
x_EmbassyAccra=[]
x_EmbassySofia=[]
x_EmbassyKualaLumpur=[]
x_EmbassyManama=[]
x_EmbassyPristina=[]
x_EmbassyKhartoum=[]
x_EmbassyAddisAbaba=[]
x_ConsulateLagos=[]
x_EmbassyAmman=[]
x_ConsulateMilan=[]
x_ConsulateAdana=[]
x_EmbassyAlgiers=[]
x_EmbassyRome=[]
x_ConsulateFrankfurt=[]
x_ConsulateIstanbul=[]
x_EmbassyMaputo=[]
x_EmbassyMadrid=[]
x_EmbassyMuscat=[]
x_EmbassyBrasilia=[]
x_EmbassyTegucigalpa=[]
x_EmbassyKathmandu=[]
x_ConsulateJerusalem=[]
x_EmbassySingapore=[]
x_ConsulateHalifax=[]
x_EmbassyZagreb=[]
x_EmbassyYerevan=[]
x_USDelegation=[]
x_Secretary=[]
x_EmbassyBelgrade=[]
x_EmbassyBuenosAires=[]
x_ConsulateJeddah=[]
x_EmbassyBrussels=[]
x_USUNNewYork=[]
x_EmbassyKabul=[]
x_EmbassyOttawa=[]
x_EmbassySantiago=[]
x_EmbassyKampala=[]
x_EmbassySantoDomingo=[]
x_ConsulateMontreal=[]
x_EmbassyNassau=[]
x_ConsulateVancouver=[]
x_EmbassyMbabane=[]
x_USEUBrussels=[]
x_EmbassyGuatemala=[]
x_EmbassySeoul=[]
x_EmbassyDushanbe=[]
x_EmbassyBangkok=[]
x_EmbassyNewDelhi=[]
x_EmbassyAsuncion=[]
x_EmbassyMaseru=[]
x_ConsulateChennai=[]
x_EmbassyLaPaz=[]
x_EmbassyTripoli=[]
x_EmbassyParamaribo=[]
x_EmbassyBerlin=[]
x_EmbassyWellington=[]
x_ConsulateKolkata=[]
x_EmbassyBratislava=[]
x_EmbassyManagua=[]
x_ConsulateGuayaquil=[]
x_EmbassyDhaka=[]
x_ConsulateSaoPaulo=[]
x_EmbassyKigali=[]
x_EmbassyVilnius=[]
x_EmbassyLjubljana=[]
x_EmbassyBaghdad=[]
x_EmbassyDublin=[]
x_ConsulateRioDeJaneiro=[]
x_EmbassySanJose=[]
x_ConsulateQuebec=[]
x_EmbassyPanama=[]
x_ConsulateMumbai=[]
x_EmbassyAsmara=[]
x_EmbassyQuito=[]
x_EmbassyPortAuPrince=[]
x_EmbassyMoscow=[]
x_AmericanInstituteTaiwan=[]
x_Taipei=[]
x_MissionGeneva=[]
x_ConsulateToronto=[]
x_ConsulateRecife=[]
x_ConsulateHongKong=[]
x_EmbassyCopenhagen=[]
x_EmbassySanSalvador=[]
x_EmbassyNouakchott=[]
x_USOfficeAlmaty=[]
x_EmbassyBern=[]
x_EmbassyKyiv=[]
x_EmbassyNdjamena=[]
x_EmbassyNairobi=[]
x_EmbassyCanberra=[]
x_EmbassyAbidjan=[]
x_EmbassyTokyo=[]
x_EmbassyOslo=[]
x_EmbassyFreetown=[]
x_EmbassyVienna=[]
x_EmbassyMontevideo=[]
x_ConsulateChiangMai=[]
x_EmbassyStockholm=[]
x_EmbassyConakry=[]
x_EmbassyBridgetown=[]
x_REOKirkuk=[]
x_ConsulateAuckland=[]
x_ConsulatePeshawar=[]
x_REOMosul=[]
x_REOHillah=[]
x_ConsulateHermosillo=[]
x_EmbassyNicosia=[]
x_EmbassyKingston=[]
x_EmbassySkopje=[]
x_EmbassyDili=[]
x_EmbassyWarsaw=[]
x_EmbassyMexico=[]
x_EmbassyBelmopan=[]
x_ConsulateFlorence=[]
x_EmbassyGeorgetown=[]
x_ConsulateCuracao=[]
x_EmbassyDarEsSalaam=[]
x_EmbassyMinsk=[]
x_REOBasrah=[]
x_EmbassyReykjavik=[]
x_ConsulateCasablanca=[]
x_EmbassyPortOfSpain=[]
x_EmbassyBaku=[]
x_ConsulateOsakaKobe=[]
x_ConsulateFukuoka=[]
x_EmbassySuva=[]
x_EmbassyWindhoek=[]
x_ConsulateAmsterdam=[]
x_ConsulateMunich=[]
x_ConsulateGuangzhou=[]
x_EmbassyLuanda=[]
x_EmbassyAntananarivo=[]
x_ConsulateNaples=[]
x_EmbassyPortMoresby=[]
x_EmbassyBudapest=[]
x_EmbassyLome=[]
x_EmbassyTallinn=[]
x_EmbassySarajevo=[]
x_ConsulateLahore=[]
x_ConsulateNaha=[]
x_MissionUSOSCE=[]
x_EmbassyVientiane=[]
x_EmbassyRiga=[]
x_EmbassyAstana=[]
x_EmbassyBishkek=[]
x_USMissionGeneva=[]
x_ConsulateJohannesburg=[]
x_EmbassyTirana=[]
x_EmbassyBamako=[]
x_EmbassyPortLouis=[]
x_EmbassyNiamey=[]
x_EmbassyYaounde=[]
x_EmbassyLisbon=[]
x_ConsulateDusseldorf=[]
x_EmbassyBujumbura=[]
x_ConsulateMelbourne=[]
x_EmbassyLuxembourg=[]
x_EmbassyCotonou=[]
x_UNVIE=[]
x_EmbassyOuagadougou=[]
x_MissionUSNATO=[]
x_EmbassyTbilisi=[]
x_ConsulateShanghai=[]
x_EmbassyBangui=[]
x_EmbassyPodgorica=[]
x_ConsulateBarcelona=[]
x_IranRPODubai=[]
x_ConsulateKrakow=[]
x_ConsulateHamburg=[]
x_ConsulateChengdu=[]
x_EmbassyMonrovia=[]
x_EmbassyChisinau=[]
x_ConsulateMonterrey=[]
x_EmbassyGrenada=[]
x_ConsulateThessaloniki=[]
x_ConsulateGuadalajara=[]
x_EmbassyKolonia=[]
x_ConsulateVladivostok=[]
x_ConsulateShenyang=[]
x_ConsulateSurabaya=[]
x_ConsulateKarachi=[]
x_USDelegationFESTTWO=[]
x_EmbassyKoror=[]
x_EmbassyValletta=[]
x_ConsulateCapeTown=[]
x_ConsulateNagoya=[]
x_EmbassyPraia=[]
x_ConsulateSapporo=[]
x_ConsulateDurban=[]
x_MissionUNESCO=[]
x_ConsulateTijuana=[]
x_EmbassyBrazzaville=[]
x_EmbassyApia=[]
x_ConsulateStPetersburg=[]
x_EmbassyMajuro=[]
x_ConsulateMatamoros=[]
x_USOFFICEFSCCHARLESTON=[]
x_ConsulateMerida=[]
x_ConsulateBelfast=[]
x_ConsulateYekaterinburg=[]
x_ConsulateCiudadJuarez=[]
x_ConsulateLeipzig=[]
x_ConsulateSydney=[]
x_EmbassyMalabo=[]
x_ConsulateCalgary=[]
x_ConsulateMarseille=[]
x_ConsulateNogales=[]
x_ConsulatePontaDelgada=[]
x_ConsulateNuevoLaredo=[]
x_ConsulateStrasbourg=[]
x_ConsulatePerth=[]
x_Dhahran=[]
x_UNRome=[]
x_ConsulateDhahran=[]
x_AmericanConsulateHyderabad=[]
x_DIRFSINFATC=[]
x_ConsulateHamilton=[]
y_EmbassyLondon=[]
y_EmbassyBeirut=[]
y_EmbassyPretoria=[]
y_EmbassyAthens=[]
y_EmbassyTashkent=[]
y_EmbassyRiyadh=[]
y_EmbassyDamascus=[]
y_EmbassyBucharest=[]
y_EmbassyAbuDhabi=[]
y_EmbassyAnkara=[]
y_ConsulateHoChiMinhCity=[]
y_EmbassyJakarta=[]
y_EmbassyTheHague=[]
y_EmbassyBandarSeriBegawan=[]
y_EmbassyKinshasa=[]
y_EmbassyHarare=[]
y_EmbassyRabat=[]
y_EmbassyLima=[]
y_EmbassyTelAviv=[]
y_EmbassyHelsinki=[]
y_EmbassyHanoi=[]
y_EmbassyBogota=[]
y_EmbassyGaborone=[]
y_EmbassyColombo=[]
y_EmbassyBeijing=[]
y_EmbassyUlaanbaatar=[]
y_SecretaryofState=[]
y_EmbassySanaa=[]
y_USInterestsSectionHavana=[]
y_ConsulateDubai=[]
y_EmbassyCairo=[]
y_EmbassyLusaka=[]
y_EmbassyManila=[]
y_EmbassyDoha=[]
y_EmbassyTunis=[]
y_EmbassyVatican=[]
y_EmbassyCaracas=[]
y_EmbassyAshgabat=[]
y_EmbassyDakar=[]
y_EmbassyBanjul=[]
y_EmbassyLibreville=[]
y_EmbassyLilongwe=[]
y_EmbassyParis=[]
y_EmbassyPhnomPenh=[]
y_EmbassyRangoon=[]
y_EmbassyIslamabad=[]
y_EmbassyAbuja=[]
y_EmbassyDjibouti=[]
y_EmbassyPrague=[]
y_EmbassyKuwait=[]
y_EmbassyAccra=[]
y_EmbassySofia=[]
y_EmbassyKualaLumpur=[]
y_EmbassyManama=[]
y_EmbassyPristina=[]
y_EmbassyKhartoum=[]
y_EmbassyAddisAbaba=[]
y_ConsulateLagos=[]
y_EmbassyAmman=[]
y_ConsulateMilan=[]
y_ConsulateAdana=[]
y_EmbassyAlgiers=[]
y_EmbassyRome=[]
y_ConsulateFrankfurt=[]
y_ConsulateIstanbul=[]
y_EmbassyMaputo=[]
y_EmbassyMadrid=[]
y_EmbassyMuscat=[]
y_EmbassyBrasilia=[]
y_EmbassyTegucigalpa=[]
y_EmbassyKathmandu=[]
y_ConsulateJerusalem=[]
y_EmbassySingapore=[]
y_ConsulateHalifax=[]
y_EmbassyZagreb=[]
y_EmbassyYerevan=[]
y_USDelegation=[]
y_Secretary=[]
y_EmbassyBelgrade=[]
y_EmbassyBuenosAires=[]
y_ConsulateJeddah=[]
y_EmbassyBrussels=[]
y_USUNNewYork=[]
y_EmbassyKabul=[]
y_EmbassyOttawa=[]
y_EmbassySantiago=[]
y_EmbassyKampala=[]
y_EmbassySantoDomingo=[]
y_ConsulateMontreal=[]
y_EmbassyNassau=[]
y_ConsulateVancouver=[]
y_EmbassyMbabane=[]
y_USEUBrussels=[]
y_EmbassyGuatemala=[]
y_EmbassySeoul=[]
y_EmbassyDushanbe=[]
y_EmbassyBangkok=[]
y_EmbassyNewDelhi=[]
y_EmbassyAsuncion=[]
y_EmbassyMaseru=[]
y_ConsulateChennai=[]
y_EmbassyLaPaz=[]
y_EmbassyTripoli=[]
y_EmbassyParamaribo=[]
y_EmbassyBerlin=[]
y_EmbassyWellington=[]
y_ConsulateKolkata=[]
y_EmbassyBratislava=[]
y_EmbassyManagua=[]
y_ConsulateGuayaquil=[]
y_EmbassyDhaka=[]
y_ConsulateSaoPaulo=[]
y_EmbassyKigali=[]
y_EmbassyVilnius=[]
y_EmbassyLjubljana=[]
y_EmbassyBaghdad=[]
y_EmbassyDublin=[]
y_ConsulateRioDeJaneiro=[]
y_EmbassySanJose=[]
y_ConsulateQuebec=[]
y_EmbassyPanama=[]
y_ConsulateMumbai=[]
y_EmbassyAsmara=[]
y_EmbassyQuito=[]
y_EmbassyPortAuPrince=[]
y_EmbassyMoscow=[]
y_AmericanInstituteTaiwan=[]
y_Taipei=[]
y_MissionGeneva=[]
y_ConsulateToronto=[]
y_ConsulateRecife=[]
y_ConsulateHongKong=[]
y_EmbassyCopenhagen=[]
y_EmbassySanSalvador=[]
y_EmbassyNouakchott=[]
y_USOfficeAlmaty=[]
y_EmbassyBern=[]
y_EmbassyKyiv=[]
y_EmbassyNdjamena=[]
y_EmbassyNairobi=[]
y_EmbassyCanberra=[]
y_EmbassyAbidjan=[]
y_EmbassyTokyo=[]
y_EmbassyOslo=[]
y_EmbassyFreetown=[]
y_EmbassyVienna=[]
y_EmbassyMontevideo=[]
y_ConsulateChiangMai=[]
y_EmbassyStockholm=[]
y_EmbassyConakry=[]
y_EmbassyBridgetown=[]
y_REOKirkuk=[]
y_ConsulateAuckland=[]
y_ConsulatePeshawar=[]
y_REOMosul=[]
y_REOHillah=[]
y_ConsulateHermosillo=[]
y_EmbassyNicosia=[]
y_EmbassyKingston=[]
y_EmbassySkopje=[]
y_EmbassyDili=[]
y_EmbassyWarsaw=[]
y_EmbassyMexico=[]
y_EmbassyBelmopan=[]
y_ConsulateFlorence=[]
y_EmbassyGeorgetown=[]
y_ConsulateCuracao=[]
y_EmbassyDarEsSalaam=[]
y_EmbassyMinsk=[]
y_REOBasrah=[]
y_EmbassyReykjavik=[]
y_ConsulateCasablanca=[]
y_EmbassyPortOfSpain=[]
y_EmbassyBaku=[]
y_ConsulateOsakaKobe=[]
y_ConsulateFukuoka=[]
y_EmbassySuva=[]
y_EmbassyWindhoek=[]
y_ConsulateAmsterdam=[]
y_ConsulateMunich=[]
y_ConsulateGuangzhou=[]
y_EmbassyLuanda=[]
y_EmbassyAntananarivo=[]
y_ConsulateNaples=[]
y_EmbassyPortMoresby=[]
y_EmbassyBudapest=[]
y_EmbassyLome=[]
y_EmbassyTallinn=[]
y_EmbassySarajevo=[]
y_ConsulateLahore=[]
y_ConsulateNaha=[]
y_MissionUSOSCE=[]
y_EmbassyVientiane=[]
y_EmbassyRiga=[]
y_EmbassyAstana=[]
y_EmbassyBishkek=[]
y_USMissionGeneva=[]
y_ConsulateJohannesburg=[]
y_EmbassyTirana=[]
y_EmbassyBamako=[]
y_EmbassyPortLouis=[]
y_EmbassyNiamey=[]
y_EmbassyYaounde=[]
y_EmbassyLisbon=[]
y_ConsulateDusseldorf=[]
y_EmbassyBujumbura=[]
y_ConsulateMelbourne=[]
y_EmbassyLuxembourg=[]
y_EmbassyCotonou=[]
y_UNVIE=[]
y_EmbassyOuagadougou=[]
y_MissionUSNATO=[]
y_EmbassyTbilisi=[]
y_ConsulateShanghai=[]
y_EmbassyBangui=[]
y_EmbassyPodgorica=[]
y_ConsulateBarcelona=[]
y_IranRPODubai=[]
y_ConsulateKrakow=[]
y_ConsulateHamburg=[]
y_ConsulateChengdu=[]
y_EmbassyMonrovia=[]
y_EmbassyChisinau=[]
y_ConsulateMonterrey=[]
y_EmbassyGrenada=[]
y_ConsulateThessaloniki=[]
y_ConsulateGuadalajara=[]
y_EmbassyKolonia=[]
y_ConsulateVladivostok=[]
y_ConsulateShenyang=[]
y_ConsulateSurabaya=[]
y_ConsulateKarachi=[]
y_USDelegationFESTTWO=[]
y_EmbassyKoror=[]
y_EmbassyValletta=[]
y_ConsulateCapeTown=[]
y_ConsulateNagoya=[]
y_EmbassyPraia=[]
y_ConsulateSapporo=[]
y_ConsulateDurban=[]
y_MissionUNESCO=[]
y_ConsulateTijuana=[]
y_EmbassyBrazzaville=[]
y_EmbassyApia=[]
y_ConsulateStPetersburg=[]
y_EmbassyMajuro=[]
y_ConsulateMatamoros=[]
y_USOFFICEFSCCHARLESTON=[]
y_ConsulateMerida=[]
y_ConsulateBelfast=[]
y_ConsulateYekaterinburg=[]
y_ConsulateCiudadJuarez=[]
y_ConsulateLeipzig=[]
y_ConsulateSydney=[]
y_EmbassyMalabo=[]
y_ConsulateCalgary=[]
y_ConsulateMarseille=[]
y_ConsulateNogales=[]
y_ConsulatePontaDelgada=[]
y_ConsulateNuevoLaredo=[]
y_ConsulateStrasbourg=[]
y_ConsulatePerth=[]
y_Dhahran=[]
y_UNRome=[]
y_ConsulateDhahran=[]
y_AmericanConsulateHyderabad=[]
y_DIRFSINFATC=[]
y_ConsulateHamilton=[]
list2=['x_EmbassyLondon','x_EmbassyBeirut','x_EmbassyPretoria','x_EmbassyAthens','x_EmbassyTashkent','x_EmbassyRiyadh','x_EmbassyDamascus','x_EmbassyBucharest','x_EmbassyAbuDhabi','x_EmbassyAnkara','x_ConsulateHoChiMinhCity','x_EmbassyJakarta','x_EmbassyTheHague','x_EmbassyBandarSeriBegawan','x_EmbassyKinshasa','x_EmbassyHarare','x_EmbassyRabat','x_EmbassyLima','x_EmbassyTelAviv','x_EmbassyHelsinki','x_EmbassyHanoi','x_EmbassyBogota','x_EmbassyGaborone','x_EmbassyColombo','x_EmbassyBeijing','x_EmbassyUlaanbaatar','x_SecretaryofState','x_EmbassySanaa','x_USInterestsSectionHavana','x_ConsulateDubai','x_EmbassyCairo','x_EmbassyLusaka','x_EmbassyManila','x_EmbassyDoha','x_EmbassyTunis','x_EmbassyVatican','x_EmbassyCaracas','x_EmbassyAshgabat','x_EmbassyDakar','x_EmbassyBanjul','x_EmbassyLibreville','x_EmbassyLilongwe','x_EmbassyParis','x_EmbassyPhnomPenh','x_EmbassyRangoon','x_EmbassyIslamabad','x_EmbassyAbuja','x_EmbassyDjibouti','x_EmbassyPrague','x_EmbassyKuwait','x_EmbassyAccra','x_EmbassySofia','x_EmbassyKualaLumpur','x_EmbassyManama','x_EmbassyPristina','x_EmbassyKhartoum','x_EmbassyAddisAbaba','x_ConsulateLagos','x_EmbassyAmman','x_ConsulateMilan','x_ConsulateAdana','x_EmbassyAlgiers','x_EmbassyRome','x_ConsulateFrankfurt','x_ConsulateIstanbul','x_EmbassyMaputo','x_EmbassyMadrid','x_EmbassyMuscat','x_EmbassyBrasilia','x_EmbassyTegucigalpa','x_EmbassyKathmandu','x_ConsulateJerusalem','x_EmbassySingapore','x_ConsulateHalifax','x_EmbassyZagreb','x_EmbassyYerevan','x_USDelegation,Secretary','x_EmbassyBelgrade','x_EmbassyBuenosAires','x_ConsulateJeddah','x_EmbassyBrussels','x_USUNNewYork','x_EmbassyKabul','x_EmbassyOttawa','x_EmbassySantiago','x_EmbassyKampala','x_EmbassySantoDomingo','x_ConsulateMontreal','x_EmbassyNassau','x_ConsulateVancouver','x_EmbassyMbabane','x_USEUBrussels','x_EmbassyGuatemala','x_EmbassySeoul','x_EmbassyDushanbe','x_EmbassyBangkok','x_EmbassyNewDelhi','x_EmbassyAsuncion','x_EmbassyMaseru','x_ConsulateChennai','x_EmbassyLaPaz','x_EmbassyTripoli','x_EmbassyParamaribo','x_EmbassyBerlin','x_EmbassyWellington','x_ConsulateKolkata','x_EmbassyBratislava','x_EmbassyManagua','x_ConsulateGuayaquil','x_EmbassyDhaka','x_ConsulateSaoPaulo','x_EmbassyKigali','x_EmbassyVilnius','x_EmbassyLjubljana','x_EmbassyBaghdad','x_EmbassyDublin','x_ConsulateRioDeJaneiro','x_EmbassySanJose','x_ConsulateQuebec','x_EmbassyPanama','x_ConsulateMumbai','x_EmbassyAsmara','x_EmbassyQuito','x_EmbassyPortAuPrince','x_EmbassyMoscow','x_AmericanInstituteTaiwan,Taipei','x_MissionGeneva','x_ConsulateToronto','x_ConsulateRecife','x_ConsulateHongKong','x_EmbassyCopenhagen','x_EmbassySanSalvador','x_EmbassyNouakchott','x_USOfficeAlmaty','x_EmbassyBern','x_EmbassyKyiv','x_EmbassyNdjamena','x_EmbassyNairobi','x_EmbassyCanberra','x_EmbassyAbidjan','x_EmbassyTokyo','x_EmbassyOslo','x_EmbassyFreetown','x_EmbassyVienna','x_EmbassyMontevideo','x_ConsulateChiangMai','x_EmbassyStockholm','x_EmbassyConakry','x_EmbassyBridgetown','x_REOKirkuk','x_ConsulateAuckland','x_ConsulatePeshawar','x_REOMosul','x_REOHillah','x_ConsulateHermosillo','x_EmbassyNicosia','x_EmbassyKingston','x_EmbassySkopje','x_EmbassyDili','x_EmbassyWarsaw','x_EmbassyMexico','x_EmbassyBelmopan','x_ConsulateFlorence','x_EmbassyGeorgetown','x_ConsulateCuracao','x_EmbassyDarEsSalaam','x_EmbassyMinsk','x_REOBasrah','x_EmbassyReykjavik','x_ConsulateCasablanca','x_EmbassyPortOfSpain','x_EmbassyBaku','x_ConsulateOsakaKobe','x_ConsulateFukuoka','x_EmbassySuva','x_EmbassyWindhoek','x_ConsulateAmsterdam','x_ConsulateMunich','x_ConsulateGuangzhou','x_EmbassyLuanda','x_EmbassyAntananarivo','x_ConsulateNaples','x_EmbassyPortMoresby','x_EmbassyBudapest','x_EmbassyLome','x_EmbassyTallinn','x_EmbassySarajevo','x_ConsulateLahore','x_ConsulateNaha','x_MissionUSOSCE','x_EmbassyVientiane','x_EmbassyRiga','x_EmbassyAstana','x_EmbassyBishkek','x_USMissionGeneva','x_ConsulateJohannesburg','x_EmbassyTirana','x_EmbassyBamako','x_EmbassyPortLouis','x_EmbassyNiamey','x_EmbassyYaounde','x_EmbassyLisbon','x_ConsulateDusseldorf','x_EmbassyBujumbura','x_ConsulateMelbourne','x_EmbassyLuxembourg','x_EmbassyCotonou','x_UNVIE','x_EmbassyOuagadougou','x_MissionUSNATO','x_EmbassyTbilisi','x_ConsulateShanghai','x_EmbassyBangui','x_EmbassyPodgorica','x_ConsulateBarcelona','x_IranRPODubai','x_ConsulateKrakow','x_ConsulateHamburg','x_ConsulateChengdu','x_EmbassyMonrovia','x_EmbassyChisinau','x_ConsulateMonterrey','x_EmbassyGrenada','x_ConsulateThessaloniki','x_ConsulateGuadalajara','x_EmbassyKolonia','x_ConsulateVladivostok','x_ConsulateShenyang','x_ConsulateSurabaya','x_ConsulateKarachi','x_USDelegationFESTTWO','x_EmbassyKoror','x_EmbassyValletta','x_ConsulateCapeTown','x_ConsulateNagoya','x_EmbassyPraia','x_ConsulateSapporo','x_ConsulateDurban','x_MissionUNESCO','x_ConsulateTijuana','x_EmbassyBrazzaville','x_EmbassyApia','x_ConsulateStPetersburg','x_EmbassyMajuro','x_ConsulateMatamoros','x_USOFFICEFSCCHARLESTON','x_ConsulateMerida','x_ConsulateBelfast','x_ConsulateYekaterinburg','x_ConsulateCiudadJuarez','x_ConsulateLeipzig','x_ConsulateSydney','x_EmbassyMalabo','x_ConsulateCalgary','x_ConsulateMarseille','x_ConsulateNogales','x_ConsulatePontaDelgada','x_ConsulateNuevoLaredo','x_ConsulateStrasbourg','x_ConsulatePerth','x_Dhahran','x_UNRome','x_ConsulateDhahran','x_AmericanConsulateHyderabad','x_DIRFSINFATC','x_ConsulateHamilton','y_EmbassyLondon','y_EmbassyBeirut','y_EmbassyPretoria','y_EmbassyAthens','y_EmbassyTashkent','y_EmbassyRiyadh','y_EmbassyDamascus','y_EmbassyBucharest','y_EmbassyAbuDhabi','y_EmbassyAnkara','y_ConsulateHoChiMinhCity','y_EmbassyJakarta','y_EmbassyTheHague','y_EmbassyBandarSeriBegawan','y_EmbassyKinshasa','y_EmbassyHarare','y_EmbassyRabat','y_EmbassyLima','y_EmbassyTelAviv','y_EmbassyHelsinki','y_EmbassyHanoi','y_EmbassyBogota','y_EmbassyGaborone','y_EmbassyColombo','y_EmbassyBeijing','y_EmbassyUlaanbaatar','y_SecretaryofState','y_EmbassySanaa','y_USInterestsSectionHavana','y_ConsulateDubai','y_EmbassyCairo','y_EmbassyLusaka','y_EmbassyManila','y_EmbassyDoha','y_EmbassyTunis','y_EmbassyVatican','y_EmbassyCaracas','y_EmbassyAshgabat','y_EmbassyDakar','y_EmbassyBanjul','y_EmbassyLibreville','y_EmbassyLilongwe','y_EmbassyParis','y_EmbassyPhnomPenh','y_EmbassyRangoon','y_EmbassyIslamabad','y_EmbassyAbuja','y_EmbassyDjibouti','y_EmbassyPrague','y_EmbassyKuwait','y_EmbassyAccra','y_EmbassySofia','y_EmbassyKualaLumpur','y_EmbassyManama','y_EmbassyPristina','y_EmbassyKhartoum','y_EmbassyAddisAbaba','y_ConsulateLagos','y_EmbassyAmman','y_ConsulateMilan','y_ConsulateAdana','y_EmbassyAlgiers','y_EmbassyRome','y_ConsulateFrankfurt','y_ConsulateIstanbul','y_EmbassyMaputo','y_EmbassyMadrid','y_EmbassyMuscat','y_EmbassyBrasilia','y_EmbassyTegucigalpa','y_EmbassyKathmandu','y_ConsulateJerusalem','y_EmbassySingapore','y_ConsulateHalifax','y_EmbassyZagreb','y_EmbassyYerevan','y_USDelegation,Secretary','y_EmbassyBelgrade','y_EmbassyBuenosAires','y_ConsulateJeddah','y_EmbassyBrussels','y_USUNNewYork','y_EmbassyKabul','y_EmbassyOttawa','y_EmbassySantiago','y_EmbassyKampala','y_EmbassySantoDomingo','y_ConsulateMontreal','y_EmbassyNassau','y_ConsulateVancouver','y_EmbassyMbabane','y_USEUBrussels','y_EmbassyGuatemala','y_EmbassySeoul','y_EmbassyDushanbe','y_EmbassyBangkok','y_EmbassyNewDelhi','y_EmbassyAsuncion','y_EmbassyMaseru','y_ConsulateChennai','y_EmbassyLaPaz','y_EmbassyTripoli','y_EmbassyParamaribo','y_EmbassyBerlin','y_EmbassyWellington','y_ConsulateKolkata','y_EmbassyBratislava','y_EmbassyManagua','y_ConsulateGuayaquil','y_EmbassyDhaka','y_ConsulateSaoPaulo','y_EmbassyKigali','y_EmbassyVilnius','y_EmbassyLjubljana','y_EmbassyBaghdad','y_EmbassyDublin','y_ConsulateRioDeJaneiro','y_EmbassySanJose','y_ConsulateQuebec','y_EmbassyPanama','y_ConsulateMumbai','y_EmbassyAsmara','y_EmbassyQuito','y_EmbassyPortAuPrince','y_EmbassyMoscow','y_AmericanInstituteTaiwan,Taipei','y_MissionGeneva','y_ConsulateToronto','y_ConsulateRecife','y_ConsulateHongKong','y_EmbassyCopenhagen','y_EmbassySanSalvador','y_EmbassyNouakchott','y_USOfficeAlmaty','y_EmbassyBern','y_EmbassyKyiv','y_EmbassyNdjamena','y_EmbassyNairobi','y_EmbassyCanberra','y_EmbassyAbidjan','y_EmbassyTokyo','y_EmbassyOslo','y_EmbassyFreetown','y_EmbassyVienna','y_EmbassyMontevideo','y_ConsulateChiangMai','y_EmbassyStockholm','y_EmbassyConakry','y_EmbassyBridgetown','y_REOKirkuk','y_ConsulateAuckland','y_ConsulatePeshawar','y_REOMosul','y_REOHillah','y_ConsulateHermosillo','y_EmbassyNicosia','y_EmbassyKingston','y_EmbassySkopje','y_EmbassyDili','y_EmbassyWarsaw','y_EmbassyMexico','y_EmbassyBelmopan','y_ConsulateFlorence','y_EmbassyGeorgetown','y_ConsulateCuracao','y_EmbassyDarEsSalaam','y_EmbassyMinsk','y_REOBasrah','y_EmbassyReykjavik','y_ConsulateCasablanca','y_EmbassyPortOfSpain','y_EmbassyBaku','y_ConsulateOsakaKobe','y_ConsulateFukuoka','y_EmbassySuva','y_EmbassyWindhoek','y_ConsulateAmsterdam','y_ConsulateMunich','y_ConsulateGuangzhou','y_EmbassyLuanda','y_EmbassyAntananarivo','y_ConsulateNaples','y_EmbassyPortMoresby','y_EmbassyBudapest','y_EmbassyLome','y_EmbassyTallinn','y_EmbassySarajevo','y_ConsulateLahore','y_ConsulateNaha','y_MissionUSOSCE','y_EmbassyVientiane','y_EmbassyRiga','y_EmbassyAstana','y_EmbassyBishkek','y_USMissionGeneva','y_ConsulateJohannesburg','y_EmbassyTirana','y_EmbassyBamako','y_EmbassyPortLouis','y_EmbassyNiamey','y_EmbassyYaounde','y_EmbassyLisbon','y_ConsulateDusseldorf','y_EmbassyBujumbura','y_ConsulateMelbourne','y_EmbassyLuxembourg','y_EmbassyCotonou','y_UNVIE','y_EmbassyOuagadougou','y_MissionUSNATO','y_EmbassyTbilisi','y_ConsulateShanghai','y_EmbassyBangui','y_EmbassyPodgorica','y_ConsulateBarcelona','y_IranRPODubai','y_ConsulateKrakow','y_ConsulateHamburg','y_ConsulateChengdu','y_EmbassyMonrovia','y_EmbassyChisinau','y_ConsulateMonterrey','y_EmbassyGrenada','y_ConsulateThessaloniki','y_ConsulateGuadalajara','y_EmbassyKolonia','y_ConsulateVladivostok','y_ConsulateShenyang','y_ConsulateSurabaya','y_ConsulateKarachi','y_USDelegationFESTTWO','y_EmbassyKoror','y_EmbassyValletta','y_ConsulateCapeTown','y_ConsulateNagoya','y_EmbassyPraia','y_ConsulateSapporo','y_ConsulateDurban','y_MissionUNESCO','y_ConsulateTijuana','y_EmbassyBrazzaville','y_EmbassyApia','y_ConsulateStPetersburg','y_EmbassyMajuro','y_ConsulateMatamoros','y_USOFFICEFSCCHARLESTON','y_ConsulateMerida','y_ConsulateBelfast','y_ConsulateYekaterinburg','y_ConsulateCiudadJuarez','y_ConsulateLeipzig','y_ConsulateSydney','y_EmbassyMalabo','y_ConsulateCalgary','y_ConsulateMarseille','y_ConsulateNogales','y_ConsulatePontaDelgada','y_ConsulateNuevoLaredo','y_ConsulateStrasbourg','y_ConsulatePerth','y_Dhahran','y_UNRome','y_ConsulateDhahran','y_AmericanConsulateHyderabad','y_DIRFSINFATC','y_ConsulateHamilton']
for year in yearlist2:
	for files in glob.glob("result"+year+"/"+"*"):
		if files in embassies:
			fi=codecs.open(files,'r',encoding='utf-8')
			f=fi.read
			fi.close()
			nameoffile=files
			nameoffile=nameoffile.replace("result"+year+"/","")
			if f=='':
				t=year
				t=t.split("_")
				for index,val in enumerate(t):			
					t[0]='20'+t[0]
					if index==2:
						if val==1:
							t[0]=t[0]+'0.08'
						if val==2:
							t[0]=t[0]+'0.17'
						if val==3:
							t[0]=t[0]+'0.25'
						if val==4:
							t[0]=t[0]+'0.33'
						if val==5:
							t[0]=t[0]+'0.42'
						if val==6:
							t[0]=t[0]+'0.50'
						if val==7:
							t[0]=t[0]+'0.58'
						if val==8:
							t[0]=t[0]+'0.67'
						if val==9:
							t[0]=t[0]+'0.74'
						if val==10:
							t[0]=t[0]+'0.83'
						if val==11:
							t[0]=t[0]+'0.92'
						if val==12:
							t[0]=t[0]+'0.99'
				nameoffile2=nameoffile
				nameoffile2=nameoffile2.replace(" ","")
				for index2,filename in enumerate(list2):
					nameoffile=nameoffile.replace(" ","")
					if nameoffile=='**Dhahran':
						nameoffile='Dhahran'
					if "x_"+nameoffile==filename:
						(filename).append(0.0)
#				if 'x_'+nameoffile2 in list2:
				for index2,filename in enumerate(list2):
					nameoffile=nameoffile.replace(" ","")
					if nameoffile=='**Dhahran':
						nameoffile='Dhahran'
					if "x_"+nameoffile==filename:
						(filename).append(float(t[0]))
					
#				('x_'+nameoffile).append(0.0)
#				('y_'+nameoffile).append(float(t[0]))
			else:
				f=f.split(',')
				xintercept=int(f[0])-int(f[1])
				t=year
				t=t.split("_")
				for index,val in enumerate(t):			
					t[0]='20'+t[0]
					if index==2:
						if val==1:
							t[0]=t[0]+'0.08'
						if val==2:
							t[0]=t[0]+'0.17'
						if val==3:
							t[0]=t[0]+'0.25'
						if val==4:
							t[0]=t[0]+'0.33'
						if val==5:
							t[0]=t[0]+'0.42'
						if val==6:
							t[0]=t[0]+'0.50'
						if val==7:
							t[0]=t[0]+'0.58'
						if val==8:
							t[0]=t[0]+'0.67'
						if val==9:
							t[0]=t[0]+'0.74'
						if val==10:
							t[0]=t[0]+'0.83'
						if val==11:
							t[0]=t[0]+'0.92'
						if val==12:
							t[0]=t[0]+'0.99'
				for index2,filename in enumerate(list2):
					nameoffile=nameoffile.replace(" ","")
					if nameoffile=='**Dhahran':
						nameoffile='Dhahran'
					if "x_"+nameoffile==filename:
						(filename).append(xintercept)
#				('x_'+nameoffile).append(xintercept)
				for index2,filename in enumerate(list2):
					nameoffile=nameoffile.replace(" ","")
					if nameoffile=='**Dhahran':
						nameoffile='Dhahran'
					if "x_"+nameoffile==filename:
						(filename).append(float(t[0]))
#		else:

#			t=year
#			t=t.split("_")
#			for index,val in enumerate(t):			
#				t[0]='20'+t[0]
#				if index==2:
#					if val==1:
#						t[0]=t[0]+'0.08'
#					if val==2:
#						t[0]=t[0]+'0.17'
#					if val==3:
#						t[0]=t[0]+'0.25'
#					if val==4:
#						t[0]=t[0]+'0.33'
#					if val==5:
#						t[0]=t[0]+'0.42'
#					if val==6:
#						t[0]=t[0]+'0.50'
#					if val==7:
#						t[0]=t[0]+'0.58'
#					if val==8:
#						t[0]=t[0]+'0.67'
#					if val==9:
#						t[0]=t[0]+'0.74'
#					if val==10:
#						t[0]=t[0]+'0.83'
#					if val==11:
#						t[0]=t[0]+'0.92'
#					if val==12:
#						t[0]=t[0]+'0.99'
#			nameoffile=files
#			nameoffile=nameoffile.replace("result"+year+"/","")
#			for index2,filename in enumerate(list2):
#					nameoffile=nameoffile.replace(" ","")
#					if nameoffile=='**Dhahran':
#						nameoffile='Dhahran'
#					if "x_"+nameoffile==filename:	
#						(filename).append(0.0)
#			for index2,filename in enumerate(list2):
#					nameoffile=nameoffile.replace(" ","")
#					if nameoffile=='**Dhahran':
#						nameoffile='Dhahran'
#					if "x_"+nameoffile==filename:
#						(filename).append(float(t[0]))

print x_EmbassyLondon
for embassy in embassies:
					
	x=[1966,1980,2005,2008]
	#print x
	y=[0.3,0.5,-0.0,-0.3]
	print ('x_' + embassy)[0]
	print embassy
#	plt.plot('x_'+embassy, 'y_'+embassy, 'k')
	plt.plot(x, y, 'k')	
	plt.title(embassy, fontdict=font)
	plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
	plt.xlabel('year(s)', fontdict=font)
	plt.ylabel('sentiment', fontdict=font)

	# Tweak spacing to prevent clipping of ylabel
	plt.subplots_adjust(left=0.15)
	#plt.show()
	plt.savefig('figures/'+embassy+'.png')
#pylab.savefig('foo.png',bbox_inches='tight')
#plt.savefig('fafa.png', dpi=None, facecolor='w', edgecolor='w',        orientation='portrait', papertype=None, format=None,       transparent=False,bbox_inches=None, pad_inches=0.1,        frameon=None)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#print ax
#ax.plot(range(100))
#fig.savefig('graph.png')
