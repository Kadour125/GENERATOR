#altenens.is => Superton 
import os
import time

#----------------------------------------------------------------------#
banner = """
 __                __   ___       ___  __       ___  __   __  
/  ` \  / \  /    / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
\__,  \/   \/     \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \                                                                                                                                                                                                             
"""
#----------------------------------------------------------------------#
def GenCvv(a):
	divideList = a.split("|")
	for lines in divideList:
		combo = divideList
		cc = combo[0]
		mm = combo[1]
		yyyy = combo[2]
		yy = (yyyy[2:4])
		cvv = combo[3]

	for i in range(1,1000):
		list_cvv = f"{cc}|{mm}|{yyyy}|{i:03}\n"
		archivo = open("cvvlist.txt","a")
		archivo.write(list_cvv)
		archivo.close()

	f = open ('cvvlist.txt','r')
	mensaje = f.read()
	print(mensaje)
	f.close()
	exit_app = input("press a key to close. ")
	time.sleep(5)

def path_exists():
	if os.path.exists("cvvlist.txt"):
		os.remove("cvvlist.txt")

def main():
	print(banner)
	path_exists()
	user_input = input("Example 4242424242424242|02|2024|000: ")
	a = user_input.replace(" ","").replace("/","|").replace(",","|").replace("\t","").replace("X","x").strip()
	count = len(a)
	if count == 28:
		GenCvv(a)
	else:
		print("Invalid Entered Method")
		time.sleep(1)
		print("Closing Application")
		time.sleep(5)

if __name__ == '__main__':
	main()
