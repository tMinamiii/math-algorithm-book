N = int(input())

a = [None] * (N + 1)
a[1], a[2] = 1, 1
for i in range(3, N + 1):
    a[i] = (a[i - 1] + a[i - 2]) % 1000000007

print(a[N] % 1000000007)

# このプログラムは、N = 100000 でも 0.05 秒ほどの実行で答えが求まります。
# これは、コード 4.6.1 と比較して数十倍速いスピードです。
# N <= 10 ** 7 の制約では実行に最大 3 秒ほどかかってしまいますが、PyPy3 で実行すれば 1 秒の制限に間に合います。
