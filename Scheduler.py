import sys
from Process import Process

def Scheduler ():
    processes = []
    verbose = 0
    num_processes = 0
    input = ''

    if len(sys.argv) > 2 and str(sys.argv[1]) == '--verbose':
        verbose = 1

    #file = open(str(sys.argv[1]), 'r')
    with open(str(sys.argv[1+verbose])) as file:
        input = file.read()

    input = input.replace('(', '')
    input = input.replace(')', '')

    input_list = input.split()
    num_processes = input_list[0]

    #SORT OUTPUTS HERE!!!!!

    for i in range(1, len(input_list), 4):
        print(input_list[i:i+4])
        processes.append(input_list[i], input_list[i+1], input_list[i+2], input_list[i+3], i)

    print(verbose)

    p = Process('gilad')
    print(p.name)
    print(p.state)


Scheduler()
