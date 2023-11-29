from model import *
from players import *

class players_handler():
    def __init__(self, source_type, file_path, file_sheet):
        self.source_type = source_type
        self.model = Model(self.source_type, file_path, file_sheet)
        self.data = self.model.data_set
        self.pd = pd
    
            
    def get_players_with_abilities_and_types(self):
        players = []
        
        for col, row in self.data.iterrows():
            
            contact_RHP = int(row.contact_RHP)
            contact_LHP = int(row.contact_LHP)
            power_RHP = int(row.power_RHP)
            power_LHP = int(row.power_LHP)
            vision = int(row.vision)
            disc = int(row.disc)
            clutch = int(row.clutch)
            speed = int(row.speed)
            steal = int(row.steal)
            
            calculated_values = self.set_players_calculated_values(contact_RHP, contact_LHP, power_RHP, power_LHP, vision, disc, clutch, speed, steal)
            
            
            player = {
                "ordr":str(row.order),
                "p_name":str(row.player_name),
                "bats":str(row.bats),
                "c_rhp":contact_RHP,
                "c_lhp":contact_LHP,
                "avg_c":calculated_values["avg_c"],
                "leadoff_rhp":calculated_values["leadoff_score_rhp"],
                "leadoff_lhp":calculated_values["leadoff_score_lhp"],
                "powerhouse_rhp":calculated_values["power_score_rhp"],
                "powerhouse_lhp":calculated_values["power_score_lhp"],
                "fundamentals_score_rhp":calculated_values["fundamentals_score_rhp"],
                "fundamentals_score_lhp":calculated_values["fundamentals_score_lhp"],
                "offroad_score_rhp":calculated_values["offroad_score_rhp"],
                "offroad_score_lhp":calculated_values["offroad_score_lhp"],
                "c_abi_rhp":calculated_values["c_abi_rhp"],
                "c_abi_lhp":calculated_values["c_abi_lhp"],
                "bs_abi":calculated_values["bs_abi"],
                "p_abi_rhp":calculated_values["p_abi_rhp"],
                "p_abi_lhp":calculated_values["p_abi_lhp"],
                "p_rhp":power_RHP,
                "p_lhp":power_LHP,
                "vis":vision,
                "disc":disc,
                "clt":clutch,
                "spd":speed,
                "stl":steal,
                "mlb":row.MLB,
                "pos":str(row.pos)
            }
            
            
            players.append(player)
            
        return players
    
    # retornar los valores calculados por cada jugador
    def set_players_calculated_values(self, contact_RHP, contact_LHP, power_RHP, power_LHP, vision, disc, clutch, speed, steal):
        
        player_formula = Player()
          
        # averages 
        avg_contact = player_formula.get_LHP_RHP_avg(contact_RHP, contact_LHP)
            
        # Abilities 
        
        # contact
        contact_ability_rhp = player_formula.get_contact_ability(contact_RHP,vision,disc,clutch)
        
        contact_ability_lhp = player_formula.get_contact_ability(contact_LHP,vision,disc,clutch)
        
        avg_cont_ability = player_formula.get_LHP_RHP_avg(contact_ability_rhp,contact_ability_lhp)
        
        # power 
        power_ability_rhp = player_formula.get_power_ability(
            power_RHP,clutch)
        
        power_ability_lhp = player_formula.get_power_ability(
            power_LHP,clutch)
        
        avg_power_ability = player_formula.get_LHP_RHP_avg(contact_ability_rhp,contact_ability_lhp)
        
        
        # batting abillity
        bating_ability = player_formula.get_batting_ability(avg_cont_ability,avg_power_ability)
        
        
        # baserunning ability
        bs_ability = player_formula.get_bs_ability(speed,steal)
        
        # leadoff
        leadoff_score_rhp = player_formula.get_leadoff_score(contact_RHP, bs_ability, contact_ability_rhp)
        
        leadoff_score_lhp = player_formula.get_leadoff_score(contact_LHP, bs_ability, contact_ability_lhp)
        
        # power_house
        power_score_rhp = player_formula.get_type_score([1,power_RHP, clutch, contact_RHP,vision])
        
        power_score_lhp = player_formula.get_type_score([1,power_LHP, clutch, contact_LHP,vision])
        
        # Fundamentals
        fundamentals_score_rhp = player_formula.get_type_score([2,vision, clutch, disc,contact_RHP])
        
        fundamentals_score_lhp = player_formula.get_type_score([2,vision, clutch, disc,contact_LHP])
        
        # offroad
        offroad_score_rhp = player_formula.get_type_score([3,contact_ability_rhp, power_ability_rhp, bs_ability,clutch])
        
        offroad_score_lhp = player_formula.get_type_score([3,contact_ability_lhp, power_ability_lhp, bs_ability,clutch])
        
        # all attributes calculated to return. 
        attrs_calculated = {
            "avg_c":avg_contact,
            "c_abi_rhp":contact_ability_rhp,
            "c_abi_lhp":contact_ability_lhp,
            "avg_c_abi":avg_cont_ability,
            "bs_abi":bs_ability,
            "p_abi_rhp":power_ability_rhp,
            "p_abi_lhp":power_ability_lhp,
            "avg_p_abi":avg_power_ability,
            "leadoff_score_rhp":leadoff_score_rhp,
            "leadoff_score_lhp":leadoff_score_lhp,
            "power_score_rhp":power_score_rhp,
            "power_score_lhp":power_score_lhp,
            "fundamentals_score_rhp":fundamentals_score_rhp,
            "fundamentals_score_lhp":fundamentals_score_lhp,
            "offroad_score_rhp":offroad_score_rhp,
            "offroad_score_lhp":offroad_score_lhp
        }
        
        return attrs_calculated

