

def returns(x,y) -> float:
    '''
    x: Current Value
    y: Previous Value
    
    '''
    returns = (x - y) / y
    return returns

def sharpe_ratio(mean,std,rate) -> float:
    

    ratio = (mean - rate)/std
    return ratio

    