from multiplos import Multiplos

if __name__ == '__main__':

    multiplos = Multiplos()

    try:
        multiplos.processar_dados([1,3,2,0,-1], 8)
        multiplos.processar_dados([1,3,'a',0,-1], 2)
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)