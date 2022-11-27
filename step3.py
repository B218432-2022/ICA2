#!/usr/bin/python3
import os,sys
import re

print('\n\tHere is the start of step 3.\n')

j8=0
while j8==0:
#A screening process very similar to step 2.
  NUM=0
  p=0
  while p==0:
    print('Would you like to further sift through the results of Step 2?')
    choice = input("(Enter \"YES\" or \"NO\")\n\t")
    if choice=="YES" or choice =="NO":
      p=1
    else:
      print("\n\tTYPO!\n")
      
  if choice =="YES":
      loop=open("loop_select.txt","r")
      lines=loop.readlines()
      loop_id=[]
  
      for i in lines:
        if i[0] == '>':
          k=i.split(' ')
          a=k[0].split('>')
          loop_id.append(a[-1])
      
      ID=list(set(loop_id))
      count_T=len(ID)
      print("Your search results include a total of "+str(count_T)+" protien ID"+"\n")
      print("These include: ")
      
      count=0
      for i in ID:
        count+=1
        print(str(count)+"\t"+i)
        
      p='YES'
      while p=='YES':
        count=0
        r_name=[]
        iname=''
        while iname!='NONE':
          count+=1
          iname=input('Please enter the protein ID one by one (strictly case sensitive):\n\t')
          print("\t(enter NONE to end)")
          if iname in ID:
            r_name.append(iname)
          if iname not in ID and iname != 'NONE':
            print("TYPO")
          if int(count)>int(count_T):
            print('Repeat entries are possible. But don\'t worry, the program will correct it automatically.')
            
        name=list(set(r_name))
        print("You have entered the species name as follows.")
        for i in name:
          print(i)
        pp=0
        while pp==0:
          p=input("Do you wish to re-enter? (Enter YES or NO)\n\t")
          if p=='YES' or p=='NO':
            pp=1
          else:
            print("\tTYPO!")
        
      if p=='NO': 
        loop=open("loop_fasta.txt","r")
        each=loop.read().split('>')
        s_name=[]
        for i in each:
          j=i.split(" ")
          k=j[0]
          if k in name:
            s_name.append(i)
        NUM=1
  
  
      if NUM==1:
        ss_name='>'+'>'.join(s_name)
      if NUM==2:
        loop=open('loop_fasta.txt','r')
        ss_name=loop.read()
        
      loop=open('loop_select_select.txt','w')
      loop.write(ss_name)
      loop.close()
  
  if choice == "NO":
    loop=open('loop_select.txt','r')
    ss_name=loop.read()
    loop=open('loop_select_select.txt','w')
    loop.write(ss_name)
    loop.close()
  
  #After finishing the filter, loop through the patamatmotifs program
  loop=open('loop_select_select.txt','r')
  whole=loop.read()
  wholelist_re=whole.split(">")
  
  wholelist_name=[]
  for i in wholelist_re[1:]:
    loop=open('loop.txt','w')
    loop.write('>'+i)
    loop.close()
    name=i.split(' ')
    wholelist_name.append(name[0])
    patcommand="patmatmotifs -sequence loop.txt -outfile "+ name[0] +".txt -auto"
    os.system(patcommand)
  
  ##output1:
  print("The names of the motifs contained in each protein sequence are as follows:")
  dic1={}
  for i in wholelist_name:
    loop=open(i+'.txt','r')
    whole=loop.readlines()
    dic1_list=[]
    for j in whole:
      if re.search(r'Motif = ',j):
        k=j.split(' ')
        e=k[-1].split('\n')
        dic1_list.append(e[0])
    dic1[i]=dic1_list
  
  name=list(dic1)
  wholename=[]
  for i in name:
    op=i+':\t' + '\t'.join(dic1[i])
    print(op)
    wholename=wholename+dic1[i]
  
  ##output2
  print("\nNumber of occurrences of each motif in all your searches:")
  i=0
  allname=[]
  maxname=''
  for j in list(set(wholename)):
    print(j+':\t'+str(wholename.count(j))) 
    if wholename.count(j)>int(i):
      i=wholename.count(j)
    if wholename.count(j)==len(name):
      allname.append(j)
  #output3    
  if i == len(name):
    for a in allname:
      print("\nmotifi " + a + " is present in all search sequences.")
  else: 
    print("\nThere is no common motif in all the search sequences.")
  
  ##output4:After finishing the filter, loop through the patamatmotifs program
  dicc={}
    #Building a motif Dictionary
  for i in list(set(wholename)):
    dicc[i]=''
    for j in name:
      loop=open(j+".txt",'r')
      select_raw=loop.read()
      select_ql_raw=select_raw.split('Length = ')
      for ql in select_ql_raw[1:]:
        select_ql=ql.split('\n')
        select_qll ='\n'.join(select_ql[0:10])
        o=select_qll.split('Motif = ')
        t=o[-1].split('\n')
        if t[0]==i:
          dicc[i]=dicc[i]+j+"\n"+'Length = '+select_qll +"\n========================\n"
  
  
    #The motif information of interest to the customer is invoked from the motif dictionary
  pp=0
  while pp==0:
    p=0
    while p==0:
      select_choice=input('Please enter the name of the motif you are interested in one by one. (strictly case sensitive):\n\t')
      if select_choice not in list(dicc) and select_choice!='NONE':
        print("\nTYPO!")
      else:
        p=1
    if select_choice=="NONE":
      pp=1
    else:
      print(select_choice)
      print(dicc[select_choice])
  
  #If you are not satisfied with the result, you can redo the second part.
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

    
print("Good Job!\nThe program will proceed to the fourth part.")
os.system("./step4.py")



  