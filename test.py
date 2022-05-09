import requests as r

# one class as a UI
# one class as player

# player is just to hold information
# info is in get_info()

# the ui will be the ability to search for a player
# search for a team
# everything will happen within the UI

# Make a user search for player in API
# listed with dictionary of name number team position
# if user_input is in data, return the dictionary, else print that player is not a part of the NBA


class Basketball_UI:

    def __init__(self):
        pass

    def get_info(self):
        dict = {}
        end_list = []
        while True:
            print('Welcome to our NBA Player Files ========== (If you typed in the wrong name, simply type "del" to remove player. ======== Pick your Favorite Players Here: ')
            user_input = input('What player do you want to search for?')
            data = r.get('https://www.balldontlie.io/api/v1/players?search=' + user_input).json()
            firstname = data['data'][0]['first_name'] 
            lastname = data['data'][0]['last_name']
            full_name = firstname + ' ' + lastname
            team = data['data'][0]['team']['full_name']
            position = data['data'][0]['position']
            conference = data['data'][0]['team']['conference']

            my_player = Player(full_name, team, position, conference)
            dict['player'] = my_player

            x = dict['player'].full_name, team, position, conference
            end_list.append(x[0])
            print(x)
            new_question = input('Are you finished selecting Players? y/n')
            if new_question == 'n':
                continue
            elif new_question == 'del':
                end_list.pop()
            else:
                print(f"Thanks for searching! Here are the players you've searched: {end_list}")
                break

    def player_team_name(self):
        team_name = []
        email_name = []
        print('Now that you have selected your players, We need to give them a new team name!')
        play_ques = input('Give your team a name: ').title()
        team_name.append(play_ques)
        print(f"You have selected {team_name} as your team name!")
        print()
        print("This content is currently being updated. Your submission will be in soon. Until then, feel free to press '1' to subscribe to our channel.")
        last_one = input('Press 1 to subscribe or 2 to quit.')
        if last_one == '1':
            x = input('What is your email?')
            email_name.append(x)
            print("Is this correct? Press 1 for Yes, Press 2 for No.")
            y = input('Press 1 for Yes, Press 2 for No.')
            if y == '1':
                print(f'Email confirmed! Thank you for subscribing. Your team {team_name} along with email: {email_name} have been successfully saved.')
            elif y == '2':
                print('Your email cannot be verifed. Please try again later.')
        elif last_one == '2':
            print('Thanks for Browsing!')

          
    
# final step is to make your starting lineup based off of the player you have selected



class Player:

    def __init__(self, full_name, team, position, conference):
        self.full_name = full_name
        self.team = team
        self.position = position
        self.conference = conference

my_Basketball_UI = Basketball_UI()
my_Basketball_UI.get_info()
my_Basketball_UI.player_team_name()
# ask the player specific questions
# if user input !=

# print('NBA Info List: You have looked up:')

# get_info()

# i want to make a function that appends that players jersey number
# the api seems to have forgetten it
# could also make this a basketball trivia game in the future


# this code still has bugs