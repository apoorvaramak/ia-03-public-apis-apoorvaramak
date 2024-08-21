#a function returning the NHL games played today and allowing the user to get the season standings of one of the teams playing
#
#Apoorva Ramakrishnan
#
#All usage information is stored in the README.md

import requests
from datetime import date
from api_key import api_key

#saving the URL and headers for all my API calls because they are reused
url = "https://api-hockey.p.rapidapi.com"
headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "api-hockey.p.rapidapi.com"
}

'''
    getting NHL (league 57) games from this season (2023) in the local timezone 
    ('America/Chicago'). 

    Inputs: 
        current_date (datetime): the date of whenever the code is run
    Returns:
        (JSON) the NHL games played on the current date and information about
        the games such as the scores, the scores per period, what time it starts
        and whether or not it is finished.
'''
def get_games(current_date):
    games_url = url + "/games"
    games_query_string = {"date": current_date,"league":"57","season":"2023", "timezone": 'America/Chicago'}
    games_response = requests.get(games_url, headers=headers, params=games_query_string)
    return games_response.json()["response"]

'''
    getting the list of the teams that are playing today, so that it can confirm 
    that the user is getting information about a team that is playing today

    Inputs:
        current_date (datetime): the date of whenever the code is run
    Returns:
        (Array) an array of the team names of the teams that are playing on a 
        current date
'''
def get_teams_playing_today(current_date):
    games_response = get_games(current_date)
    teams_list = []
    for game in games_response:
        teams = game["teams"]
        home_team = teams["home"]["name"]
        away_team = teams["away"]["name"]
        teams_list.append(home_team)
        teams_list.append(away_team)
    return teams_list
'''
    getting the id of a team based on the team name.

    Inputs:
        team_name (String): the name of the team that is being searched
    Returns:
        id (int): the id of the team that is entered
        0 (int): returned when the name of the team does not exist
'''
def get_team_id(team_name):
    search_url = url + "/teams"
    search_query_string = {"search": team_name}
    search_response = requests.get(search_url, headers = headers, params = search_query_string)
    if(search_response.json()["response"]):
        #if the response is not 0 then it is a valid team_name and will have an id
        team_id = search_response.json()["response"][0]["id"]
        return team_id
    else:
        return 0
    
'''
    prints the standings of the team this season (2023) and only from the NHL.

    Inputs:
        team_id (int): the id of the team that was found using the search endpoint
        and the get_team_id function above
    Returns: 
        Nothing (void): it is just used to retrieve the standings and print them out
        if the team_id is of one of the teams that is playing in the NHL today.
'''
def get_standings(team_id):
    standings_url = url + "/standings"
    standings_query_string = {"league":"57","season":"2023","team": team_id}
    standings_response = requests.get(standings_url, headers = headers, params = standings_query_string)
    standings = standings_response.json()["response"][0][0]
    
    print("games played: " + str(standings["games"]["played"]))
    print("games won: " + str(standings["games"]["win"]["total"]))
    print("games won in overtime: " + str(standings["games"]["win_overtime"]["total"]))
    print("games lost: " + str(standings["games"]["lose"]["total"]))
    print("games lost in overtime: " + str(standings["games"]["lose_overtime"]["total"]))
    print("place: #" + str(standings["position"]) + " in the " + standings["group"]["name"] + "\n")

if __name__ == "__main__":
    current_date = date.today()
    input("Press enter to get NHL games today!")
    games_response = get_games(current_date)
    print("NHL games played today: ")
    for game in games_response:
        teams = game["teams"]
        home_team = teams["home"]["name"]
        away_team = teams["away"]["name"]
        print("home team: " + home_team)
        print("away team: " + away_team)
        if(game["status"]["short"] == "FT"):
            #if the game is completed print the scores
            home_score = str(game["scores"]["home"])
            away_score = str(game["scores"]["away"])
            print("score (home team - away team): " + home_score + "-" + away_score + "\n")
        else:
            #if the game isn't done yet the scores will not display until it's over
            print("game in progress! \n")
    while True:
        team_name = input("enter a team above to get their 23-24 season standings!\n")
        if(get_team_id(team_name) == 0):
            #if the team name entered isn't a valid hockey team name
            print("Please enter a valid team name! \n")
            continue
        elif(team_name not in get_teams_playing_today(current_date)):
            #if the name entered is a valid team name but not playing today
            print("Please enter a team playing today! \n")
            continue
        else:
            #if the team entered is a valid team name and playing/played today
            get_standings(get_team_id(team_name))
            break
    print("Thank you! Go Blackhawks :)")




    





