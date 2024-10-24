import random

pilihan = "y"
while pilihan.lower() == "y":
    choices = ["gunting", "batu", "kertas"]
    komputer = random.choice(choices)

    print()
    print("=" * 30)
    print("Game Suit Gunting Batu Kertas")
    print("=" * 30, "\n")

    # Menampilkan pilihan kepada pengguna
    print("Pilihan:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice.capitalize()}")
    
    inputUser = input("Masukkan pilihan (1 untuk Gunting, 2 untuk Batu, 3 untuk Kertas): ")

    try:
        pemain = choices[int(inputUser) - 1]
    except (ValueError, IndexError):
        print("Pilihan yang kamu masukan salah... Silakan coba lagi.")
        continue  # Mengulangi loop jika input tidak valid

    print(f"\nKamu memilih: {pemain.capitalize()}")
    print(f"Komputer memilih: {komputer.capitalize()}")

    if pemain.lower() == komputer:
        print("\nHasil suit Seri!")
    elif (pemain.lower() == "gunting" and komputer == "batu") or \
         (pemain.lower() == "batu" and komputer == "kertas") or \
         (pemain.lower() == "kertas" and komputer == "gunting"):
        print("\nYahh kamu kalah :(")
    else:
        print("\nHoree kamu menang :)")

    print("=" * 30, "\n")

    pilihanBaru = input("Apakah kamu ingin bermain kembali? Y/N = ")
    pilihan = pilihanBaru
