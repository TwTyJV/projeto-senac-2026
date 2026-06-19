def fazer_backup_dados(nome_arquivo_original):
    nome_arquivo_backup = f"{nome_arquivo_original}.bak"

    try:
        with open(nome_arquivo_original, "r") as arquivos_original:
            conteudo = arquivos_original.read()

        with open(nome_arquivo_backup, "wb") as arquivo_backup:
            arquivo_backup.write(conteudo)

        return nome_arquivo_backup
    

    except PermissionError:
        print("fsemp ermisão"
        f"{nome_arquivo_backup}"
        )

    except OSError as erro:
        print(f"realizar backup")

    return None