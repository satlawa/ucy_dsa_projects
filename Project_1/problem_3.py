#------------------------------------------------------#
#   problem 3 - Huffman Coding
#------------------------------------------------------#

# imports
import sys

class Node(object):

    def __init__(self,char = None, value = None, left = None, right = None, code = None):
        self.char = char
        self.value = value
        self.left = left
        self.right = right
        self.code = code

    def __repr__(self):
        return "Node(char: {} value: {} code: {} \n left: {} \n right: {})".format(self.char, self.value, self.code, self.left, self.right)


def count_char(string):
    """
    Return a dictinary with the count of unique characters in a string

    Args:
        string(str): String on which to perform the count
    Return:
        dictionary with: * keys = unique characters from the input string
                         * values = count of the character in the string
    """

    char_freq = {}

    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq


def merge_nodes(pqueue):
    """
    Merge the two Nodes whith the lowest frequency from the priority queue
    and add the merged Node back to the priority queue

    Args:
        pqueue(list): sorted list by priority, contining: priority [0], node [1]
    Return:
        priority queue (list) with the merged merged Node
    """
    # pop 2 nodes from priority queue
    freq_1, node_1 = pqueue.pop()
    freq_2, node_2 = pqueue.pop()
    # create internal merged node with the sum of frequencies
    merged_node = Node(value = freq_1 + freq_2, left = node_1, right = node_2)
    # add merged node back to pqueue
    pqueue.append((merged_node.value, merged_node))
    pqueue = sorted(pqueue, key=lambda x: x[0], reverse=True)
    return pqueue


def add_code(node):
    """
    Add binary code to all nodes. 0s to left children nodes and
    1s to right children nodes.

    Args:
        node(Node): tree node
    Return:
        node (Node) with the added binary code
    """
    # base case
    if node.left == None and node.right == None:
        return node
    # if left child, add code, call function recursivley
    if node.left is not None:
        # add '0' for encoding
        if node.code is None:
            node.left.code = '0'
        else:
            node.left.code = node.code + '0'
        # add 0 for decoding
        node.left.value = 0
        node.left = add_code(node.left)
    # if right child, add code, call function recursivley
    if node.right is not None:
        # add '1' for encoding
        if node.code is None:
            node.right.code = '1'
        else:
            node.right.code = node.code + '1'
        # add 1 for decoding
        node.right.value = 1
        # call function recursivley
        node.right = add_code(node.right)
    return node


def retrieve_code_from_tree(node, dic):
    """
    Retrieve binary encoding from Huffman tree

    Args:
        node(Node): tree node
        dic(dict): empty binary encoding dictionary
    Return:
        dic(dict): filled binary encoding dictionary
    """
    if node.left == None and node.right == None:
        dic[node.char] = node.code
        return dic
    if node.left is not None:
        retrieve_code_from_tree(node.left, dic)
    if node.right is not None:
        retrieve_code_from_tree(node.right, dic)
    return dic


def create_encoder(tree):
    """
    Creates the dictionary for the encoding of data

    Args:
        tree(Node): the root node of the Huffman tree
    Return:
        encode_dict(dict): encoding dictionary
        tree(Node): the root node of the Huffman tree
    """
    # if tree has no children we create a left child
    if tree.left == None:
        tree.left = Node(char = tree.char, value = 0, left = None, right = None, code = '0')

    # create encoding dictionary
    encode_dict = dict()

    # get dictionary with the encoding for each character
    encode_dict = retrieve_code_from_tree(tree, encode_dict)

    return encode_dict, tree


def huffman_encoding(data):
    """
    Using Huffman encoding to compress the input data

    Args:
        data(str): string containing the data to be encoded
    Return:
        encoded data (str) and the tree for decoding (Tree)
    """

    if data == "":
        print("Value error: Please enter a non empty string")
        return None, None

    # get dict with each characters frequency
    char_freq = count_char(data)

    # create a priority queue out of the dictionary
    pqueue = list()
    for key, value in char_freq.items():
        node = Node(char=key, value=value)
        pqueue.append((node.value, node))
        pqueue = sorted(pqueue, key=lambda x: x[0], reverse=True)

    # merge 2 nodes until there is just one node left
    while len(pqueue) > 1:
        pqueue = merge_nodes(pqueue)

    # add binary code to nodes
    tree = add_code(pqueue[0][1])

    # create encoder dictonary
    encode_dict, tree = create_encoder(tree)

    # encode data with Huffman
    encoded_data = ""
    for char in data:
        encoded_data += encode_dict[char]

    return encoded_data, tree


def huffman_decoding(data, tree):
    """
    Using Huffman decoding to retrieve the original data from the compressed data

    Args:
        data(str): encoded data to be decoded
        tree(Node): the root node of the Huffman tree
    Return:
        decoded data (str)
    """

    # decode
    decoded_data = ""
    i = 0
    current_node = tree

    # loop until the the encoded data ends
    for i in range(len(data)):
        # get item in index
        item = data[i]
        # if item is 0 set current node to LEFT child node
        if item == str(current_node.left.value):
            current_node = current_node.left
        # if item is 1 set current node to RIGHT child node
        elif item == str(current_node.right.value):
            current_node = current_node.right

        # if current node is a leaf node convert binary code to character
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree

    return decoded_data


if __name__ == "__main__":
    # Standard test cases
    print("---------------------------------- Test 1 ------------------------------------------")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1110100100010111000110101101100111111110111100010001011001110000101101

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word


    print("---------------------------------- Test 2 ------------------------------------------")
    a_great_sentence = "Th3 83sT daY 0F mY 1if3!!!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 75
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: Th3 83sT daY 0F mY 1if3!!!

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 40
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 10110100100000101110001010101100111011110010100011111111100011001101000110001101111010100011011011

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 75
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: Th3 83sT daY 0F mY 1if3!!!


    # Edge test cases
    print("---------------------------------- Test 3 ------------------------------------------")
    a_great_sentence = "xxxxxx"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 55
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: xxxxxx

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 55
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: xxxxxx


    print("---------------------------------- Test 4 ------------------------------------------")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 49
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is:

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # Value error: Please enter a non empty string
