class ChainDemo:

    def __init__(self,item = None,pos_item=None):

        self._item = item
        self._pos_item = pos_item


if __name__ == '__main__':
    chain = ChainDemo('A',(ChainDemo('B',ChainDemo('C',ChainDemo('D')))))
    while True:
        print(chain._item)
        if chain._pos_item != None:
            chain = chain._pos_item
        else:
            break