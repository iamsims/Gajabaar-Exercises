import utils
  

def main():
    inputbytestring = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    inputkey = b"ICE"
    deciphered = utils.repeating_xor(inputbytestring, inputkey)
    print(deciphered.hex())

if __name__ == '__main__':
	main()