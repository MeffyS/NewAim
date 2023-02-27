class SOptions:
    def __init__(self,username = 'Guest', sound = 100, music = 100, time = 0, level = 0, points = 0, hearts = 4, colorR = 0 , colorG = 0, colorB = 0):
        self.username = username
        self.sound = sound
        self.music = music  
        self.level = level
        self.points = points
        self.hearts = hearts
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB
    
t = SOptions()
print(t.username)


