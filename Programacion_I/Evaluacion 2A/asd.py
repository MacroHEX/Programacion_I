class reversa:
    def __init__(self,c):
        self.c=c
    
    def proceso(self):
        return ' '.join(self.c.split(' '))
    
    def invertir(self):
        return ' '.join(self.c.split(' ')[::-1])
        
palabra=reversa('Mi Diario')

print(palabra.proceso())
