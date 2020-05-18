import random as rand

def readNums(File):
    f = open(File, 'r')
    data = []
    for l in f:
        l = l[0:l.find('#')]
        data = data + [float(x) for x in l.split()]
    return data

def readPatterns(File, N, M):
    data = readNums(File)
    P = int(len(data)/(N+M))
    return [([data[(p * (M + N)) + n] for n in range(N)], [data[(p * (M + N)) + N + m] for m in range(M)]) for p in range(P)]

def MPNeuron (X, W, Th): # Simple McCulloch-Pitts Neuron
    return [int(sum([x * w for x, w in zip(X, ws)]) >= Th) for ws in W]

def BiLayerPerzeptron (InputDim, OutputDim, Weights, Patterns, LearningRate, RandomSeed, MaxSteps, ErrThreshold):
    rand.seed(RandomSeed)
    ''' Initialize '''
    N = InputDim + 1 # + 1 for Bias
    M = OutputDim
    if not Weights:
        Weights = [[rand.random() - 0.5 for j in range(N)] for i in range(M)]
    elif type(Weights) == str:
        data = readNums(File)
        Weights = [[data[(i * N) + j] for j in range(N)] for i in range(M)]
    if type(Patterns) == str:
        Patterns = readPatterns(Patterns, InputDim, OutputDim)
    P = len(Patterns)
    ''' Learning '''
    for Step in range(MaxSteps):
        Error = 0
        rand.shuffle(Patterns)
        for p in Patterns:
            X = [1] + p[0]
            Target = p[1]
            Y = MPNeuron(X, Weights, 0)
            Error += sum([(y - y_t) ** 2 for y, y_t in zip(Y, Target)])/OutputDim
            Weights = [[Weights[i][j] - (LearningRate * (Y[i] - Target[i]) * X[j]) for j in range(N)] for i in range(M)] # Single step learning
        if Error < ErrThreshold:
            break
    ''' End '''
    print('Weights :')
    for m in range(M):
        print(Weights[m])
    return lambda X: MPNeuron([1] + X, Weights, 0)