import utils

def decipher(bytestring):
    """
    provided the hexstring it returns the best decoded value based on the character frequency score
    """
    potential_messages = []
    for key_value in range(256):

        message = utils.single_char_xor(bytestring, key_value)
        score = utils.get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)

    best_guess = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
    return best_guess

def main():
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    inputstring = bytes.fromhex(hexstring)
    best_guess = decipher(inputstring)
    print(best_guess['message'])

if __name__ == '__main__':
	main()