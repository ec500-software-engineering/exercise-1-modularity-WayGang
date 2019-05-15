# Copyright 2018 Gang Wei wg0502@bu.edu
# storage module


class storage():
    def __init__(self, bo, bp, pul):
        self.bo = bo
        self.bp = bp
        self.pul = pul



    def store(self):
        print('storage blood oxygen processed successfully')
        print('storage blood pressure processed successfully')
        print('storage pulse processed successfully')
        return 0
    # for useful data
    # connection to the database
    # storage the data into the database
    # extract the data out of the database of the format


    def read(self,Input):
        if Input == "bo":
            return self.bo
        elif Input == "bp":
            return self.bp
        elif Input == "pul":
            return self.pul

    # for example: print(storage(3,4,5).read('bo'))
    # which is bo = 3,bp = 4,and pul = 5
    # Then it returns 3

    # print(storage(3,4,5).read('bo'))
