# python3
#221RDC024, Ksenija Žuka

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(i,0) for i in range(n)]
    for i in range(m):
        min_thr = min(threads, key=lambda x: x[1])
        output.append((min_thr[0], min_thr[1]))
        threads[min_thr[0]] = (min_thr[0], min_thr[1] + data[i])
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
