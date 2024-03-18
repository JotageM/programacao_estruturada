import random
def main():
    # aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10,20)
    defesa_aventureiro = random.randint(1,5)
    # monstro
    vida_monstro = random.randint(60,80)
    ataque_monstro = random.randint(20,30)

    rodada = 1
    print("Aventureiro: vida",vida_aventureiro,"- att",ataque_aventureiro,"- def",defesa_aventureiro)
    print("Monstro: vida",vida_monstro,"- att ",ataque_monstro)
    while True:
        print("Rodada", rodada)
        vida_monstro -= random.randint(1,ataque_aventureiro)
        ataque_rodada_monstro=random.randint(1,ataque_monstro) - defesa_aventureiro
        if ataque_rodada_monstro < 0:
            ataque_rodada_monstro = 0
        vida_aventureiro -= ataque_rodada_monstro
        rodada += 1
        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break
        elif vida_monstro <= 0:
            print("O monstro morreu!")
            break
        print("Aventureiro: vida",vida_aventureiro,"- att",ataque_aventureiro,"- def",defesa_aventureiro)
        print("Monstro: vida",vida_monstro,"- att ",ataque_monstro)


main()











