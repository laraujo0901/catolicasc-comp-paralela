import os
import time
import sys

number = int(sys.argv[1])

if number > 1000000:
    print("Número muito grande para ser verificado. Saindo...")
    sys.exit(0)

if number > 2 and number%2 == 0:
    print("Todo número par maior que 2 não é primo!")
    sys.exit(0)

def generate_list(begin,end):
    return [x + 1 for x in range(begin,end)]

def is_multiple(a_number, other_number):
    # Considerar número dividido por 1 ou por ele mesmo como não multiplo
    if a_number == 1 or other_number == 1 or a_number == other_number:
        return False

    if (a_number > other_number):
        return (a_number%other_number == 0)
    else:
        return (other_number%a_number == 0)

if __name__ == '__main__':
    start = time.time()
    divisors = [x for x in generate_list(1, number) if is_multiple(x, number) == True]
    finish = time.time()
    print("O número {} {} primo!".format(number, ("é" if len(divisors)==0 else "não é")))
    print("Resposta em {} seg.".format(finish-start))
            


