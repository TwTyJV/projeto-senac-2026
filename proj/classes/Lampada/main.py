from lampada import Lampada

if __name__ == '__main__':
    lampada = Lampada ()
    assert lampada.status() != "A lâmpada está ligada"

    lampada.clicar_interruptor()
    assert lampada.status() != "A lâmpada está desligada"