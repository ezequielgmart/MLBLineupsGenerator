from players_handler import * 
import os
from lineup_handler import *

class Main():
    def __init__(self, source_type):
        self.data = players_handler(source_type).get_players_with_abilities_and_types()
        self.pd = pd
        
    def main(self):
        while True:
            os.system('cls')
            pitcher_hand = int(input("Enter pitcher hand. 1 RHP / 2 LHP: "))
            
            data = self.get_best_scores_by_phand(self.data, pitcher_hand, 0)
            catchers_availables = self.get_best_scores_by_phand(self.data, pitcher_hand, "C")
            
            lineup_generator = lineup_handler()
            
            lineup = lineup_generator.get_lineup(data, catchers_availables, pitcher_hand)
            
            # print(lineup)
            # Render the line up
            
            if pitcher_hand == 1:
                pitcher_hand = "RHP"
            elif pitcher_hand == 2:
                pitcher_hand = "LHP"
            
            print(f"Showing lineup starting pitcher: {pitcher_hand}")
            print("Order  | Player       | pos   | leadoff     |    offroad    |    powerhouse      | fundamentals     ")
            place = 1  
            for item in lineup:
                print(f"{place:<7} {item["Player"]:<16} {item["Pos"]:<7} {item["leadoff"]:<16} {item["offroad"]:<16} {item["powerhouse"]:<16} {item["fundamentals"]:<16}")
                place += 1  
        
            input("Generate lineup again...")
    def get_all_players(self, dataset):
        
        dataframe = self.pd.DataFrame(dataset)
        
        players = []
        
        for col, row in dataframe.iterrows():
            player = {
                "Player":row.p_name,
                "Leadoff_avg":row.leadoff_avg,
                "Leadoff_rhp":row.leadoff_rhp,
                "Leadoff_lhp":row.leadoff_lhp,
                "Pos":row.pos
            }
            
            players.append(player)
            
        return players
    
    
    def available_catchers(self):
        all_players = self.get_best_scores_by_phand()
        return all_players
            
    def set_dataframe(self, data):
         dataframe = self.pd.DataFrame(data)
         return dataframe
    
        
    def get_best_scores_by_phand(self, dataset, pitcher_hand, position):
        dataframe = self.pd.DataFrame(dataset)
        
        players = []
        
        for col, row in dataframe.iterrows():
                
                if pitcher_hand == 1:
                    # RHP
                    
                    batter_type = max([row.leadoff_rhp,row.powerhouse_rhp, row.fundamentals_score_rhp, row.offroad_score_rhp])
                    
                    player = {
                        "Player":row.p_name,
                        "leadoff":row.leadoff_rhp,
                        "powerhouse":row.powerhouse_rhp,
                        "fundamentals":row.fundamentals_score_rhp,
                        "offroad":row.offroad_score_rhp,
                        "Pos":row.pos,
                        "bats":row.bats
                    }
                    
                    if position == 0: 
                        players.append(player)
                    elif position != 0:
                        if player["Pos"] == position:
                            players.append(player)
                        else:
                            pass
                    else:
                        pass    
                    
                    
                elif pitcher_hand == 2:
                    # LHP
                    batter_type = max([row.leadoff_lhp,row.powerhouse_lhp, row.fundamentals_score_lhp, row.offroad_score_lhp])
                
                    player = {
                        "Player":row.p_name,
                        "leadoff":row.leadoff_lhp,
                        "powerhouse":row.powerhouse_lhp,
                        "fundamentals":row.fundamentals_score_lhp,
                        "offroad":row.offroad_score_lhp,
                        "better_type": batter_type,
                        "Pos":row.pos,
                        "bats":row.bats
                    }
                    
                    if position == 0: 
                        players.append(player)
                    elif position != 0:
                        if player["Pos"] == position:
                            players.append(player)
                        else:
                            pass
                    else:
                        pass   
                    
                else:
                    player = [0]
                    
                    players.append(player)
            
        return players
                
players_main = Main('excel')

players_main.main()
