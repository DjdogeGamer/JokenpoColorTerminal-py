# Jokenpô!!!
import random

player = None
cpu = None

print("")
print("\033[4;33mVamos jogar pedra, papel ou tesoura!\033[m ")
print("")
print("\033[36m------------------------------------\033[m")
print("\033[1;33mDigite:\033[m ")
print("\033[37m1 Para: Pedra\033[m")
print("\033[30m2 Para: Papel\033[m")
print("\033[35m3 Para: Tesoura\033[m")
print("\033[36m------------------------------------\033[m")
print("")

player = int(input("\033[4;33mDigite aqui!:\033[m "))

print("")

cpu = random.randint(1, 3)

if player == cpu:
    print("\033[1;33mEmpate!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 1 and cpu == 2:
    print("\033[1;31mVocê perdeu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 2 and cpu == 1:
    print("\033[1;32mVocê venceu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 2 and cpu == 3:
    print("\033[1;31mVocê perdeu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 3 and cpu == 2:
    print("\033[1;32mVocê venceu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 1 and cpu == 3:
    print("\033[1;32mVocê venceu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))

elif player == 3 and cpu == 1:
    print("\033[1;31mVocê perdeu!\033[m \033[36m[Você] ->\033[m {} \033[30mX\033[m {} \033[33m<- [CPU]\033[m ".format(player, cpu))


