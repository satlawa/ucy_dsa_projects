#------------------------------------------------------#
#   problem 5 - Blockchain
#------------------------------------------------------#

# imports
import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        """ Initialize Block """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


    def __repr__(self):
        """ Standard representation of the Block as a string """
        return " ----------------------------------------------------\
        \n Block info: \n   data: {} \n   timestamp: {} \n   hash: {}\
        ----------------------------------------------------\n"\
        .format(self.data, self.timestamp, self.hash)


    def calc_hash(self):
        """ Calculate hash for this Block """
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        """ Initialize BlockChain """
        self.tail = None
        self.length = 0


    def append(self, data):
        """ Add new Block-node to the BlockChain """

        # if input argument is not of type string
        if not isinstance(data, str):
            print("Type error: argument must be of type string")
            return
        # if input argument is an empty string
        if len(data) == 0:
            print("Value error: argument must be at least one character long")
            return

        # if the new Block is the root Block previous_hash is set to None
        if self.tail is None:
            self.tail = Block(timestamp = datetime.datetime.utcnow(), \
                              data = data, previous_hash = None)
        # else previous_hash is set to the previous Block
        else:
            self.tail = Block(timestamp=datetime.datetime.utcnow(), \
                              data = data, previous_hash = self.tail)
        self.length += 1


    def search(self, data):
        """ Search the BlockChain for a node with the requested data and return the node """
        if self.tail is None:
            return None

        node = self.tail
        while node:
            if node.data == data:
                return node
            node = node.previous_hash

        raise ValueError("Value not found in the list.")


    def size(self):
        """ Return the size or length of the BlockChain """
        return self.length


    def to_list(self):
        """ Convert the BlockChain into a Python list """
        out = []
        node = self.tail
        while node:
            out.append([node.timestamp, node.data, node.hash])
            node = node.previous_hash
        return out


# standard test cases
bc = BlockChain()

bc.append("Transaction from card number: 30084290103, amount: 40$, balance: 440$")
print(bc.tail)
#data: Transaction from card number: 30084290103, amount: 40$, balance: 440$
#   timestamp: 2020-12-26 10:52:23.908411
#   hash: 8f8b3f51fbd055163bd09bb82a0262a17a37857e4411f0a1170d42e708cdfd7c

bc.append("Transaction from bank account: 45557559, amount: 10000$, balance: 10440$")
print(bc.tail)
#Block info:
#   data: Transaction from bank account: 45557559, amount: 10000$, balance: 10440$
#   timestamp: 2020-12-26 10:52:23.908791
#   hash: ec02a1dafbacc51a8a179add3334580bea074150c0706898ad364fb22d36f5a2

bc.append("Transaction to card number: 30084290103, amount: 440$, balance: 10000$")
print(bc.tail)
#Block info:
#   data: Transaction to card number: 30084290103, amount: 440$, balance: 10000$
#   timestamp: 2020-12-26 10:52:23.909120
#   hash: d445e514b000d2281e2bf3e587837a72daeaddfd477b65797a9fe0f23cc56bbc

# edge test cases
bc.append("")
print(bc.tail)
#Value error: argument must be at least one character long
#Block info:
#   data: Transaction to card number: 30084290103, amount: 440$, balance: 10000$
#   timestamp: 2020-12-26 10:52:23.909120
#   hash: d445e514b000d2281e2bf3e587837a72daeaddfd477b65797a9fe0f23cc56bbc

bc.append(4000)
print(bc.tail)
#Type error: argument must be of type string
#Block info:
#   data: Transaction to card number: 30084290103, amount: 440$, balance: 10000$
#   timestamp: 2020-12-26 10:52:23.909120
#   hash: d445e514b000d2281e2bf3e587837a72daeaddfd477b65797a9fe0f23cc56bbc
