def main():

    hockey_team = {
        'name' : 'Maple Leafs',
        'city' : 'Toronto',
        'players' : [
            'matthews',
            'marner',
            'nylander'
        ],
        'games' :[
            {
                'opponent' : 'Canadiens',
                'goals for' : 6,
                'goals against' : 2, 
            },
            {
                'opponent' : 'Ottawa',
                'goals for' : 2,
                'goals against' : 3,
            }
        ]

   }

    new_game = {
    'opponent' : 'Boston', 
    'goals for' : 8,
    'goals against' : 0
   }

    hockey_team['games'].append()

    print_team_info(hockey_team)
    add_players(hockey_team,('giordano', 'reilly', ' engvall',))
    )


    return





def add_players(team, new_players):
    
    team['players'].extend(new_players)

    team['players'].sort()




    return

def print_team_info(team):
        
     team_name = team['name']
     team_city = team['city']

     print(f'The players on the {team_city} {team_name} are:')

     for p in team['players']:
        print(f'-{p.capitalize()}')



    


     




if __name__ == '__main__':
    main()