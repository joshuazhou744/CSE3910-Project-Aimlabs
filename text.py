class Text(MySprite):
    def __init__(self, text, font_family = "Arial", font_size=36, x=0, y=0):
        MySprite.__init__(self, x=x, y=y)
        self.text = text
        self.font_family = font_family
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.surface = self.font.render(self.text, True, self.color)

    def setText(self,text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)