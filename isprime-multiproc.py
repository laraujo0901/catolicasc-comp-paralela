from multiprocessing import Pool
import os
import time
import sys

number = int(sys.argv[1])

if number > 300000001:
    print("Número muito grande para ser verificado. Saindo...")
    sys.exit(0)

if number > 2 and number%2 == 0:
    print("Todo número par maior que 2 não é primo!")
    sys.exit(0)

def generate_list(begin,end):
    return [x for x in range(begin,end)]

def is_multiple(a_number, other_number):
    # Considerar número dividido por 1 ou por ele mesmo como não multiplo
    if a_number <= 1 or other_number <= 1  or a_number == other_number:
        return False

    if (a_number > other_number):
        return (a_number%other_number == 0)
    else:
        return (other_number%a_number == 0)

def evaluate_list(x):
    global number
    return is_multiple(x, number)

if __name__ == '__main__':
    pool = Pool() # quando não informado, obtem o numero de cpus usando os.cpu_count()
    
    start = time.time()
    the_list = generate_list(2, number)
    result = pool.imap(evaluate_list, the_list)
    finish = time.time()
    
    print("O número {} {} primo!".format(number, ("não é" if (True in result) else "é")))
    print("Resposta em {} seg.".format(finish-start))
            


