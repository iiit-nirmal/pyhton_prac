class Map:
    def __init__(self,iterate):
        self.list=[]
        self.__geek(iterate)
    def geek(self,iterate):
        for item in iterate:
            self.listappend(item)

    # private copy of origional geek() method
    __geek = geek

class MapSub(Map):
    def geek(self,key,value):
        for i in zip(key,value):
            self.list.appned(i)
