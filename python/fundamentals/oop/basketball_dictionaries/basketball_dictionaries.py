class Player:
  new_team = []

  def __init__(self, dict_list):
    [setattr(self, key, dict_list[key]) for key in dict_list]

  @classmethod
  def get_team(cls, team_list):
    for i in team_list:
      player = Player(i)
      cls.new_team.append(player)
    return cls.new_team

  @classmethod
  def view_team(cls):
    for team_dict in cls.new_team:
      print(team_dict.__dict__)

kevin = {
      "name": "Kevin Durant", 
      "age":34, 
      "position": "small forward", 
      "team": "Brooklyn Nets"
}
jason = {
      "name": "Jason Tatum", 
      "age":24, 
      "position": "small forward", 
      "team": "Boston Celtics"
}
kyrie = {
      "name": "Kyrie Irving", 
      "age":32,
        "position": "Point Guard", 
      "team": "Brooklyn Nets"
}
    
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


players = [
    {
      "name": "Kevin Durant", 
      "age":34, 
      "position": "small forward", 
      "team": "Brooklyn Nets"
    },
    {
      "name": "Jason Tatum", 
      "age":24, 
      "position": "small forward", 
      "team": "Boston Celtics"
    },
    {
      "name": "Kyrie Irving", 
      "age":32,
        "position": "Point Guard", 
      "team": "Brooklyn Nets"
    },
    {
      "name": "Damian Lillard", 
      "age":33,
        "position": "Point Guard", 
      "team": "Portland Trailblazers"
    },
    {
      "name": "Joel Embiid", 
      "age":32,
        "position": "Power Foward", 
      "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# new_team = []
# for list_dict in players:
#   player = Player(list_dict)
#   new_team.append(player)

team1 = Player.get_team(players)

Player.view_team()
