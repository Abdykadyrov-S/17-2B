"Магические методы"
"dunder методы -  (double underscore) "

class BrawlStars:
    def __init__(self, hero, map, coins):
        self.hero = hero
        self.map = map
        self.coins = coins

    def info(self):
        print(f"Hero - {self.hero}, map - {self.map}, coins - {self.coins}")

    def __str__(self): # print
        return f"Hero - {self.hero}, map - {self.map}, coins - {self.coins} "

    # def __repr__(self): # print
    #     return f"Hero - {self.hero}, map - {self.map}, coins - {self.coins} \nэто repr\n"
    "Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции"
    def __call__(self, a , b):
        print("Это маг. метод call")
        return a , b
    
    "Магические методы для арифметических действий"
    def __add__(self, other): # +
        new_coin = self.coins + other.coins
        return BrawlStars( self.hero, self.map, new_coin)

    def __sub__(self, other): # -
        new_coin = self.coins - other.coins
        return BrawlStars( self.hero, self.map, new_coin)
    
    def __mul__(self, other): # *
        new_coin = self.coins * other.coins
        return BrawlStars( self.hero, self.map, new_coin)
    
    def __truediv__(self, other): # /
        new_coin = self.coins / other.coins
        return BrawlStars( self.hero, self.map, new_coin)
    
    def __floordiv__(self, other): # //
        new_coin = self.coins // other.coins
        return BrawlStars( self.hero, self.map, new_coin)
    

    "Магические методы для операторов сравнения"
    def __gt__(self, other): # >
        return  self.coins > other.coins
    
    def __lt__(self, other): # <
        return  self.coins < other.coins
    
    def __eq__(self, other): # ==
        return  self.coins == other.coins
    
    def __ne__(self, other): # !=
        return  self.coins != other.coins
    
    def __ge__(self, other): # >=
        return  self.coins >= other.coins
    
    def __le__(self, other): # <=
        return  self.coins <= other.coins

brawl = BrawlStars("Spike", "School", 40000)
brawl_2 = BrawlStars("Shelly", "Dream", 20000)
"str , repr"
print(brawl_2)
print(brawl)
# brawl.info()

"Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции"
brawl(3 ,7)


"Магические методы для арифметических действий"
print(brawl + brawl_2)
print(brawl - brawl_2)
print(brawl * brawl_2)
print(brawl / brawl_2)
print(brawl // brawl_2)


"Магические методы для операторов сравнения"
print(brawl > brawl_2)
print(brawl < brawl_2)
print(brawl == brawl_2)
print(brawl != brawl_2)
print(brawl >= brawl_2)
print(brawl <= brawl_2)

