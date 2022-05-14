import click
import glob
import csv
import os.path
import pandas as pd

#Select files
files = glob.glob('../../csv/**/**/Football_League_First_Division/saisons/*.csv')

def produce():
    #TODO

def producteur(file_saison):
    global file
    global file_path
    global saved_equipe
    global names_files
    global year
    global year_fin


    names_files = []
    year = file_saison[-13:-9]
    year_fin = file_saison[-8:-4]

    #file load
    file_path = os.getcwd()+'/'+file_saison
    file = open(file_path)
    
    #save all equipes
    coloumn = ["\xc3\x89quipe"] 
    data = pd.read_csv(file,usecols=coloumn)
    saved_equipe = data[coloumn[0]] #without number in saved_equipe 
    print(saved_equipe)
    print("")
    print("phase : changeName")
    print("")
    saved_equipe = changeName(saved_equipe, year, year_fin)
    print (saved_equipe)
    print("")
    print("phase : create csv")

    #create folder
    folder = year + '-' + year_fin
    os.mkdir(folder)
    path=os.getcwd()+'/'+folder
    print('folder '+ folder + ' is created')


    creating(saved_equipe,path)

# transformer noms in noms of files
def changeName(equipes,deb,fin):
    result = []

    #saved all object in name
    for x in equipes :
        name=str(x)      #object convert to string
        names_files.append(name)

    #transforme names_files
    for x in equipes :
        tmp=""
        for i in x :
            if i!=" " : 
                tmp=tmp+i
            else :
                tmp=tmp+"_"
        tmp=tmp+'--'+deb+'-'+fin+'.csv'
        result.append(tmp)
    return result

# create all new files of csv
def creating(names,path_name):
    route = os.getcwd()
    csvwriter = csv
    for name in names :
        file_name = os.path.join(path_name,name)
        print(file_name)
        f=open(file_name,'w')
        f.close()
        print(f.closed)


if __name__ == "__main__":
    producteur()