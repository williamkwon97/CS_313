#  File: BST_Cipher.py

#  Description: binary tree data structure

#  Student Name: William Kwon

#  Student UT EID: uk660

#  Partner Name: Brandon Ford

#  Partner UT EID: bef528

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/11/18

#  Date Last Modified: 11/12/18


class Node (object):
  def __init__(self, ch):
    self.ch = ch
    self.lchild = None
    self.rchild = None


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        self.encrypt_str = encrypt_str
        self.encrypt_str = self.encrypt_str.lower()
        new_str = ''
        for i in range(len(self.encrypt_str)):
            if(ord('a') <= ord(self.encrypt_str[i]) and ord(self.encrypt_str[i]) <= ord('z') or (self.encrypt_str[i] == ' ')):
                new_str += self.encrypt_str[i]

        self.encrypt_str = new_str

        for i in range(len(self.encrypt_str)):
            self.insert(self.encrypt_str[i])

        self.dict = {}

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):

        new_node = Node(ch)

        # checks to see if the character already exists
        if(self.find_node(ch) != None):
            return

        if (self.root == None):
            self.root = new_node
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (ord(ch) < ord(current.ch)):
                    current = current.lchild
                else:
                    current = current.rchild
            if (ord(ch) < ord(parent.ch)):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # searches for the node given then character to look for
    def find_node(self, ch):

        current = self.root

        while (current != None) and (current.ch != ch):
            if (ord(ch) < ord(current.ch)):
                current = current.lchild
            else:
                current = current.rchild
        return current

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):

        str = ''
        current = self.root

        if(ch == current.ch):
            self.dict[ch] = '*'
            return '*'
        elif(self.find_node(ch) == None):
            return ''

        while (current != None) and (current.ch != ch):
            if (ord(ch) < ord(current.ch)):
                str += '<'
                current = current.lchild
            else:
                str += '>'
                current = current.rchild

        self.dict[ch] = str

        return str

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):

        current = self.root

        if(st[0] == '*'):
            return current.ch

        for i in range(len(st)):
            if(st[i] == '<' and current.lchild != None):
                current = current.lchild
            elif(st[i] == '>' and current.rchild != None):
                current = current.rchild
            else:
                return ''

        return current.ch

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):

        e_str = ''

        st = st.lower()

        for i in range(len(st)):
            if(st[i] in self.encrypt_str):
                e_str += self.search(st[i])+'!'
            else:
                e_str += st[i]+'!'

        return e_str[:len(e_str)-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):

        d_str = ''

        tokens = ['<', '>', '*', '!']

        st = st.split('!')

        for i in range(len(st)):
            flag = True
            for j in range(len(st[i])):
                if not(st[i][j] in tokens):
                    d_str += st[i][j]
                    flag = False
            if flag:
                d_str += self.traverse(st[i])

        return d_str

def main():

    encrypt_key = input('Enter encryption key: ')
    print()

    bin_tree = Tree(encrypt_key)

    encrypt_str = input('Enter string to be encrypted: ')
    e_str = bin_tree.encrypt(encrypt_str)
    print('Encrypted string:', e_str)
    print()

    decrypt_str = input('Enter string to be decrypted: ')
    d_str = bin_tree.decrypt(decrypt_str)
    print('Decrypted string:', d_str)




main()