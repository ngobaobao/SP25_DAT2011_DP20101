from champion_base import Champion
class Zeus(Champion): # Zeus kế thừa từ Champion
    def __init__(self):
        super().__init__("Zeus", "Thunderbolt")

    # Ghi đè phương thức attack
    def attack(self):
        super().attack() # Thực hiện phương thức attack của cha
        # Có thể thực hiện thêm một số nội dung khác
        print('Zeus hồi 1 máu')
