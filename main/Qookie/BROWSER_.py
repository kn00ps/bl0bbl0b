# -*- coding: utf-8 -*-
import os ,random ,sys


from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



#binary = FirefoxBinary("/usr/bin/firefox")
#profile = FirefoxProfile("/root/.mozilla/firefox/q46k7l0h.default")
#driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)#, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")

######################################################
def createDriverInstance_with_profil():
	prro="/root/.mozilla/firefox/hbxtyfcz.00a001"
	binary = FirefoxBinary('/usr/bin/firefox')
	#fp=firefox_prof()
	fp=FirefoxProfile(prro)
	extension_path = '/root/ub.xpi'
	#options = Options()
	firefox_capabilities = DesiredCapabilities.FIREFOX
	firefox_capabilities['marionette'] = True
	firefox_capabilities['acceptSslCerts'] = True
	driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_profile=fp,firefox_binary=binary)
	driver.install_addon(extension_path, temporary=True)
	driver.implicitly_wait(10)
	return driver
######################################################
