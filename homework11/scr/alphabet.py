class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Літери алфавіту:", " ".join(self.letters))

    def letters_num(self) -> int:
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def s_en_letter(self, letter: str) -> bool:
        return letter.upper() in self.letters

    def letters_num(self) -> int:
        return EngAlphabet.__letters_num

    @staticmethod
    def example() -> str:
        return "London is the capital of Great Britain."


if __name__ == "__main__":
    eng_alphabet = EngAlphabet()

    eng_alphabet.print()
    print("Кількість літер:", eng_alphabet.letters_num())

    print("Чи належить 'F' англійському алфавіту?",
          eng_alphabet.s_en_letter('F'))

    print("Чи належить 'Щ' англійському алфавіту?",
          eng_alphabet.s_en_letter('Щ'))

    print("Приклад тексту:", EngAlphabet.example())
