class Hp():
    def __init__(self):
        self.max_hp = 100
        self._hp = self.max_hp

    def get_hp(self):
        return self.hp
    
    def set_hp(self,value):
        self.hp = value
        print(self.hp)

    @property
    def hp(self):
        print("get")
        return self._hp
    @hp.setter
    def hp(self,value):
        self._hp = value
        print("setter")

something = Hp()
#something.set_hp(45)
something.hp += 58
print(something.hp)