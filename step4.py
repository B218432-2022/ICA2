#!/usr/bin/python3
import os,sys
print('\n\tHere is the start of step 4.\n')

j8=0
while j8==0:
#A screening process very similar to step 2.
  print("You can select a protein sequence for further analysis in step 4.")
  loop=open("loop_fasta.txt","r")
  lines=loop.readlines()
  loop_id=[]

  for i in lines:
    if i[0] == '>':
      k=i.split(' ')
      a=k[0].split('>')
      loop_id.append(a[-1])
  
  ID=list(set(loop_id))
  count_T=len(ID)
  print("Your search results from step1 include a total of "+str(count_T)+" protien ID"+"\n")
  print("These include: ")
      
  count=0
  for i in ID:
    count+=1
    print(str(count)+"\t"+i)
  p=0
  while p==0:
    iname=input('Please enter the protein ID (strictly case sensitive):\n\t')
    if iname in ID:
      r_name=iname
      p=1
    if iname not in ID and iname != 'NONE':
      print("TYPO")
  loop=open("loop_fasta.txt","r")
  each=loop.read().split('>')
  s_name=[]
  for i in each:
    j=i.split(" ")
    k=j[0]
    if k == r_name:
      s_name=i
  ss_name='>'+s_name
  loop=open('loop_select_select.txt','w')
  loop.write(ss_name)
  loop.close()
  
  jj=str.lower(r_name).split('.')
  pcommand="pepstats loop_select_select.txt -auto"
  os.system(pcommand)
  
  loop=open(jj[0]+'.pepstats','r')
  lines=loop.readlines()
  for i in lines:
    i=i.replace('\n','')
    print(i)  
  
  while True:
    size=input("Enter the length of the repeated short sequence you want to query (please enter Arabic numerals) :\n\t")
    try:    
      s=eval(size)
      break
    except:
      print("\tTYPO!")
  
  wcommand="wordcount loop_select_select.txt -wordsize " + str(size)+" -auto"
  os.system(wcommand)
  loop=open(jj[0]+'.wordcount','r')
  lines=loop.readlines()
  j=[]
  repeat=[]
  for i in lines:
    j=i.split('\t')
    if int(j[1])>1:
      repeat.append(i)
  
  print("The information of the sequences in which a repeat occurs is as follows:")
  print("seq\tcount")
  for i in repeat:
    print(i)
    
  p=0
  while p==0:
    jj=input("Do you want to try again?(Enter \"YES\" or \"NO\")\n\t")
    if jj=='YES' or jj=="NO":
      p=1
    else:
      print("\tTYPO!")
  if jj=="YES":
    print("\n\restarting\n")
  if jj=="NO":
    j8=1

print("GoodJob!\nYou have completed all the steps")