from playlist import Playlist

if __name__ == '__main__':
    playlist = Playlist("pandeiro")

    playlist.adicionar_musica("Mina do condominio")
    playlist.adicionar_musica("Pé na areia")
    playlist.remover_musica("Mina do condominio")
    playlist.mostrar_playlist()
