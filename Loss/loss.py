''' Loss function for MSE '''
''' L = (y-y_h)^2 '''
def update_weights_MSE(a, b, X, Y, lr):
    a = 0
    b = 0
    N = len(X)
    for i in range(N):
        # 偏导数
        # -2x(y-(ax+b))
        a += -2*X[i]*(Y[i]-(a*X[i]+b))
        # -2(y-(ax+b))
        b += -2*(Y[i]-(a*X[i]+b))
    # update a,b
    a -= (a/float(N))*lr
    b -= (b/float(N))*lr
    return(a,b)
