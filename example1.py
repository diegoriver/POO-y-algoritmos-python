class Cordenada:



    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff =(self.x - otra_cordenada.x)**2
        y_diff =(self.y - otra_cordenada.y)**2
        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord1 = Cordenada(4, 3)
    coord2 = Cordenada(0,0)

    print(coord1.distancia(coord2))