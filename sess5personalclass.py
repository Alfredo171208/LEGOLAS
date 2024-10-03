class Alfredo:
    def __init__(self, height : int, money : int, gf : bool):
        self.height = height 
        self.money = money 
        self.gf = gf 
    
    
    
    def get_cuan(self,money : int):
        self.money += money
        print('Congrats, you now have', self.money, 'bucks in your bank')
    
    def bakar_duit(self,money : int):
        self.money -= money
        print('You lost', money, 'bucks.')
        if self.money < 0:
            print('Congrats, you are now', abs(self.money),'bucks in debt!')
        else: 
            print('Now you have', self.money,'bucks left.')
            
    def rungkad_mode(self, height: int):
        paid= height * 20
        self.money -= height * 20 
        if self.money >= 0:
            self.height += height
            print('You paid', paid,'bucks. You are now', self.height, 'cm tall.')
            print('you now have', self.money, 'bucks left!')
        else:
            print("you don't have that kind of money!")
    
    def get_gf(self):
        if self.height * self.money >= 10000000000:
            self.gf == True 
            print('Congrats! You now have a girlprendd')
        else:
            print('Sorry, you are too broke!')

stats= Alfredo(170, 12, False)
stats.get_cuan(13)
stats.bakar_duit(1)
stats.rungkad_mode(13)
stats.get_gf()