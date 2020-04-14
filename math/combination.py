def mod_comb(N, mod):
    inverse = [0]*(N+1)
    for i in range(1, N+1):
        inverse[i] = pow(i, mod-2, mod)
    
    comb = [0]*(N+1)
    comb[0] = 1
    for i in range(1, N+1):
        comb[i] = comb[i-1]*(N-i+1)*inverse[i]%mod
    
    return comb