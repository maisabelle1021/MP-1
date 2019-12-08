def PROBLEM1():   
    X = [ ]
    Y = [ ]
  
    for i in range(0,100,1):
        X.append(i)
        i += 1
    
    for i in range(0,100,1):
        if i <= 9:
            m = pow(i,2)-7
            Y.append(m)
            i += 1
        elif i >= 10:
            n = i-10
            Y.append(n)
            i += 1
            
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize=(50,30))
    fig = plt.stem(X,Y)
    plt.show(fig)
