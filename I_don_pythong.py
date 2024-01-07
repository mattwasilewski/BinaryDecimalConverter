class Converter:


    def validate_binary_input(self, input_str):
        """
        Sprawdza poprawność wprowadzonej liczby binarnej.
        :param input_str: Wprowadzona liczba binarna.
        :return: Liczba binarna jako ciąg znaków, jeśli liczba jest poprawna; None w przeciwnym razie.
        """
        if not all(bit in '01' for bit in input_str):
            print("Błędna liczba binarna")
            return None
        return input_str

    def validate_decimal_input(self, input_str):
        """
        Sprawdza poprawność wprowadzonej liczby dziesiętnej.
        :param input_str: Wprowadzona liczba dziesiętna.
        :return: Liczba dziesiętna jako ciąg znaków, jeśli jest poprawna; None w przeciwnym razie.
        """
        if not all(char in '0123456789' for char in input_str):
            print("Błędna liczba dziesiętna")
            return None
        return input_str


    def binary_to_decimal(self, binary):
        """
        Konwertuje liczbę binarną na dziesiętną.

        :param binary: Wprowadzona liczba binarna.
        :return: Liczba dziesiętna lub None, jeśli wprowadzona liczba jest niepoprawna.
        """

        if not self.validate_binary_input(binary):
            return None
        
        binary = int(binary)

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
        if not self.validate_decimal_input(decimal):
            return None
        
        decimal = int(decimal)
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
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
            if choice == '1':
                binary_number = input("Podaj liczbę binarną: ")
                decimal_result = self.binary_to_decimal(binary_number)
                if decimal_result is not None:
                    print(f'{binary_number} w systemie dziesiętnym to: {decimal_result}')
            elif choice == '2':
                decimal_number = input("Podaj liczbę dziesiętną: ")
                binary_result = self.decimal_to_binary(decimal_number)
                if binary_result is not None:
                    print(f'{decimal_number} w systemie binarnym to: {binary_result}')
            elif choice.lower() == 'exit':
                return
            else:
                print("Błędny wybór. Wybierz 1, 2 lub wpisz 'exit'.")



if __name__ == "__main__":
    converter = Converter()
    converter.convert()