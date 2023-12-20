    """
    Klasa Converter zawiera metody do przekształcania liczb między systemem binarnym a dziesiętnym.

    Metody:
    - binary_to_decimal(binary): Przekształca liczbę binarną na dziesiętną.
    - decimal_to_binary(decimal): Przekształca liczbę dziesiętną na binarną.
    - convert(): Obsługuje interakcję z użytkownikiem, umożliwiając mu wybór rodzaju przekształcenia.

    Przykłady użycia:
    converter = Converter()
    converter.convert()
    """
        """
        def binary_to_decimal(self, binary):
        
        Przekształca liczbę binarną na dziesiętną.

        Args:
        binary (str): Liczba binarna jako ciąg znaków.

        Returns:
        int: Liczba dziesiętna.
        """
          """
            def decimal_to_binary(self, decimal):
        
        Przekształca liczbę dziesiętną na binarną.

        Args:
        decimal (int): Liczba dziesiętna.

        Returns:
        str: Liczba binarna jako ciąg znaków.
        """
    """
    def convert(self):
        
        Obsługuje interakcję z użytkownikiem, umożliwiając mu wybór rodzaju przekształcenia.
        Użytkownik może przekształcić liczbę z systemu binarnego na dziesiętny lub z systemu dziesiętnego na binarny.
        """
class Converter:
    def binary_to_decimal(self, binary):
        decimal = 0
        binary = str(binary)
        if not all(bit in '01' for bit in binary):
            print("Błędna liczba binarna. Wprowadź poprawną liczbę binarną.")
            return None

        binary = binary[::-1]
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** i
        return decimal

    def decimal_to_binary(self, decimal):
        if decimal < 0:
            print("Błędna liczba dziesiętna. Wprowadź liczbę większą lub równą zero.")
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
                try:
                    decimal_number = int(input("Podaj liczbę dziesiętną: "))
                    binary_result = self.decimal_to_binary(decimal_number)
                    if binary_result is not None:
                        print(f'{decimal_number} w systemie binarnym to: {binary_result}')
                except ValueError:
                    print("Błędna liczba dziesiętna. Wprowadź liczbę całkowitą.")
            else:
                print("Błędny wybór. Wybierz 1, 2 lub wpisz 'exit'.")

if __name__ == "__main__":
    converter = Converter()
    converter.convert()
