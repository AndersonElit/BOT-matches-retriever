import pickle
from bash import bash
import numpy as np

class Utils:

    def __init__(self):

        self.list = []

    def get_years(self, text):

        new_list = text.split()
        years = new_list[0].split('-')
        years_list = [int(years[0]), int(years[1])]
        return years_list

    def matches_list(self, text, teams_list):

        text_list = text.splitlines()
        new_list = []
        
        # depure non util lines
        for item in text_list:

            """
            if item == ',,,,,,,,,,,' or item == '' or item == ' ':
                pass
            else:
                new_list.append(item)
            """
            if item == ',,,,,,,,,,,,,' or item == '' or item == ' ':
                pass
            else:
                new_list.append(item)
        
        new_list_mod = new_list[2:]
        match_list = []

        # extract info for each match:
        for item in new_list_mod:
            """
            item_list = item.split(',')
            goals = item_list[5].split('–')
            # [date, local, visit, goalslocal, goalsvisit]
            data_set = [int(item_list[0]), item_list[4], item_list[6], int(goals[0]), int(goals[1])]
            match_list.append(data_set)
            """
            item_list = item.split(',')
            goals = item_list[6].split('–')
            # [date, local, visit, goalslocal, goalsvisit]
            data_set = [int(item_list[0]), item_list[4], item_list[8], int(goals[0]), int(goals[1])]
            match_list.append(data_set)

        # rearrange matches per date
        sorted_list = sorted(match_list, key=lambda date: date[0])
        matches_per_date = (len(teams_list))/2
        dates_num = len(sorted_list)/matches_per_date
        split_per_date = np.array_split(sorted_list, dates_num)

        return split_per_date

    def serialize_teams(self, years, teams_list):

        file_name = f"teams_{str(years[0])}_{str(years[1])}"
        binary_file = open(file_name, "wb")
        pickle.dump(teams_list, binary_file)
        binary_file.close()

        #verify if the teams were saved
        file = open(file_name, "rb")
        list = pickle.load(file)
        print(list)

        #move file to teams dir
        command = 'mv ' + file_name + ' premier_league/teams/'
        bash(command)

        return ''

    def serialize_matches(self, years, matches_list):

        file_name = f"matches_{str(years[0])}_{str(years[1])}"
        binary_file = open(file_name, "wb")
        pickle.dump(matches_list, binary_file)
        binary_file.close()

        #verify if the teams were saved
        file = open(file_name, "rb")
        list = pickle.load(file)
        print(list)

        #move file to teams dir
        command = 'mv ' + file_name + ' premier_league/matches/'
        bash(command)

        return ''