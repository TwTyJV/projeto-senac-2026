class IdadeInvalidaError(Exception):
    pass


def cadastrar_eleitor(idade: int):
    if idade < 16:
        raise IdadeInvalidaError("Idade inválida para cadastro de eleitor.")
    print("Eleitor cadastrado com sucesso!")