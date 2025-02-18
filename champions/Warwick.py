from champion_base import Champion
class Warwick(Champion): 
    def __init__(self):
        super().__init__("Warwick", "Cắn xé")
        
    def cast_skill_q(self):
        return 'Cắn xé'
         
    def cast_skill_w(self):
        return 'Mùi máu'
    def cast_skill_e(self):
        return 'Gầm thét'
    def cast_skill_r(self):
        return 'Khóa chết'