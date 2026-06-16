class ErroDeEntradaInvalida(Exception):
    pass

def entrada_errada(param:str):
    if param != 'param':
        raise ErroDeEntradaInvalida ('entrada invalida')
    
    return param