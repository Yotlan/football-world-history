import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('equipe')
@click.argument('stadiums')

def parser(equipe,stadiums):
    # Take years of the equipe
    equipe_year = equipe[-13:]
    equipe_begin_year = int(equipe_year[:4])
    equipe_end_year = int(equipe_year[5:9])
    # Take squad ID
    equipe_id = equipe.rpartition('--')[0].rpartition('/')[2]
    equipe_id = equipe_id.replace("_and_","_&_")
    equipe_name = equipe.rpartition('--')[0].rpartition('/')[2].replace("_"," ")
    equipe_name = equipe_name.replace("_and_","_&_")
    # Create database for the player in the squad
    with open(equipe) as csvfile:
        squad_file = csv.reader(csvfile)
        total=[]
        with open(f'output/sql/{equipe_id}-players.sql', 'a') as sql:
            i=0
            for line in squad_file:
                if i>1 and ("Total" not in line[0]):
                    player_name = line[0].rpartition('\\')[0]
                    player_nation = ''
                    if line[1] != '':
                        nation = line[1].split()
                        player_nation = ""
                        if len(nation) == 1:
                            player_nation = nation[0]
                        else:
                            player_nation = nation[1]
                    if line[6] == '':
                        sql.write(f"INSERT INTO PLAYERS_DIM (SQUAD_ID,START_DATE_ID,END_DATE_ID,PLAYER_ID,NATION,POST,AGE,MATCH_PLAYED_NB,MATCH_START,MATCH_MINUTES_PLAYED,GOAL_SCORED_NB,ASSISTS_NB,GOAL_WITHOUT_PENO_NB,PENO_SCORED,PENO_SHOOT,YELLOW_CARD_NB,RED_CARD_NB) VALUES(\"{equipe_name}\",{equipe_begin_year},{equipe_end_year},\"{player_name}\",\"{player_nation}\",\"{line[2]}\",{line[3]},{line[4]},{line[5]},0,0,0,0,0,0,0,0);\n")
                    else:
                        sql.write(f"INSERT INTO PLAYERS_DIM (SQUAD_ID,START_DATE_ID,END_DATE_ID,PLAYER_ID,NATION,POST,AGE,MATCH_PLAYED_NB,MATCH_START,MATCH_MINUTES_PLAYED,GOAL_SCORED_NB,ASSISTS_NB,GOAL_WITHOUT_PENO_NB,PENO_SCORED,PENO_SHOOT,YELLOW_CARD_NB,RED_CARD_NB) VALUES(\"{equipe_name}\",{equipe_begin_year},{equipe_end_year},\"{player_name}\",\"{player_nation}\",\"{line[2]}\",{line[3]},{line[4]},{line[5]},{line[6]},{line[8]},{line[9]},{line[10]},{line[11]},{line[12]},{line[13]},{line[14]});\n")
                elif "Total de l'équipe" in line[0]:
                    total=line
                i+=1

        with open(f'output/sql/{equipe_id}.sql', 'a') as sql:
            with open(stadiums) as stadium_csvfile:
                stadium_file = csv.reader(stadium_csvfile)
                i=0
                stade_name = ""
                for line in stadium_file:
                    if i>0 and line[4] == equipe_name:
                        stade_name = line[1]
                        squad_stats = total
                        squad_pd = squad_stats[9]
                        squad_gpeno = squad_stats[10]
                        squad_mpeno = squad_stats[11]
                        squad_tpeno = squad_stats[12]
                        squad_yc = squad_stats[13]
                        squad_rc = squad_stats[14]
                        sql.write(f"INSERT INTO SQUADS_DIM (SQUAD_ID,START_DATE_ID,END_DATE_ID,STADIUM_ID,ASSISTS_NB,GOAL_WITHOUT_PENO_NB,PENO_SCORED,PENO_SHOOT,YELLOW_CARD_NB,RED_CARD_NB) VALUES (\"{equipe_name}\",{equipe_begin_year},{equipe_end_year},\"{stade_name}\",{squad_pd},{squad_gpeno},{squad_mpeno},{squad_tpeno},{squad_yc},{squad_rc});\n")
                    i+=1

if __name__ == "__main__":
    parser()