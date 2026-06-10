from agenda import Agenda

if __name__ == '__main__':

    agenda = Agenda ()


    agenda.salvar_contato("cleiton", "92222-1111")
    agenda.salvar_contato("Carlos", "98888-2222")

    print(agenda.buscar_telefone("cleiton"))


    print(agenda.buscar_telefone("João"))