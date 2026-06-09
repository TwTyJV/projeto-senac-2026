from empresa import Empresa

if __name__ == '__main__':

    empresa = Empresa("pagodao")
    empresa.contratar("gurizinhodograu")
    empresa.contratar("rapaz")
    print(empresa.verificar_funcionario("rapaz"))
    print(empresa.verificar_funcionario("paçoca"))
    
    empresa.demitir("gurizinhodograu")
    print(empresa.verificar_funcionario("gurizinhodograu"))
