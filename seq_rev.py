# source: https://codefights.com/challenge/JenHHG7p5osTwNiBe/

def seq_rev(n, p):
    a = list(range(n))
    res = []
    for i in range(len(p)): 
        if len(p[i]) == 2:
            a[p[i][0]:(p[i][1]+1)] = a[p[i][0]:(p[i][1]+1)][::-1]
        elif len(p[i]) == 1:
            res = res + [a[p[i][0]]]
    return(sum(res))
	
seq_rev(5, [[0, 4], [1, 4], [4], [1, 3], [2, 4], [3]])
seq_rev(10, [[0, 1], [1, 2], [1, 3], [2, 4], [3]])