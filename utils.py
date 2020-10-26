
class Utils:

    def __init__(self):

        self.list = []

    def get_years(self, text):

        new_list = text.split()
        years = new_list[0].split('-')
        years_list = [int(years[0]), int(years[1])]
        return years_list

    def matches_list(self, text):

        text_list = text.splitlines()
        
        # depure non util lines
        for item in text_list:

            if item == ',,,,,,,,,,,' or item == '' or item == ' ':
                pass
            else:
                self.list.append(item)
        
        list = self.list
        new_list = list[2:]

        # extract info for each match:
        for item in new_list:

            self.list = []
            item_list = item.split(',')
            goals = item_list[5].split('–')
            # [date, local, visit, goalslocal, goalsvisit]
            data_set = [int(item_list[0]), item_list[4], item_list[6], int(goals[0]), int(goals[1])]
            self.list.append(data_set)

        list = self.list
        sorted_list = sorted(list, key=lambda date: date[0])

        # rearrange matches per date
        count = 1

        for item in list:

            new_list = []

            if item[0] == count:
                new_list.append(item)

            list.append(new_list)
            count += 1

        list = self.list

        return list