import heapq
import json
from collections import Counter

"""
This python file contains my self written implementation of Huffman coding based on books explanation.
Huffman coding encodes the letter frequency and input text and creates tree holding the letters and rewrites data with 1's and 0's of tree letter path.
This way files are compressed and encoded/encrypt. WHich can be decoded using the tree as key.
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
    frequency = Counter(text)
    root = build_huffman_tree(frequency)
    code_map = generate_codes(root)
    encoded = encode(text, code_map)
    return encoded, root


def huffman_decompress(encoded, root):
    decoded = decode(encoded, root)
    return decoded


file = "all_of_shakespear.txt" # 5.37 Mb file containing all W. Shakespear Works.
compressed_file = "all_of_shakespear_compressed.txt" # 2.47 Mb, nearly 2.17x efficient storage using huffman coding. No Loss in data (Not Lossy)
decompressed_file = "all_of_shakespear_decompressed.txt" # same as original file with 5.37 Mb. No Loss in Information.

read_file = open(file, "r", encoding="utf-8")
write_file = open(compressed_file, "w", encoding="utf-8")
write_file2 = open(decompressed_file, "w", encoding="utf-8")

# Compressing
data = read_file.readlines()
c_data, key = huffman_compression(data)
write_file.writelines(c_data)

# Save Key/codemap for Later Use
def serialize_tree(node):
    if node is None: return None
    return [node.char, serialize_tree(node.left), serialize_tree(node.right)]
with open("key.json", "w", encoding="utf-8") as f:
    json.dump(serialize_tree(key), f)


# Get key from key.json
def deserialize_tree(data):
    if data is None:return None
    node = HuffmanNode(data[0])
    node.left = deserialize_tree(data[1])
    node.right = deserialize_tree(data[2])
    return node
with open("key.json", "r", encoding="utf-8") as f:
    tree_data = json.load(f)
    key_x = deserialize_tree(tree_data)


# Decompressing
w = open(compressed_file, "r", encoding="utf-8")
compressed_data = w.readlines()[0]
d_data = huffman_decompress(compressed_data, key_x)
write_file2.writelines(d_data)


