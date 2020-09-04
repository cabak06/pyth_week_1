import os
import argparse

def first_function(path_to_folder):
    #parser = argparse.ArgumentParser()
    #parser.add_argument("read_to", help="file_path to output_file")
    #args = parser.parse_args()  
    files = []
    for element in os.listdir(path_to_folder):
        if os.path.isfile(element):
            files.append(element)
    with open('exercise2.txt','w') as v:
        for file in files:
            v.write(file + '\n')
 


def second_function(path_to_folder):

    listen = []
    files = os.listdir(path_to_folder)
    for file in files:
        low_path = os.path.join(path_to_folder, file)
        if(path_to_folder.isdir(low_path)):
            sub_files = os.listdir(low_path)
            for subfile in sub_files:
                listen.append(subfile)
        else:
            listen.append(file)

    with open('second_txt','w') as v:
        for file in listen:
            v.write(file +'\n')



file_system = ['cars.csv','exercise2.txt','file_to_read.txt','output_file.txt']

def third_function(file_system):
    first_liners = []
    #for filename in file_system: dette kører lokalt men ikke over notebook
    indx = 0
    while indx < len(file_system):
        with open(file_system[indx],'r') as v:
            line = v.readline()
            first_liners.append(line)
            indx += 1
    for element in first_liners:
        print(element + '\n')



mail_system = ['cars.csv','exercise2.txt','file_to_read.txt','output_file.txt','mail1.txt','mail2.txt']

def fourth_function(file_system):
    list_with = []
    #for filename in file_system:
    indx = 0
    while indx < len(mail_system):
        text = open(mail_system[indx],'r')
        lines = text.readlines()
        for line in lines:
            for char in line:
                if(char == '@'):
                    list_with.append(line)
        indx +=1
                
    for element in list_with:
        print(element + '\n')
          


md_files = ['exercise2.txt','file_to_read.txt','output_file.txt','mail1.txt','mail2.txt','md_file1.md','md_file2.md']

def fifth_function(md_files,path):
    list_with = []
    #for filename in md_files:
    indx = 0
    while indx < len(md_files):
        text = open(md_files[indx],'r')
        lines = text.readlines()
        for line in lines:
            if(line[0] == '#'):
                list_with.append(line)
        indx +=1
    with open(path,'w') as v:
        for element in list_with:
            v.write(element +'\n')















