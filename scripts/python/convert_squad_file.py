import click
import glob
import csv
import os.path
import pandas as pd
import re

#Select directories
dirs = glob.glob('../../csv/**/**/Football_League_First_Division/equipes/1904-1905')
#Select files
files = glob.glob('../../csv/**/**/Football_League_First_Division/equipes/1904-1905/*.csv')

def produce():
    print('Start...')
    #Create directories
    for dir in dirs:
        if os.path.isdir(f'{dir}_final'):
            print(f'Directory {dir} already created !')
        else:
            print(f'Create directory for {dir}')
            os.mkdir(f'{dir}_final')
        #Create files
        season = dir.split('/')[7]
        for file in files:
            if season in file:
                squad_file_name = file.split('/')[8]
                with open(file) as squadfile:
                    with open(f'{dir}_final/{squad_file_name}','a') as sfile:
                        first_head_line = 'Nation,Name,Position,App,Gls,Pen,App,Gls,Pen,App,Gls,Pen'
                        second_head_line = ',,,League,League,League,FA Cup,FA Cup,FA Cup,Other,Other,Other'
                        csv_squad = squadfile.read()
                        if '\t' in csv_squad:
                            result_file = csv_squad.replace('\t', ',')
                            result_file = re.sub('[,]+[\n]', ',"', result_file, flags = re.M)
                            result_file = re.sub(' [,]', ' ",', result_file, flags = re.M)
                            result_file = re.sub('.*[\n][\n][1][9][0-9][0-9]/[0-9][0-9][\n].*[\n][\n]', f'{first_head_line}\n{second_head_line}\n', result_file, flags = re.M)
                            result_file = re.sub('[\n]+[N]', 'N', result_file, flags = re.M)
                            sfile.write(result_file)
    print('Done !')

if __name__ == "__main__":
    produce()
    