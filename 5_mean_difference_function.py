def md_nre_single_sample(y, y_hat, n, p):
    # Compute the n-th root of y and y_hat
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    
    # Calculate the absolute difference between the two values
    difference = abs(y_root - y_hat_root)
    
    # Raise this difference to the power of p
    loss = difference ** p
    
    return loss

# check
print( md_nre_single_sample(100, 99.5, 2, 1))
print(md_nre_single_sample(50, 49.5, 2, 1))
print( md_nre_single_sample(20, 19.5, 2, 1))
print( md_nre_single_sample(0.6, 0.1, 2, 1))
