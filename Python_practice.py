#create counties list
counties = ["Arapahoe","Denver","Jefferson"]

#county dictonary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#voter data dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
                
for i in range(len(counties_dict)):
    print(f'{counties_dict.keys()} county has {counties_dict.values()} registered voters')

