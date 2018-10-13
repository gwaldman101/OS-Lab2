class Process:
    state = 'not ready'     # options: not ready, ready, running, blocked, terminated
    arrival_time = 0
    B = 0
    cpu_needed = 0
    M = 0
    id = 0

    remaining_run = 0
    remaining_block = 0
    remaining_cpu = 0

    def __init__(self, A, B, C, M, id):
        self.arrival_time = A
        self.B = B
        self.cpu_needed = C
        self.M = M
        self.id = id
