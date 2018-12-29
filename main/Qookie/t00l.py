# -*- coding: utf-8 -*-






######################################################
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
######################################################
#RT2
######################################################
def pinto (TEXT_,f):
	if f == "G_BLOOD_END" :
		print(bcolors.BOLD + bcolors.OKGREEN + TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f == "G_BLOOD_PLUS" :
		print(bcolors.BOLD + bcolors.OKGREEN + TEXT_+"" ,end=""+ bcolors.ENDC,flush=True)
	if f == "BLUE_BLOOD_END":
		print(bcolors.BOLD + bcolors.OKBLUE + TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f== "NF":
		print(bcolors.BOLD + bcolors.FAIL + TEXT_+"" ,end="\n"+bcolors.ENDC)
	if f == "NTX":
		print(TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f== "BR":
		print(bcolors.BOLD + bcolors.OKBLUE + TEXT_+"" ,end="\n"+bcolors.ENDC)
	if f == "RT2" :
		print(bcolors.BOLD + bcolors.FAIL + TEXT_+"" ,end="\n"+ bcolors.ENDC)

######################################################
def banner():
	print("""
		COOL
		BOT HUNTER
		THE YA
	 """)
	#print(tot)
######################################################