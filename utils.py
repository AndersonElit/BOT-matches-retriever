import pickle
from bash import bash

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
        
        # depure non util lines
        for item in text_list:

            if item == ',,,,,,,,,,,' or item == '' or item == ' ':
                pass
            else:
                self.list.append(item)
        
        list = self.list
        new_list = list[2:]
        self.list = []

        # extract info for each match:
        for item in new_list:

            item_list = item.split(',')
            goals = item_list[5].split('–')
            # [date, local, visit, goalslocal, goalsvisit]
            data_set = [int(item_list[0]), item_list[4], item_list[6], int(goals[0]), int(goals[1])]
            self.list.append(data_set)

        list = self.list
        # rearrange matches per date
        sorted_list = sorted(list, key=lambda date: date[0])
        self.list = []
        limit = len(teams_list)/2
        start = 0
        end = limit
        new_length = len(sorted_list) - limit

        while end <= new_length:

            date = sorted_list[start:end]
            self.list.append(date)
            start += limit
            end += limit
        
        last_item = sorted_list[end:]
        self.list.append(last_item)

        final_list = self.list

        return final_list

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
        msg = "porceso exitoso"

        return msg

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
        command = 'mv ' + file_name + ' premier_league/teams/'
        bash(command)
        msg = "porceso exitoso"

        return msg