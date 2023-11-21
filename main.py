from players_handler import * 
import os
from lineup_handler import *
from settings_handler import *

class Main():
    def __init__(self, source_type, file_path, sheet):
        self.data = players_handler(source_type, file_path, sheet).get_players_with_abilities_and_types()
        self.pd = pd
        
    def main(self, source_type, file_path, sheet, team, mode):
        
        function_selected = input(f"Press A to get the whole roster or L to get lineup... ").upper()
        
        if function_selected == "L":
            self.view_lineup_generator(source_type, file_path, sheet, team, mode)
        elif function_selected == "A":
            self.view_all_players(source_type, file_path, sheet, team, mode)
        else: 
            print("Unable function at this time... ")
        
    
    def view_lineup_generator(self, source_type, file_path, sheet, team, mode):
        while True:
            os.system('cls')
            
            self.view_table_with_whole_roster(source_type, file_path, sheet, team, mode)
            pitcher_hand = int(input("Enter pitcher hand. 1 RHP / 2 LHP: "))
            
            data = self.get_best_scores_by_phand(self.data, pitcher_hand, 0)
            catchers_availables = self.get_best_scores_by_phand(self.data, pitcher_hand, "C")
            
            lineup_generator = lineup_handler()
            
            is_any_player_excluded = input("Player name of order in case that you wanna exclude him of the roster, or press N to get the whole roster: ")
            
            if is_any_player_excluded == "n" or is_any_player_excluded == "N":
                excluded_player = 0
                lineup = lineup_generator.get_lineup(data, catchers_availables, 0)
            else:
                excluded_player = is_any_player_excluded
                lineup = lineup_generator.get_lineup(data, catchers_availables, excluded_player)
                
            self.render_players_in_lineup(pitcher_hand, lineup)
            
            input("Generate lineup again...")  
        
        
    def view_all_players(self, source_type, file_path, sheet, team, mode):
        while True:
            os.system('cls')
            
            self.view_table_with_whole_roster(source_type, file_path, sheet, team, mode)
            
            input("")   
            self.main(source_type, file_path, sheet, team, mode)
    
    def view_table_with_whole_roster(self, source_type, file_path, sheet, team, mode):
        
        self.render_header_information_banner(source_type, file_path, sheet, team, mode)
            # option
            
        data = self.get_all_players(self.data)
        
        self.render_players_all(data)
        
        
        print("************************************************************")   
                
    def get_all_players(self, dataset):
        
        dataframe = self.pd.DataFrame(dataset)
        
        players = []
        
        for col, row in dataframe.iterrows():
            player = {
                    "order":row.ordr,
                    "Player":row.p_name,
                    "leadoff_RHP":row.leadoff_rhp,
                    "leadoff_LHP":row.leadoff_lhp,
                    "powerhouse_RHP":row.powerhouse_rhp,
                    "powerhouse_LHP":row.powerhouse_lhp,
                    "fundamentals_RHP":row.fundamentals_score_rhp,
                    "fundamentals_LHP":row.fundamentals_score_lhp,
                    "offroad_RHP":row.offroad_score_rhp,
                    "offroad_LHP":row.offroad_score_lhp,
                    "Pos":row.pos,
                    "bats":row.bats
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
                        "order":row.ordr,
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
                        "order":row.ordr,
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
    
        
    # RENDER METHODS
    def render_header_information_banner(self, source_type, file_path, sheet, team, mode):
        print(f"Reading information from Source: {source_type} | Path:{file_path}  | Page:{sheet} | Team: {team} | Mode:{mode}")
        print(f"**********************************************************************************************")
            
    def render_players_in_lineup(self, pitcher_hand = 0, lineup = 0):
        
        if pitcher_hand == 1:
            pitcher_hand = "RHP"
        elif pitcher_hand == 2:
            pitcher_hand = "LHP"
        else:
            pitcher_hand = "N/A"  
                
        print(f"Showing lineup starting pitcher: {pitcher_hand}")
        print(f"********************************************************************************************************************")
        print("       |              |        |       |             |               |                    |      ")  
        print("Order  | Player       | Bats   | Pos   | Leadoff     |    Offroad    |    Powerhouse      | Fundamentals     ")  
        print("       |              |        |       |             |               |                    |      ")  
        print(f"********************************************************************************************************************")
        
        place = 1  
        for item in lineup:
            print(f"{place:<7} {item["Player"]:<16} {item["bats"]:<7} {item["Pos"]:<7} {item["leadoff"]:<16} {item["offroad"]:<16} {item["powerhouse"]:<16} {item["fundamentals"]:<16}")
            place += 1  
    
    def set_settings(self):  
        pass     
    def render_players_all(self, roster):
        
                
        print(f"Showing All players")
        print(f"***********************************************************************************************************")
        print("       |               |        |       |             |               |              |      ")  
        print("       |               |        |       | Leadoff     |    Offroad    |   Powerhouse |   Fundamentals    ")    
        print("Order  | Player        | Bats   | Pos   | RHP   LHP   |    RHP   LHP  |   RHP   LHP  |   RHP   LHP   ")   
        print("       |               |        |       |             |               |              |     ")   
        print(f"***********************************************************************************************************")
        
        for item in roster:
            print(f"{item["order"]:<7} {item["Player"]:<16} {item["bats"]:<10} {item["Pos"]:<4} {item["leadoff_RHP"]:<7} {item["leadoff_LHP"]:<7}  {item["offroad_RHP"]:<7}{item["offroad_LHP"]:<7} {item["powerhouse_RHP"]:<7}{item["powerhouse_LHP"]:<7} {item["fundamentals_RHP"]:<7}{item["fundamentals_LHP"]:<7}")

os.system("cls")
print("Lineup Generator ")
print("************************************************************************************************************************************************************")

mode_selected = input("Press Y to run in default mode. ").upper()
print("************************************************************************************************************************************************************")    

if mode_selected == "Y":
    settings  = Settings()
    settings.default_config()  
    
    players_main = Main(settings.source_type,settings.path, settings.sheet)
    players_main.main(settings.source_type,settings.path, settings.sheet, settings.team, settings.mode)
else:
    print("No available.")
    

# print("Set up the preferences: ")
# print(f"1. The default method will use the settings by default where the excel file we are reading the information from is {FILE_PATH}")
# mode = input("2. In the event that you desire to use a different one, please press N. Otherwhise, press any key.. ").upper()
# file_sheet = input("3. Enter D to set up the excel sheet as a default settings however, write down the sheet name where you want to read from:   ").upper()    
# if mode == "N":
    
#     file_path = input("3. Enter D to set up the excel file as a default settings or write down the file name / file path where you want to read from:   ").upper()
#     file_sheet = input("4. Enter D to set up the excel sheet as a default settings however, write down the sheet name where you want to read from:   ").upper()
    
#     print("Default method is the only one allowed a this time.")
#     print("************************************************************************************************************************************************************")   

# else:
#     file_path = "D"
#     mode = "Default"
#     if file_path == "D" and file_sheet == "D":    
#         players_main = Main('excel',FILE_PATH, FILE_SHEET)
#         players_main.main('excel',FILE_PATH, FILE_SHEET, TEAMS[0], mode)
#     else:
#         print("No disponible.")