import random
import math

# Fungsi X
def func(x):
    return (-5 * math.exp(-x ** 2))

# Inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1": random.uniform(0, 3),
    "x2": random.uniform(0, 3),
    "x3": random.uniform(0, 3),
    "x4": random.uniform(0, 3),
    "x5": random.uniform(0, 3),
    "x6": random.uniform(0, 3),
    "x7": random.uniform(0, 3),
    "x8": random.uniform(0, 3),
    "x9": random.uniform(0, 3),
    "x10": random.uniform(0, 3)
}

# Inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before = {key: 0 for key in xi}

# Inisialisasi vo
v0 = 0

# Inisialisasi vi setelah terjadi iterasi
vi = {f"v{i}": v0 for i in range(1, 11)}

# Inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1 / 2
r1 = random.uniform(0, 1)  # Gunakan uniform untuk nilai desimal
r2 = random.uniform(0, 1)
w = 1
Gbest = None  # Mulai dengan None karena belum ada nilai terbaik
Pbesti = []

# Fungsi untuk mencari Gbest dengan membandingkan semua fungsi(x) lalu mengambil nilai x dari fungsi yang menghasilkan nilai paling kecil
def x_minimum(*args):
    global Gbest
    Gbest = min(args, key=func)

# Fungsi untuk yang akan mengambil langsung nilai xi dan menyimpannya ke dalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(*args):
    Pbesti.extend(args)

# Fungsi untuk mengambil nilai xi dan menyimpannya ke dalam Pbesti dengan cara membandingkan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(*args):
    # args berisi pasangan (x_before, x_current)
    for i in range(0, len(args), 2):
        x_before = args[i]
        x_current = args[i + 1]
        if func(x_current) <= func(x_before):
            Pbesti.append(x_current)
        else:
            Pbesti.append(x_before)

# Fungsi untuk mencari nilai vi
def vi_func(vimin1, xi_current, pbest_i):
    return (w * vimin1) + (c1 * r1 * (pbest_i - xi_current)) + (c2 * r2 * (Gbest - xi_current))

n = int(input("\033[92m" + f"Masukan Jumlah Iterasi :" + "\033[0m"))
print()

# Looping berdasarkan jumlah iterasi yang diinginkan
for index in range(n):
    print("\033[92m" + f"iterasi ke-{index + 1}" + "\033[0m")
    # Pengosongan array Pbesti
    Pbesti.clear()

    # Kondisional statement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0:
        fx_minimum_iterasi1(
            xi["x1"], xi["x2"], xi["x3"], xi["x4"], xi["x5"],
            xi["x6"], xi["x7"], xi["x8"], xi["x9"], xi["x10"]
        )
    else:
        fx_minimum_selanjutnya(
            xi_before["x1"], xi["x1"],
            xi_before["x2"], xi["x2"],
            xi_before["x3"], xi["x3"],
            xi_before["x4"], xi["x4"],
            xi_before["x5"], xi["x5"],
            xi_before["x6"], xi["x6"],
            xi_before["x7"], xi["x7"],
            xi_before["x8"], xi["x8"],
            xi_before["x9"], xi["x9"],
            xi_before["x10"], xi["x10"]
        )

    # Memanggil fungsi x_minimum
    x_minimum(*Pbesti)

    # Update nilai vi berdasarkan fungsi vi_func
    vi["v1"] = vi_func(vi["v1"], xi["x1"], Pbesti[0])
    vi["v2"] = vi_func(vi["v2"], xi["x2"], Pbesti[1])
    vi["v3"] = vi_func(vi["v3"], xi["x3"], Pbesti[2])
    vi["v4"] = vi_func(vi["v4"], xi["x4"], Pbesti[3])
    vi["v5"] = vi_func(vi["v5"], xi["x5"], Pbesti[4])
    vi["v6"] = vi_func(vi["v6"], xi["x6"], Pbesti[5])
    vi["v7"] = vi_func(vi["v7"], xi["x7"], Pbesti[6])
    vi["v8"] = vi_func(vi["v8"], xi["x8"], Pbesti[7])
    vi["v9"] = vi_func(vi["v9"], xi["x9"], Pbesti[8])
    vi["v10"] = vi_func(vi["v10"], xi["x10"], Pbesti[9])

    # Update nilai xi_before dengan nilai dari xi iterasi sekarang
    for key in xi_before:
        xi_before[key] = xi[key]

    # Update nilai dari xi iterasi sekarang
    for i in range(1, 11):
        key = f"x{i}"
        vi_key = f"v{i}"
        xi[key] = xi_before[key] + vi[vi_key]

    for i in range(10):
        print(f"Nilai x({i+1}): {xi[f'x{i+1}']:.2f}\t\tNilai v{i+1}: {vi[f'v{i+1}']:.2f}")
        print(f"Nilai f(x{i+1}): {func(xi[f'x{i+1}']):.2f}\t\tNilai Pbest(x{i+1}): {Pbesti[i]:.2f}")

    print()
    if Gbest is not None:
        print(f"Nilai Gbest: {Gbest:.2f}")
        print(f"Nilai Minimum f({Gbest:.2f}): {func(Gbest):.2f}")
    else:
        print("Nilai Gbest belum ditentukan.")
    print()
print("Proses iterasi selesai.")
