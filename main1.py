ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,?!-"


def find_number(text: str) -> list:
    encrypted_text = []
    for item in text:
        encrypted_text.append(ALPHABET.find(item) + 1)
    return encrypted_text


def sum_number(text_number: list, key_number: list) -> list:
    new_text = []
    count = 0
    for word in text_number:
        if count >= len(key_number):
            count = 0
        word = word + key_number[count]
        if (word > len(ALPHABET)):
            word = word - len(ALPHABET)
        new_text.append(word)
        count += 1
    return new_text


def spy(text_number: list) -> str:
    spy_text = ""
    for word in text_number:
        spy_text += ALPHABET[word - 1]
    print(spy_text)
    return spy_text


def encryption(text: str, key: list) -> str:
    text_number = find_number(text)
    key_number = find_number(key)
    new_text_number = sum_number(text_number, key_number)
    return spy(new_text_number)


if __name__ == "__main__":
    file = open("decrypted_text1.txt", "r")
    text = file.read()
    file.close()
    new_file = open("encrypted_text1.txt", "w+")
    new_file.write(encryption(text, "кодирование"))
    new_file.close()
