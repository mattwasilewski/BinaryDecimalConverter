class Converter:
    def validate_input_binary_decimal(self, input_str, is_binary=True):
        """
        Sprawdza poprawność wprowadzonej liczby binarnej lub dziesiętnej.

        :param input_str: Wprowadzona liczba binarna lub dziesiętna.
        :param is_binary: Określa, czy sprawdzać poprawność liczby binarnej (domyślnie True).
        :return: True, jeśli liczba jest poprawna; False w przeciwnym razie.
        """
        valid_chars = '01' if is_binary else '0123456789'
        if not all(bit in valid_chars for bit in input_str):
            print(f"Błędna liczba {'binarna' if is_binary else 'dziesiętna'}. Wprowadź poprawną liczbę.")
            return False
        return True

    def binary_to_decimal(self, binary):
        """
        Konwertuje liczbę binarną na dziesiętną.

        :param binary: Wprowadzona liczba binarna.
        :return: Liczba dziesiętna lub None, jeśli wprowadzona liczba jest niepoprawna.
        """
        binary = str(binary)

        if not self.validate_input_binary_decimal(binary):
            return None

        decimal = 0
        binary = binary[::-1]
        for i, bit in enumerate(binary):
            if bit == '1':
                decimal += 2 ** i
        return decimal

    def decimal_to_binary(self, decimal):
        """
        Konwertuje liczbę dziesiętną na binarną.

        :param decimal: Wprowadzona liczba dziesiętna.
        :return: Liczba binarna lub None, jeśli wprowadzona liczba jest niepoprawna.
        """
        if not self.validate_input_binary_decimal(str(decimal), is_binary=False):
            return None

        binary = ''
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal //= 2
        return binary

    def print_menu(self):
        """
        Wyświetla menu dla użytkownika.
        """
        print("Wybierz przekształcenie:")
        print("1. Binarny -> Dziesiętny")
        print("2. Dziesiętny -> Binarny")

    def convert(self):
        """
        Główna funkcja obsługująca interakcję z użytkownikiem i wykonująca konwersje.
        """
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
