''' Loss function for MSE '''
''' L = (y-y_hat)^2 '''
def update_weights_MSE(a, b, X, Y, lr):
    ad = 0
    bd = 0
    N = len(X)
    for i in range(N):
        # 偏导数
        # -2x(y-(ax+b))
        ad += -2*X[i]*(Y[i]-(a*X[i]+b))
        # -2(y-(ax+b))
        bd += -2*(Y[i]-(a*X[i]+b))
    # update a,b
    a -= (a/float(N))*lr
    b -= (b/float(N))*lr
    return(a,b)

''' Loss function for MAE '''
''' L = |y-y_hat| '''
def update_weights_MAE(a,b,X,Y,lr):
    ad = 0
    bd = 0
    N = len(X)
    for i in range(N):
        # -x(y-(ax+b))/|ax+b|
        ad += X[i]*(Y[i]-(a*X[i]+b))/abs(Y[i]-(a*X[i]+b))
        # -(y-(ax+b))/|ax+b|
        bd += -(Y[i]-(a*X[i]+b))/abs(Y[i]-(a*X[i]+b))
    #update a,b
    a -= (a/float(N))*lr
    b -= (b/float(N))*lr
    return(a,b)
''' Loss function for Huber '''
''' L = 1/2(y-y_hat)^2, if |y-y_hat| <= delta
      = delta*|y-y_hat| - 1/2* delta^2'''
def update_weights_huber(a,b,X,Y,delta,lr):
    a_d = 0
    b_d = 0
    N = len(X)
    for i in range(N):
        if abs(Y[i]-(aX[i]+b)) <= delta:
            a_d += -X[i] * (Y[i] - (a*X[i] + b))
            b_d += - (Y[i] - (a*X[i] + b))
        else:
            a_d += delta*X[i] * ((a*X[i] + b) - Y[i]) / abs((a*X[i] + b) - Y[i])
            b_d += delta * ((a*X[i] + b) - Y[i]) / abs((a*X[i] + b) - Y[i])
    #update a, b
    a -= (a_d / float(N)) * lr
    b -= (b_d / float(N)) * lr
    return(a,b)

            
    
    
    
    
    
    
    
