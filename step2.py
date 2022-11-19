#!/usr/bin/python3

import os,sys

print("\n\tThis is the beginning of the second part of the program.\n")
print(" SOMETHING ")
print("Do you want to select a certain number of sequences in your search for the second step or do you want to use your entire search results for the second step? ")
first=input("(type \"SELECT\" to start the selection, type anything else to skip the selection)\n\t")
NUM=2

if first=="SELECT":
  NUM=1
  
choice=''
while NUM==1:
  choice=input("Search by species name please enter \"SN\".\nSearch by protein ID please enter \"PID\"\nTo search by sequence similarity to a template sequence please enter \"SST\".\n\t")
  if choice=='SN':
    NUM = 0
  if choice=='PID' :
    NUM = 0
  if choice=='SST' :
    NUM = 0
  else:
    print('\tTYPO!')

p=''

while NUM==0:
  #######
  if choice == 'SN':
    loop=open("loop_speices.txt","r")
    lines=loop.readlines()
    loop_sp=[]
    
    for i in lines:
      j=i.split("[")
      k=j[-1].split("]")
      loop_sp.append(k[0])
      
    sp=list(set(loop_sp))
    count_T=len(sp)
    print("Your search results include a total of "+str(count_T)+" species"+"\n")
    print("These include: ")
    
    count=0
    for i in sp:
      count+=1
      print(str(count)+'\t'+i)
    
    p='YES' 
    while p=='YES':  
      count=0
      r_name=[]
      iname=''
      while iname!='NONE':
        count+=1
        iname=input("Please enter the species names one by one (strictly case sensitive):\n\t")
        print("\t(enter NONE to end)")
        if iname in sp:
          r_name.append(iname)
        if iname not in sp and iname != 'NONE':
          print("\tTYPO!")
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
  if p=="NO":
    loop=open("loop_fasta.txt","r")
    each=loop.read().split('>')
    s_name=[]
    for i in each[1:]:
      j=i.split("[")
      k=j[-1].split("]")
      if k[0] in name:
        s_name.append(i)
    NUM=1


  #######
  if choice =="PID":
    loop=open("loop_speices.txt","r")
    lines=loop.readlines()
    loop_id=[]

    for i in lines:
      j=i.split(" ")
      k=j[0].split(">")
      loop_id.append(k[-1])
    
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
    
  #if choice == "SST":
    
#########


if NUM==1:
  ss_name='>'+'>'.join(s_name)
if NUM==2:
  loop=open('loop_fasta.txt','r')
  ss_name=loop.read()

loop=open('loop_select.txt','w')
loop.write(ss_name)
loop.close()
ccommand="clustalo -i loop_select.txt -o loop_clus.txt -v --force"
os.system(ccommand)
p=0
while p==0:
  while True:
    size=input("Chose your window size:(enter an number)\n\t")
    try:    
      s=eval(size)
      break
    except:
      print("\tTYPO!")
  
  ppcommand="plotcon loop_clus.txt -winsize "+ size + " -graph png"
  os.system(ppcommand)
  print("The Similarity Plot of Aligned Sequences has been downloaded in the folder where step2.py is located.")
  pdcommand="plotcon loop_clus.txt -winsize "+ size + " -graph data "
  os.system(pdcommand)
  

  pp=0
  while pp==0:
    fp=input("Are you satisfied with the window size you have chosen?(enter \"YES\" or \"NO\")")
    if fp=="YES":
      p=1
      pp=1
    if fp =="NO":
      p=0
      pp=1
    if fp!="YES" and fp!="NO":
      print("typo")
print('GoodJob!\nThe program will proceed to the Third part.')      
      
    