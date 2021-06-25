import utils


def main():
    string_1= "1c0111001f010100061a024b53535009181c"
    string_2 ="686974207468652062756c6c277320657965"
    byte_string_1 = bytes.fromhex(string_1)
    byte_string_2 = bytes.fromhex(string_2)

    print( (utils.bXor(byte_string_1, byte_string_2)).hex())

if __name__ == '__main__':
	main()