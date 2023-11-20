def render_player_row(self, player, abilities_and_types_score):
        
        print(f"{player.bats_hand:<3}|{player.name:<15}|{player.position:<5}|Leadoff:  {abilities_and_types_score['leadoff_score']:<5}| Powerhouse: {abilities_and_types_score['powerhouse_score']:<5}|Fundamentals: {abilities_and_types_score['fundamentals_score']:<5}|Offroad {abilities_and_types_score['offroad_score']:<7} | Player Type: {abilities_and_types_score['better_arquetype']:<7}")
        
def render_header(self, pitcher_hand):
        print("-----------------------------------------------------------------------------------")
        if pitcher_hand == 1:
            print(f"List of players | RHP")
        elif pitcher_hand == 2:
            print(f"List of players | LHP")
        else:
            print(f"List of players | Pitcher hand not selected")
        print("-----------------------------------------------------------------------------------")
        
