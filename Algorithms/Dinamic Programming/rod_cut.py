
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10

r = [0]
s = [0] * n

def bu_cut_rod(p, n):
    global r

    for j in range(n):
        q = -9999

        for i in range(j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i+1
        r.append(q)

    return r, s


print(bu_cut_rod(p, n))
