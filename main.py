# -*- coding: utf-8 -*-
## Please to have a problem using github.com/ruperthnyagesoa/blog-search mention ISSUE
### Author: Ruperth
#### MICENCE: MIT
##### blog-search
import os
from bs4 import BeautifulSoup

## Set the target
target = './articles/' # Directory location
layers = 1 # Traverse layer
targettype = 'html' # The file suffix ( only support html)

## JSON standard format
# {"articles":[{"title":"The article title","path":"Relative paths","time":"Update time","text":"All the body"},{"title":"The article title","path":"Relative paths","time":"Update time","text":"All the body"},{"title":"The article title","path":"Relative paths","time":"Update time","text":"All the body"}]}
main_structure_head='{"articles":['
main_structure_end=']}'
inner_structure_1='{"title":"'
inner_structure_2='","path":"'
inner_structure_3='","time":"'
inner_structure_4='","text":"'
inner_structure_5='"}'


## Open the target directory
targetfile = []
for i in os.listdir(target):
    if '.' not in i:
        for k in os.listdir(target +i):
            if targettype in k:
                targetfile.append(target + i + '/' + k)

## Reconstruct the target file
inner_structure_cache=[]
inner_structure_text=''
for i in targetfile:
    with open(i,'r') as f:
        filecontent = BeautifulSoup(f.read(),'html.parser')
        textlist = filecontent.find_all(name='p')
        title = filecontent.find_all(name='h2')
        titlelen=len(title)
    length = len(textlist)
    for j in range(length):
        inner_structure_text=inner_structure_text+textlist[j].get_text()
    time = i[-19:-11]
    time = time[0:4]+'-'+time[4:6]+'-'+time[6:8]
    title = title[titlelen-1]
    path = i[1:][:-10]
    inner_structure_text=inner_structure_text.replace(' ','').replace('\n','').replace('"','&quot;')
    inner_structure_all = inner_structure_1 + str(title.get_text()) + inner_structure_2 + str(path) + inner_structure_3 + str(time) + inner_structure_4 + inner_structure_text + inner_structure_5
    inner_structure_cache.append(inner_structure_all)

## Refactoring complete JSON
main_structure = main_structure_head
for i in inner_structure_cache:
    main_structure = main_structure + i + ','
main_structure = main_structure[:-1] + main_structure_end

## To write thr JSON file
with open(target+'search.json','w+') as f1:
    f1.write(main_structure)
    
        
