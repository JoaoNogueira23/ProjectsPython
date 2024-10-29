import os

def commands(inputs):
    global queue
    if int(inputs[0]) == 1:
        queue.append(inputs[1])
        return None
    elif int(inputs[0]) == 2:
        queue.pop(0)
        return None
    elif int(inputs[0]) == 3:
        return queue[0]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    queue = []
    #numero de consultas
    q = int(input().strip())

    for t_itr in range(q):
        s = input()

        inputs_commands = s.split(' ')

        result = commands(inputs_commands)
        
        if result:
            fptr.write(result + '\n')

    fptr.close()