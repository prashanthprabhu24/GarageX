import heapq
from collections import Counter

"""
This python file contains my self written implementation of Huffman coding based on books explanation.
Huffman coding encodes the letter frequency and input text and creates tree holding the letters and rewrites data with 1's and 0's of tree letter path.
This way texts are compressed and encoded. WHich can be decoded using the tree as key.
"""


class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]


def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map


def encode(text, code_map):
    return ''.join(code_map[char] for char in text)


def decode(encoded_text, root):
    decoded_text = ''
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_text += node.char
            node = root
    return decoded_text



def huffman_compression(text):
    print(f"Original Text: {text}")
    frequency = Counter(text)
    print(f"Frequencies: {frequency}")
    root = build_huffman_tree(frequency)
    code_map = generate_codes(root)
    print(f"Huffman Codes: {code_map}")
    encoded = encode(text, code_map)
    print(f"Encoded Text: {encoded}")
    decoded = decode(encoded, root)
    print(f"Decoded Text: {decoded}")
    return encoded, decoded


text = "huffman coding is a data compression algorithm"
encoded, decoded = huffman_compression(text)
