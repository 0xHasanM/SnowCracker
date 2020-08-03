#!/usr/bin/env python3
import subprocess
import sys
import getopt
import time
import pyfiglet
from concurrent.futures import ThreadPoolExecutor
def main(argv):
      print(pyfiglet.figlet_format("0xMohammed"))
      wordlist = ''
      textfile = ''
      Message = ''
      opt = ''
      stripped_password = ''
      try:
         opts, args = getopt.getopt(argv,"hw:f:",["wordlist=","file="])
      except getopt.GetoptError:
         print('snowcracker by 0xmohammed \n -w,--wordlisr <wordlist> \n -f,--file <textfile>')
         sys.exit()
      for opt, arg in opts:
         if opt == '-h':
            print('snowcracker by 0xmohammed \n -w,--wordlist <wordlist> \n -f,--file <textfile>')
            sys.exit()
         elif opt in ("-w", "--wordlist"):
            wordlist = open(arg, "r")
         elif opt in ("-f", "--file"):
            textfile = arg
      if opt == '':
            print('snowcracker by 0xmohammed \n -w,--wordlist <wordlist> \n -f,--file <textfile>')
            sys.exit()
      print("Bruteforcing...Plz wait")
      for password in wordlist:
            stripped_password = ''.join(password.split())
            result = out = subprocess.Popen(['stegsnow', '-Q', '-p', stripped_password, textfile], 
              stdout=subprocess.PIPE, 
              stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            try:
              Message = stdout.decode('ascii')
              if Message.isprintable() == True :
                 print("Password : "+stripped_password+"\nMessage : "+ Message)
              continue
            except:
              continue
if __name__ == "__main__":
   main(sys.argv[1:])
   executor = ThreadPoolExecutor(max_workers=10)
   a = executor.submit(main)
