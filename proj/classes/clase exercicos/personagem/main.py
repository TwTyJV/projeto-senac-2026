from personagem import Personagem

heroi = Personagem("Herói", 100, 20)
monstro = Personagem("Monstro", 80, 15)

heroi.atacar(monstro)
print(monstro.vida)

monstro.atacar(heroi)
print(heroi.vida)