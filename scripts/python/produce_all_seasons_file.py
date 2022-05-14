import glob
import csv

#Select files
files = glob.glob('../../csv/**/**/**/saisons/*.csv')

def produce():
    print('Start...')
    #Create new csv file to add all value
    with open('../../csv/England/D1/all_seasons.csv','a') as sfile:
        sfile.write('season,position,squad,match_played,victory,draw,lose,goal_for,goal_against,goal_difference,points,attendance,win_facup,win_eflcup,qualif_uefacup,status\n')
    for file in files:
        #Select year of the season
        season = file.split('/')[7]
        season = season[6:15]
        print(season)
        last = 1
        nbatt = 0
        #Calculate average attendance
        with open(file) as avgfile:
            avg = csv.reader(avgfile)
            j = 0
            for row in avg:
                if j>0 and row != []:
                    if int(season[0:4])>1991:
                        if int(season[0:4])>2016:
                            if row[14] != '':
                                nbatt+=int(row[14])
                        else:
                            if row[10] != '':
                                nbatt+=int(row[10])
                    else:
                        if row[11] != '':
                            nbatt+=int(row[11])
                    last = int(row[0])
                j+=1
            nbatt = nbatt / last
        with open(file) as csvfile:
            seasonfile = csv.reader(csvfile)
            pos = 0
            squad = ''
            played = 0
            v = 0
            d = 0
            l = 0
            gf = 0
            ga = 0
            gd = 0
            points = 0
            att = 0
            facup = 0
            eflcup = 0
            uefacup = 0
            status = 'Normal'
            i = 0
            for row in seasonfile:
                if i>0 and row != []:
                    #Take position of the squad in the file
                    pos = row[0]
                    #Find global status of the squad (depend of the position except for Relegated)
                    if int(pos) in [1,2,3,4,5,6]:
                        if int(pos) == 1:
                            status = 'Champion'
                        elif int(pos) == 2:
                            status = 'Runner-Up'
                        else:
                            status = 'Big Six'
                    else:
                        status = 'Normal'
                    #Get all necessary variable
                    squad = row[1]
                    played = row[2]
                    v = row[3]
                    d = row[4]
                    l = row[5]
                    gf = row[6]
                    ga = row[7]
                    #Check division format
                    if int(season[0:4])>1991:
                        gd = row[8]
                        points = row[9]
                        #Check if excepted variable is present
                        if int(season[0:4])>2016:
                            if row[14] != '':
                                att = round((((nbatt - int(row[14])) / nbatt) * 100),2)
                            else:
                                att = 0
                            #Look if FA Cup is in Notes
                            if 'FA Cup' in row[17]:
                                facup = 1
                            else:
                                facup = 0
                            #Look if League Cup is in Notes
                            if 'League Cup' in row[17]:
                                eflcup = 1
                            else:
                                eflcup = 0
                            #Look if UEFA Cup is in Notes
                            if 'UEFA' in row[17]:
                                uefacup = 1
                            else:
                                uefacup = 0
                            #Look if its a Regelated Team
                            if ('Failed' in row[17]) or ('Second Division' in row[17]) or ('Relegated' in row[17]) or ('Relégué' in row[17]):
                                status = 'Relegated'
                        else:
                            if row[10] != '':
                                att = round((((nbatt - int(row[10])) / nbatt) * 100),2)
                            else:
                                att = 0
                            #Look if FA Cup is in Notes
                            if 'FA Cup' in row[13]:
                                facup = 1
                            else:
                                facup = 0
                            #Look if League Cup is in Notes
                            if 'League Cup' in row[13]:
                                eflcup = 1
                            else:
                                eflcup = 0
                            #Look if UEFA Cup is in Notes
                            if 'UEFA' in row[13]:
                                uefacup = 1
                            else:
                                uefacup = 0
                            #Look if its a Regelated Team
                            if ('Failed' in row[13]) or ('Second Division' in row[13]) or ('Relegated' in row[13]) or ('Relégué' in row[13]):
                                status = 'Relegated'
                    else:
                        gd = row[9]
                        points = row[10]
                        if row[11] != '':
                            att = round((((nbatt - int(row[11])) / nbatt) * 100),2)
                        else:
                            att = 0
                        #Look if FA Cup is in Notes
                        if 'FA Cup' in row[14]:
                            facup = 1
                        else:
                            facup = 0
                        #Look if League Cup is in Notes
                        if 'League Cup' in row[14]:
                            eflcup = 1
                        else:
                            eflcup = 0
                        #Look if UEFA Cup is in Notes
                        if 'UEFA' in row[14]:
                            uefacup = 1
                        else:
                            uefacup = 0
                        #Look if its a Regelated Team
                            if ('Failed' in row[14]) or ('Second Division' in row[14]) or ('Relegated' in row[14]) or ('Relégué' in row[14]):
                                status = 'Relegated'
                    #Write information in file
                    with open('all_seasons.csv','a') as sfile:
                        sfile.write(f"{season},{pos},{squad},{played},{v},{d},{l},{gf},{ga},{gd},{points},{att},{facup},{eflcup},{uefacup},{status}\n")
                i+=1
    print('Done !')

if __name__ == "__main__":
    produce()