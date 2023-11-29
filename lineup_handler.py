
class lineup_handler():
    
    def __init__(self):
        self.spots_available = 3
        
    def get_lineup(self, data, catchers_availables, excluded_player_list):
        picked_players = []
        
        best_hitter = 1
        powerhouse_spots = 3
        leadoff_spots = 2
        fundamentals_spots = 2
        
        for player in data:
            if player["is_mlb"] == "No":
                data.remove(player)
            else:
                pass
        
        if excluded_player_list != 0:
            
            for item in data:
                for player_excluded in excluded_player_list:
                    if item["Player"] == player_excluded or item["order"] == player_excluded:
                        data.remove(item)
                    else:
                        pass

        while best_hitter > 0:
            
            attr='offroad'
            
            for player in data:
                max_offroad = max(data, key=lambda x: x[attr])
                picked_players.append(max_offroad)
                data.remove(max_offroad)
                break
            best_hitter-=1
        
        while powerhouse_spots > 0:
            
            attr='powerhouse'
            
            for player in data:
                max_powerhouse = max(data, key=lambda x: x[attr])
                picked_players.append(max_powerhouse)
                data.remove(max_powerhouse)
                break
            powerhouse_spots-=1
        
        while leadoff_spots > 0:
            
            attr='leadoff'
            
            for player in data:
                max_powerhouse = max(data, key=lambda x: x[attr])
                picked_players.append(max_powerhouse)
                data.remove(max_powerhouse)
                break
            leadoff_spots-=1
        
        
        while fundamentals_spots > 0:
            attr='fundamentals'
            
            for player in data:
                max_powerhouse = max(data, key=lambda x: x[attr])
                picked_players.append(max_powerhouse)
                data.remove(max_powerhouse)
                break
            fundamentals_spots-=1
    
        # in case there's no catchers on the lineup
        position_to_search = "C" 
        
        for item in picked_players:
            if position_to_search in item["Pos"]:
                are_catchers = True
            else:
                are_catchers = False
         
               
        if are_catchers:
            # Si ya tiene un catcher, el 9no bate sera el 3er mejor leadoff
            attr='leadoff'
            
            # if excluded_player != 0:
            
            #     for item in data:
            #         if item["Player"] == excluded_player or item["order"] == excluded_player:
            #             data.remove(item)
            #         else:
            #             pass
            
            for player in data:
                max_powerhouse = max(data, key=lambda x: x[attr])
                picked_players.append(max_powerhouse)
                data.remove(max_powerhouse)
                break
        else:
            # en caso de no tener catchers, pues buscaremos el mejor catcher disponible, en este caso lo unico que tomaremos en cuenta es que sea de la mano contraria al pitcher. 

            attr='leadoff'
            
            for player in catchers_availables:
                max_powerhouse = max(catchers_availables, key=lambda x: x[attr])
                picked_players.append(max_powerhouse)
                data.remove(max_powerhouse)
                break
         
        # The order on the lineup 
        # 1. 1st leadoff
        # 2. 2nd best leadoff
        # 3. Best hitter
        # 4. 1st Best powerhouse
        # 5. 2nd best powerhouse
        # 6. 1st Best fundamentals
        # 7. 2nd Best fundamentals
        # 8. 3nd best powerhouse
        # 7. 3rd leadoff / catcher
        
        
        lineup = [
            picked_players[4],
            picked_players[5],
            picked_players[0],
            picked_players[1],
            picked_players[2],
            picked_players[6],
            picked_players[3],
            picked_players[7],
            picked_players[8]
        ]
        
        return lineup
     
    def get_top_three(self, players, attr):
        top_three_players_by_attr = []
        
        top_three_players_by_attr = self.set_best_players_by_attr(players, attr)
        
        return top_three_players_by_attr
        
    def set_best_players_by_attr(self, players_list, attr_to_filter):
        lineup = []
        while self.spots_available > 0:
            for player in players_list:
                max_dict = max(players_list, key=lambda x: x[attr_to_filter])
                lineup.append(max_dict)
                players_list.remove(max_dict)
                break
            self.spots_available -=1
        return lineup
    
    def remove_players_already_picked(self, players_picked, players_list):
        available_players = [element for element in players_list if element not in players_picked]
        return available_players
    
 
            
            
