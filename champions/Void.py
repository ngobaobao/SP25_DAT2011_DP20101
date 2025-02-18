from champion_base import Champion
class Void(Champion): # Void kế thừa từ Champion
    def __init__(self):
        super().__init__("Void", "Dark Matter")
    
    # Ghi đè hoàn toàn
    def attack(self):
        print(self.get_name(), 'go to sleep')