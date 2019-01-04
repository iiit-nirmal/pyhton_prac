class itrClass:
    def __init__(self,in_list):
        self.items =in_list
        self.itemslen = len(in_list)
        pass

    ## is called at the initilization of an iterator and return an object that has __next__ method.
    def __iter__(self):
        self.index =0
        return self

    def __next__(self):
         index =self.index

         if index>=self.itemslen:
             raise StopIteration

         item = self.items[index]
         self.index = index+1
         return item

## here at each iteration it for calls __next__ on iterator object and this method should raise StopIteration to signal to end the iteration
for i in itrClass([1,2,3]):
    print(i)