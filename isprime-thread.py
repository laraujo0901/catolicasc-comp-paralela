from threading import Thread, Lock
import time

value = 100001
temp_list = [] # Variável compartilhada pelas threads
lock = Lock()

def drop_multiples(num, the_list):
  """
  Seguindo a lógica do crivo de Eratóstenes, gera uma nova lista, sem os 
  múltiplos do número fornecido.
  """
  return [x for x in the_list if x == num or x%num != 0]

def process_list(num, the_list):
  """
  Função auxiliar que será chamada pelas threads
  """
  global temp_list
  
  # Se o ultimo elemento da lista for menor que o número a verificar, 
  # retorna a própria lista  
  if the_list[-1] < num:
    temp_list = temp_list + the_list
  else:
    new_list = drop_multiples(num, the_list)
  
    # Restringe o acesso à variável compartilhada
    lock.acquire()
    temp_list = temp_list + new_list
    lock.release()

def is_prime(num):
  """
  Função principal para verificar se um número é primo
  """
  global temp_list
  
  # Número par maior que 2 não é primo
  if num > 2 and num%2 == 0:
    return False

  # Lista de números inteiros, de 2 ao número fornecido (crivo de Eratóstenes)
  int_list = [x+1 for x in range(1,num)]
  
  has_values  = True
  idx         = 0
  num_threads = 5
  
  # Este laço percorre a lista completa de números, para eliminar os multiplos
  while has_values:

    # Número que será verificado na lista completa
    number = int_list[idx]
    
    # Tamanho dos pedaços da lista completa, de acordo com número de threads
    slice_size = int(len(int_list)/num_threads)
  
    threads = []
    start   = 0
    end     = slice_size + 1
        
    # Criar as threads
    for i in range(num_threads):

      list_slice = int_list[start:end]
      
      threads.append(Thread(target=process_list, args=(number, list_slice)))
      
      start = end
      end   = end + slice_size
    
    # Iniciar as threads
    for thread in threads:
      thread.start()
    
    # Aguardar finalização das threads
    for thread in threads:
      thread.join()
        
    # Ajustando eventual troca de ordem dos elementos
    temp_list.sort()
    
    # Atualizando a lista principal com os elementos restantes
    int_list  = temp_list
    temp_list = []
    
    idx += 1
    has_values = (idx < len(int_list))
    
  #print("Lista dos primos até o número {} (tamanho: {}):".format(num,len(int_list)))
  #print(int_list)
  
  # Verifica se o número consta na lista final que contem apenas primos.
  return (num in int_list)

tic = time.time()
print(" O numero {} é primo? {}".format(value, is_prime(value)))
tac = time.time()
print(" Tempo de execução: {}".format(tac-tic))
  