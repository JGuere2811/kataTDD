class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto)==1:
            return (self.__conjunto[0])
        elif len(self.__conjunto)==2:
            return (self.__conjunto[0]+self.__conjunto[1])/2
        elif len(self.__conjunto)>2:
            return sum(self.__conjunto)/len(self.__conjunto)
        else:
            return None
