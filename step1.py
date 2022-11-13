#!/usr/bin/python3

import os,sys,subprocess

p=1

######1
while p==1:
 NUM=0
 
 #######1.1
 while NUM==0:
  #input proname
  profam=input("Please enter the name of the protein family you wish to search for:\n\t").upper()
  print("Check!")
  
  #input taxgp
  taxgp=[""]
  i=0
  #######1.1.1
  while i<5:
    j=input("Please enter the name of the taxonomic group you wish to search for in order (enter NONE to end):\n\t")
    if j=="NONE":
      break
    j=j.upper()
    taxgp.append(j)
    i+=1
  print("Check!")
  
  #query try
  qcommand='esearch -db protein -query '+"\'"+ ' AND '.join(taxgp)+' AND '+profam+'[PROT]'+"\'"+" > loop1.txt"
  os.system(qcommand)
  
  #choice of count
  count=0
  loop=open("loop1.txt","r")
  lines=loop.readlines()
  count_r=lines[4]
  count=count_r.replace('<Count>','').replace('</Count>\n','')
  dcommand='rm -f loop1.txt'
  os.system(dcommand)
  c=int(count)
  if c <=1000 and c>=10:
    NUM=1
  if c>=1000:
    print("Searching for too many protein sequences may cause the program to run too slowly or the results to be biologically insignificant.")
    p=input("Do you want to continue running the program? (Enter YES or NO):\n\t")
    if p=="YES":
      NUM=1
    if p=="NO":
      print('\n\tPROCESSING\t\n')
  if c<=10:
    print("Searching for too few protein sequences may result in biologically insignificant results.")
    p=input("Do you want to continue running the program? (Enter YES or NO):\n\t")
    if p=="YES":
      NUM=1
    if p=="NO":
      print('\n\tPROCESSING\t\n')
          
  if NUM == 1:
    break
     
 #get fastafile
 qcommand='esearch -db protein -query '+"\'"+ ' AND '.join(taxgp)+' AND '+profam+'[PROT]'+"\'"+" | efetch -format fasta"+" > loop_fasta.txt"
 os.system(qcommand)
 
 lcommand="grep '>' loop_fasta.txt > loop_speices.txt"
 os.system(lcommand)
 #Species count
 loop=open("loop_speices.txt","r")
 lines=loop.readlines()
 loop_sp=[""]
 for i in lines:
   j=i.split("[")
   k=j[-1].split("]")
   loop_sp.append(k[0])
 sp=list(set(loop_sp))
 count_sp=len(sp)-1
 print("Your search results include a total of "+str(count_sp)+" species")
 
 #choice of displaying for species names
 x=1
 #######1.2
 while x==1:
   x=input("Do you want to know the names of these species? (Enter YES or NO)\n\t")
   if x=="YES":
     for i in sp:
       print(i)
     x=0
   elif x =="NO":
     x=0
   else:
     print("TYPO")
 
 #Species counts are too low
 p=1    
 if count_sp<=5:
   print("The number of species in your search content is too small, which may lead to the biological significance of the subsequent results. ")
   #######1.3
   while True:
     p=input("\tDo you want to continue the program?(Enter YES or NO)\n\t")
     if p=="YES":
       p=1
       break
     if p=="NO":
       p=0
       break
     if p!="YES" or p!="NO":
       print("TYPO")
       
 #ending of step1
 if p==0:
   print("\n\tRESTARTING\n")
 if p==1:
   print("\n\tGOOD JOB!\nThe program will proceed to the second part.")
   break
#######