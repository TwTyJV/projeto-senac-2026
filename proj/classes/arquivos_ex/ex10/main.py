from simulador import fazer_backup_dados

if __name__ == '__main__':

    backup = fazer_backup_dados("dados.txt")

if backup:
    print(f"criado:{backup}")