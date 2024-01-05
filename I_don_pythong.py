class Converter:
    def validate_input_binary_decimal(self, input_str):
        if not all(bit in '01' for bit in input_str):
            print("Błędna liczba binarna. Wprowadź poprawną liczbę binarną.")
            return False
        return True

    def validate_input_decimal_binary(self, input_str):
        try:
            decimal_number = int(input_str)
            if decimal_number < 0:
                print("Błędna liczba dziesiętna. Wprowadź liczbę większą lub równą zero.")
                return False
            return True
        except ValueError:
            print("Błędna liczba dziesiętna. Wprowadź liczbę całkowitą.")
            return False

    def binary_to_decimal(self, binary):
        binary = str(binary)

        if not self.validate_input_binary_decimal(binary):
            return None

        decimal = 0
        binary = binary[::-1]
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** i
        return decimal

    def decimal_to_binary(self, decimal):
        if not self.validate_input_decimal_binary(str(decimal)):
            return None

        binary = ''
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def print_menu(self):
        print("Wybierz przekształcenie:")
        print("1. Binarny -> Dziesiętny")
        print("2. Dziesiętny -> Binarny")

    def convert(self):
        while True:
            self.print_menu()

            choice = input("Twój wybór (1 lub 2), lub wpisz 'exit' aby zakończyć: ")

            if choice.lower() == 'exit':
                return
            elif choice == '1':
                binary_number = input("Podaj liczbę binarną: ")
                decimal_result = self.binary_to_decimal(binary_number)
                if decimal_result is not None:
                    print(f'{binary_number} w systemie dziesiętnym to: {decimal_result}')
            elif choice == '2':
                decimal_number = input("Podaj liczbę dziesiętną: ")
                binary_result = self.decimal_to_binary(decimal_number)
                if binary_result is not None:
                    print(f'{decimal_number} w systemie binarnym to: {binary_result}')
            else:
                print("Błędny wybór. Wybierz 1, 2 lub wpisz 'exit'.")

if __name__ == "__main__":
    converter = Converter()
    converter.convert()
