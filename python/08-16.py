def decrypt(encrypted_text):
    dic = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }
    result = ""
    for word in encrypted_text.split("  "):
        for char in word.split(" "):
            result += dic[char]
        result += " "
    return result


print(decrypt(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"))
