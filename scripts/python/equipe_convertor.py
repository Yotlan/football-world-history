import click
import csv
import os.path
import pandas as pd

@click.group()
def cli():
   pass

@cli.command()
@click.argument('dossier_equipe')
def principal(dossier_equipe):



    path_directory=os.getcwd()+'/'+dossier_equipe

    if (os.path.isdir(os.getcwd()+'/'+dossier_equipe+'(2)')) :
        print("directory created")
    else :
        os.mkdir(dossier_equipe+'(2)')
        print("directory create")

    for file in os.listdir(path_directory) :
        if (file[len(file)-3:len(file)]=='csv'):
            print('file '+file + ' execution')
            producteur(file,path_directory,dossier_equipe)
            print('write ' + file +' : OK')

    print('finished')

def producteur(file,path_directory,directory):
    global file_path
    global year
    global year_fin


    
    year = file[-13:-9]
    year_fin = file[-8:-4]

    #file load
    print('Phase file load')
    file_path = path_directory+'/'+file

    file_r = open(file_path,'r')
    reader = csv.reader(file_r)

    #file writer
    writer_path = os.getcwd()+'/'+directory+'(2)'+'/'+file
    file_w = open(writer_path,'w')
    writer = csv.writer(file_w)

    #attribut prefixed
    att_head=['Nation','Name','Position','App','Gls','Pen','App','Gls','Pen','App','Gls','Pen']
    att_att=['','','','League','League','League','FA Cup','FA Cup','FA Cup','Other','Other','Other']

    #found caracters
    head=0
    tab=['\t\t\t\t\t\t\t\t\t\t']
    vide=[]
    date_t=year+'/'+year_fin[2]+year_fin[3]
    date=[date_t]
    attribut=['Position\tApp\tGls\tPen\tApp\tGls\tPen\tApp\tGls\tPen']

    for row in reader :
        #check head
        for x in row :
            if ('-' in x) :
                head=1

        if (head==1) :
            #print('head complete')
            writer.writerow(att_head)
            head=0
        elif (row==date) :
            pass
        elif (row==tab ) :
            pass
        elif (row==vide) :
            pass
        elif (row==attribut) :
            #print('attribut fixed') #convertir en attributs prefixed
            writer.writerow(att_att)
        else :
            #ligne normal
            # row [0] le debut du nom 
            content=['']
            first_name=row[0]+','
            # row [1] contient le reste 
            a = 0
            tmp=' '
            capt=0
            nom_found=0
            position_found=0 

            last_name=''
            position=''
            while a < len(row[1]):
                if (nom_found==0) :
                    #found last name
                    if (row[1][a]==' ') :
                        if (capt==0) :
                            capt=1
                            tmp=' '
                        elif (capt==1) :
                            tmp=tmp+' '
                            last_name=tmp
                            capt=0
                            tmp=''
                            nom_found=1
                    if (row[1][a]!=' ') :
                        if (capt==1) :
                            tmp=tmp+row[1][a]
                            
                elif (position_found==0) : 
                    #position_found==0

                    if (row[1][a]==chr(9)) :
                        if (capt==0) :
                            capt=1
                            #print('position av = ',tmp )
                        else :
                            #print('position = ',tmp)
                            #print('1st position =',tmp[0])
                            #print('\t=>,')
                            position=''+tmp[1:len(tmp)]
                            capt=0
                            position_found=1
                            tmp=''
                    if ((capt==1) and (row[1][a]!=' ')) :
                        tmp=tmp+row[1][a]
                    else : 
                        tmp=tmp+' '

                    if (position_found==1) :
                        tmp=[]

                #other values
                elif (position_found==1) :

                    if (row[1][a]!=chr(9)) :
                        tmp.append(row[1][a])

                a=a+1
            tmp_name=""+first_name+last_name
            content.append(tmp_name)
            content.append(position)
            for x in tmp :
                content.append(x)
            writer.writerow(content)
            
    file_r.close()
    file_w.close()

if __name__ == "__main__":
    principal()
    