from settings import * 

class Player():
    
    def __init__(self):
        pass
        
    def get_average_arquetype_score(self, leadoff, powerhouse, fundamental, offroad):
        return round(self.get_attr_avg([leadoff,powerhouse, fundamental, offroad]), 1)    
    
            
    def get_max_arquetype_score(self, leadoff, powerhouse, fundamental, offroad):
        arquetypes_score = {
            "Leadoff": leadoff,
            "Powerhouse": powerhouse,
            "Fundamentals": fundamental,
            "Offroad": offroad
        }
        
            
        return max(arquetypes_score, key=arquetypes_score.get)   
    

    # This return a score by attribute given. attr could be the vision, contact, wathever, and the score_by_attr is the score that attribute represents in order to get the arquetype final puntuation  
    def get_score_by_attr(self,attr,score_by_attr):
        return ((attr / 100) * score_by_attr)
    
    def get_LHP_RHP_avg(self, RHP, LHP):
        return self.get_attr_avg([RHP, LHP])
    
    def get_attr_avg(self,attrs):
        return sum(attrs) / len(attrs)
    
    # Los abilities
    def get_contact_ability(self, contact, vision, discipline, clutch):
        con= self.get_score_by_attr(contact,CONTACT_ABILITY_AVG_SCORE)
        clt = self.get_score_by_attr(clutch,CONTACT_ABILITY_CLT_SCORE)
        vision  = self.get_score_by_attr(vision,CONTACT_ABILITY_VISION_SCORE)
        disc = self.get_score_by_attr(discipline,CONTACT_ABILITY_DISC_SCORE)
        
        score = con + clt + disc + vision
    
        return round(score,1)
            
    
    def get_power_ability(self, power, clutch):
        p_avg = self.get_score_by_attr(power,MAIN_SCORE)
        clt = self.get_score_by_attr(clutch,SUB_SCORE)
        score = p_avg + clt 
        return round(score,1) 
              
     
    def get_batting_ability(self, contact_ability, power_ability):
        return round(self.get_attr_avg([contact_ability, power_ability]),1)
        
    def get_bs_ability(self, speed, steal):
        spd = self.get_score_by_attr(speed,MAIN_SCORE)
        stl = self.get_score_by_attr(steal,SUB_SCORE)
        
        score = spd + stl 
        
        return round(score,1)   
   
   # Los score
    def get_leadoff_score(self, contact, batting_ability, bs_ability):
        # cambiare que sea solo basando en el contacto porque un leadoff no necesita tener buenos fundamentos sino buena capacidad de contacto
        
            contact_score = self.get_score_by_attr(contact,CONTACT_HITTER_C_AB_REQUIRED)
            bs_ability_score = self.get_score_by_attr(bs_ability,CONTACT_HITTER_BS_AB_REQUIRED)
            b_ability_score = self.get_score_by_attr(batting_ability,CONTACT_HITTER_BAT_AB_REQUIRED)
            
            score = contact_score + bs_ability_score + b_ability_score
            
            return round(score,1)
    
    def get_type_score(self, attributes):
        # esta lsita de atributos tomara el primer atributo como el score que queires calcular
        # este sera el orden, indice / valor:
        # 0 - score que se quiere calcular, valor puede ser 1 powerhouse, 2 fundamentals, offroad
        # 1 - el primer atributo que tiene mas peso en la ecuacion, ejemplo para powerhouse el primero y de mas peso es el poder. 
        # 2 - el segundo con mas peso, por ejemplo en power house es  contact y sigue asi. 
        
        # powerhouse
        if attributes[0] == 1:
            result = [
                self.get_score_by_attr(attributes[1],POWERHOUSE_POWER_REQUIRED),
                self.get_score_by_attr(attributes[2],POWERHOUSE_CLT_REQUIRED),
                self.get_score_by_attr(attributes[3],POWERHOUSE__CONTACT_REQUIRED),
                self.get_score_by_attr(attributes[4],POWERHOUSE_VISION_REQUIRED)
            ]
        elif attributes[0] == 2:
        # Fundamentals
            result = [
                self.get_score_by_attr(attributes[1],FUNDAMENTAL_VISION_REQUIRED),
                self.get_score_by_attr(attributes[2],FUNDAMENTAL_CLT_REQUIRED),
                self.get_score_by_attr(attributes[3],FUNDAMENTAL_DISCIPLINE_REQUIRED),
                self.get_score_by_attr(attributes[4],FUNDAMENTAL_CONTACT_REQUIRED)
            ]
        elif attributes[0] == 3:
        # offroad
            result = [
                self.get_score_by_attr(attributes[1],OFFROAD_CONTACT_REQUIRED),
                self.get_score_by_attr(attributes[2],OFFROAD_POWER_REQUIRED),
                self.get_score_by_attr(attributes[3],OFFROAD_SPEED_REQUIRED),
                self.get_score_by_attr(attributes[4],OFFROAD_CLT_REQUIRED)
            ]
        else:
            print("Type score attribute missing... ")
        
        return round(sum(result),1)
    
    # def get_powerhouse_score(self, power, contact, clutch, vision):
    #         pow = self.get_score_by_attr(power,POWERHOUSE_POWER_REQUIRED)
    #         clt = self.get_score_by_attr(clutch,POWERHOUSE_CLT_REQUIRED)
    #         con = self.get_score_by_attr(contact,POWERHOUSE__CONTACT_REQUIRED)
    #         vis = self.get_score_by_attr(vision,POWERHOUSE_VISION_REQUIRED)
            
    #         score = pow + clt + con + vis
            
    #         return round(score,1)  
            
                
    
    # def get_fundamental_score_overall(self, vision, clutch, discipline, contact):
    #         vis = self.get_score_by_attr(vision,FUNDAMENTAL_VISION_REQUIRED)
    #         clt = self.get_score_by_attr(clutch,FUNDAMENTAL_CLT_REQUIRED)
    #         dis = self.get_score_by_attr(discipline,FUNDAMENTAL_DISCIPLINE_REQUIRED)
    #         con = self.get_score_by_attr(contact,FUNDAMENTAL_CONTACT_REQUIRED)
            
    #         score = vis + clt + dis + con
            
    #         return round(score,1)
            
                
        
        
    # def get_offroad_score_overall(self, contact_ability, power_ability, bs_ability, clutch):
    #     con = self.get_score_by_attr(contact_ability,OFFROAD_CONTACT_REQUIRED)
    #     pow = self.get_score_by_attr(power_ability,OFFROAD_POWER_REQUIRED)
    #     spd = self.get_score_by_attr(bs_ability,OFFROAD_SPEED_REQUIRED)
    #     clt = self.get_score_by_attr(clutch,OFFROAD_CLT_REQUIRED)
        
    #     score = pow + clt + spd + con
        
    #     return round(score,1) 
        