''' calculate the gradient descent '''
''' Loss function for MSE '''
''' L = (y-y_hat)^2 '''
def update_weights_MSE(a, b, X, Y, lr):
    a_d = 0
    b_d = 0
    N = len(X)
    for i in range(N):
        # 偏导数
        # -2x(y-(ax+b))
        a_d += -2*X[i]*(Y[i]-(a*X[i]+b))
        # -2(y-(ax+b))
        b_d += -2*(Y[i]-(a*X[i]+b))
    # update a,b
    a -= (a_d/float(N))*lr
    b -= (b_d/float(N))*lr
    return(a,b)

''' Loss function for MAE '''
''' L = |y-y_hat| '''
def update_weights_MAE(a,b,X,Y,lr):
    a_d = 0
    b_d = 0
    N = len(X)
    for i in range(N):
        # -x(y-(ax+b))/|ax+b|
        a_d += X[i]*(Y[i]-(a*X[i]+b))/abs(Y[i]-(a*X[i]+b))
        # -(y-(ax+b))/|ax+b|
        b_d += -(Y[i]-(a*X[i]+b))/abs(Y[i]-(a*X[i]+b))
    #update a,b
    a -= (a_d/float(N))*lr
    b -= (b_d/float(N))*lr
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
''' Loss function for binary cross entropy '''
''' L = -(y * log(y_hat) + (1 - y) * log(1 - y_hat)) '''
''' y_hat = 1/(1+math.exp(-m1*X1[i]- m2*X2[i] - b)) '''
''' log-loss function '''
def update_weight_bce(m1,m2,X1,X2,Y,lr):
    m1_d = 0
    m2_d = 0
    b_d = 0
    for i in range(N):
        s = 1 / (1 / (1 + math.exp(-m1*X1[i] - m2*X2[i] - b)))
        m1_d += -X1[i] * (s - Y[i])
        m2_d += -X2[i] * (s - Y[i])
        b_d += -(s - Y[i])
    m1 -= (m1_d / float(N)) * lr
    m2 -= (m2_d / float(N)) * lr
    b -= (b_d / float(N)) * lr
    return(m1, m2, b)

            
    
    
    
    
    
    
    
