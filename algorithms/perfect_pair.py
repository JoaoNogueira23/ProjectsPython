#!/bin/python3
import os


def getPerfectPairsCount(arr):
    # Converter para valores absolutos e ordenando
    # será importante para a nova forma de validação, diminuindo o processamento
    arr = [abs(x) for x in arr]
    arr.sort()
    
    start_index = 0
    count_perfects_pairs = 0
    n = len(arr)
    
    # Percorrer os elementos do array
    for i in range(1, n):
        # Verificar enquanto start não satisfaz a condição
        #  andando pelo array até chegar em i (para que a condição x < y seja sastifeita)
        # arr[i] = y e arr[start] = x
        while start_index < i and arr[start_index] < arr[i] / 2:
            start_index += 1
        
        # Adicionar o número de pares perfeitos
        count_perfects_pairs += i - start_index

    return count_perfects_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPerfectPairsCount(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
