import base64
import utils
import challenge3

def hamming_distance(bytes_a,bytes_b):
    xored= utils.bXor(bytes_a, bytes_b)
    binary_bytes = [bin(i)[2:] for i in xored]
    binary_string = ''.join(binary_bytes)
    binary = list(map(int, list(binary_string)))
    count= sum(binary)
    return(count)

def find_key_size(string):
    candidates = []
    for keysize in range(2,40):
        array_of_strings = [string[i:i+keysize] for i in range(0,len(string),keysize)]
        totalhd = 0
        for a in range(0,len(array_of_strings)-1): #leaving the last block which may or may not be keysize long
            totalhd += hamming_distance(array_of_strings[a],array_of_strings[a+1])
        
        normalizedhd = totalhd/keysize
        normalizedhd /= len(array_of_strings)

        candidate = {
            'hamming_dist':normalizedhd,
            'keysize':keysize
        }

        candidates.append(candidate)

    best_key_size= sorted(candidates, key=lambda x: x['hamming_dist'])[0]
    return best_key_size['keysize']

def find_key(byte,keysize):
    key = ""
    for i in range(keysize):
        by = byte[i::keysize]
        best_guess= challenge3.decipher(by)
        key+=chr(best_guess['key'])
    return key.encode()

def main():    
    file = open("6.txt","r")
    strings = file.read()
    binary_strings = base64.b64decode(strings)
    best_key_size = find_key_size(binary_strings)
    key = find_key(binary_strings,best_key_size)
    answer = utils.repeating_xor(binary_strings, key).decode()
    print(answer)

if __name__=="__main__":
    main()


