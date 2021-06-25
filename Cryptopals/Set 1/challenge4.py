import utils
import challenge3

def main():

    best_items =[]

    with open('4.txt') as f:
        for line in f:
            # print(line)
            hexstring= line
            inputstring = bytes.fromhex(hexstring)
            best_item = challenge3.decipher(inputstring)
            best_items.append(best_item)

    actual_message = sorted(best_items, key=lambda x: x['score'], reverse=True)[0]
    print(actual_message['message'])

if __name__ == '__main__':
	main()
    