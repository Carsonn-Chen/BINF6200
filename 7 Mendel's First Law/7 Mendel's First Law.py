k, m, n = map(int, input().split())
sum_num = k+m+n
ans = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*sum_num*(sum_num-1))


print(ans)