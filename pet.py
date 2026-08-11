import random 
class Pet:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.hunger=50
        self.mood=50
        self.energy=80
    def show_status(self):
        print(f'''
        ======{self.name}状态=====
        年龄：{self.age}
        饥饿度：{self.hunger}
        心情：{self.mood}
        精力：{self.energy}
        ''')
    def feed(self):

        if self.hunger == 0:
            print(f"{self.name}已经吃饱了")
            return

        self.hunger -= 10

        if self.hunger <= 0:
            self.hunger = 0
            print(f"{self.name}吃饱了！")
    def touch(self):
        self.mood+=10
        if random.randint(1,100)<=30:
            print(f'{self.name}害羞了')
            self.mood+=5
        if self.mood>100:
            self.mood=100
    def sleep(self):
        self.energy+=10
        if self.energy>100:
            self.energy=100
        if random.randint(0,100)<=15:
            print(f'{self.name}打呼噜了')
        self.hunger-=10
        if self.hunger<0:
            self.hunger=0
        print(f"{self.name}睡了一觉")

