# Class đại diện cho Tướng trong Liên minh huyền thoại
# Đây là 1 Abstract Class
# Bất kỳ class nào kế thừa class này đều sẽ có 
#   tính chất của 1 tướng trong Liên minh huyền thoại

from abc import ABC

# Đánh dấu đây là 1 Abstract Class bằng cách dùng ABC
class Champion(ABC):
    def __init__(self, name, skill):
        self.__name = name # Đóng gói, private bằng 2 dấu gạch dưới __
        self.__skill = skill # Khi private thì class ngoài không truy cập vào được

    def attack(self):
        print(self.__name, 'thi triển' ,self.__skill)

    def cast_skill_q(self):
        pass
    def cast_skill_w(self):
        pass
    def cast_skill_r(self):
        pass
    def cast_skill_e(self):
        pass

    # Getter
    def get_name(self): # Cho phép bên ngoài xem được giá trị thuộc tính private
        return self.__name