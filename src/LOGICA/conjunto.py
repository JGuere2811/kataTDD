class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto)==1:
            return (self.__conjunto[0])
        elif len(self.__conjunto)==2:
            return (self.__conjunto[0]+self.__conjunto[1])/2
        else:
            return None
