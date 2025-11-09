def LCG(a, c, m, z0):
    U = z0 / m
    print("U0 =", U)
    Zk1 = (a * z0 + c) % m
    z0 = Zk1
    print("Z1 =", Zk1, "--- z0 =", z0)

    for i in range(1, m):
        U = Zk1 / m
        Zk1 = (a * z0 + c) % m
        z0 = Zk1
        print(f"{i + 1}: Zk = {Zk1} --- z0 = {z0} --- Uk = {U}")



LCG(7, 5, 16, 112)