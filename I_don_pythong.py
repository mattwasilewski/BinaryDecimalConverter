def bin_to_dec(binary):
    decimal = 0
    binary = str(binary)[::-1]  # Odwróć ciąg binarny
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal

def dec_to_bin(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Przykład użycia
print("1. Konwersja z binarnego na dziesiętny")
binary_input = input("Podaj liczbę binarną: ")
decimal_result = bin_to_dec(binary_input)
print(f"Wynik: {decimal_result}")

print("\n2. Konwersja z dziesiętnego na binarny")
decimal_input = int(input("Podaj liczbę dziesiętną: "))
binary_result = dec_to_bin(decimal_input)
print(f"Wynik: {binary_result}")
