import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('saison')

def parser(saison):
    # Take years of the season
    saison_year = saison[-13:]
    saison_begin_year = saison_year[:4]
    saison_end_year = saison_year[5:9]
    # Create database for the squad in the season
    with open(saison) as csvfile:
        file = csv.reader(csvfile)
        with open(f'output/sql/saison{saison_begin_year}-{saison_end_year}.sql', 'a') as sql:
            i=0
            haveExpectedGoal = False
            for line in file:
                if "xG" in line:
                    haveExpectedGoal = True
                if i>0 and haveExpectedGoal:
                    best_scorers = line[15].rpartition('- ')[0]
                    names = best_scorers.split()
                    nb_names = len(names)
                    first_best_scorer=''
                    second_best_scorer=''
                    if nb_names == 4:
                        first_best_scorer = names[0] + ' ' + names[1]
                        second_best_scorer = names[2] + ' ' + names[3]
                    elif (nb_names == 3) or (nb_names > 4) or (nb_names == 0):
                        # Verify if first player have just one name or is it's the second player
                        with open("output/error.log", 'a') as log:
                            log.write(f"NEED TO CHECK THE {i} TH OF THE CSV FILE {saison}\n")
                        first_best_scorer = line[15].rpartition('- ')[0]
                        second_best_scorer = line[15].rpartition('- ')[0]
                    elif nb_names == 2:
                        first_best_scorer = names[0] + ' ' + names[1]
                        second_best_scorer = names[0] + ' ' + names[1]
                    elif nb_names == 1:
                        first_best_scorer = names[0]
                        second_best_scorer = names[0]
                    sql.write(f"INSERT INTO SEASONS_FACTS_PER_SQUAD (SQUAD_ID,START_DATE_ID,END_DATE_ID,FIRST_BEST_SCORER_ID,SECOND_BEST_SCORER_ID,PRINCIPAL_GOALKEEPER_ID,MATCH_NB,VICTORY_NB,DRAW_NB,LOSE_NB,GOAL_SCORED_NB,GOAL_TAKEN_NB,SQUAD_POINT,PLACE,FOLLOWER_NB) VALUES (\"{line[1]}\",{saison_begin_year},{saison_end_year},\"{first_best_scorer}\",\"{second_best_scorer}\",\"{line[16]}\",{line[2]},{line[3]},{line[4]},{line[5]},{line[6]},{line[7]},{line[9]},{line[0]},{line[14]});\n")
                elif i>0 and not haveExpectedGoal:
                    best_scorers = line[11].rpartition('- ')[0]
                    names = best_scorers.split()
                    nb_names = len(names)
                    first_best_scorer=''
                    second_best_scorer=''
                    if nb_names == 4:
                        first_best_scorer = names[0] + ' ' + names[1]
                        second_best_scorer = names[2] + ' ' + names[3]
                    elif nb_names == 3:
                        # Verify if first player have just one name or is it's the second player
                        with open("output/error.log", 'a') as log:
                            log.write(f"NEED TO CHECK THE {i} TH OF THE CSV FILE {saison}\n")
                        first_best_scorer = names[0] + ' ' + names[1] + ' ' + names[2]
                        second_best_scorer = names[0] + ' ' + names[1] + ' ' + names[2]
                    elif nb_names == 2:
                        first_best_scorer = names[0] + ' ' + names[1]
                        second_best_scorer = names[0] + ' ' + names[1]
                    elif nb_names == 1:
                        first_best_scorer = names[0]
                        second_best_scorer = names[0]
                    sql.write(f"INSERT INTO SEASONS_FACTS_PER_SQUAD (SQUAD_ID,START_DATE_ID,END_DATE_ID,FIRST_BEST_SCORER_ID,SECOND_BEST_SCORER_ID,PRINCIPAL_GOALKEEPER_ID,MATCH_NB,VICTORY_NB,DRAW_NB,LOSE_NB,GOAL_SCORED_NB,GOAL_TAKEN_NB,SQUAD_POINT,PLACE,FOLLOWER_NB) VALUES (\"{line[1]}\",{saison_begin_year},{saison_end_year},\"{first_best_scorer}\",\"{second_best_scorer}\",\"{line[12]}\",{line[2]},{line[3]},{line[4]},{line[5]},{line[6]},{line[7]},{line[9]},{line[0]},{line[10]});\n")
                i+=1


if __name__ == "__main__":
    parser()