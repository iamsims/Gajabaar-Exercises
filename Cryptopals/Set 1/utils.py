from base64 import b64encode
import codecs
from binascii import hexlify, unhexlify
import struct 
import math
# encode/decode for strings to binary and viceversa

def convertHextoBase64(hex):
    b64=codecs.encode(bytes.fromhex(hex), 'base64').decode().replace("\n", "")
    # bytes.fromhex converts the string type into byte type
    # codecs.encode converts the byte object into base64 format,
    # decode is used to convert the byte object to string 
    return b64

def bXor(byte_string_1,byte_string_2):
    """
    recievers byte strings and return a xored byte strings
    """
    return bytes([b1 ^ b2 for b1, b2 in zip(byte_string_1, byte_string_2)])

def get_english_score(input_bytes):
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    keystring = struct.pack("B", char_value)*len(input_bytes)
    
    return bXor(input_bytes, keystring)


def get_english_score(input_bytes):
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    keystring = struct.pack("B", char_value)*len(input_bytes)
    #we reuse the bXor we implemented in problem #2
    return bXor(input_bytes, keystring)


def repeating_xor(input_bytes, key_bytes):
    keystring = key_bytes*(math.ceil(len(input_bytes)/len(key_bytes)))
    keystring= keystring[:len(input_bytes)]

    return bXor(input_bytes, keystring)
    


