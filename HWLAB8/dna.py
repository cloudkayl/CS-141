"""
file: dna.py
author: Ayush Rout
github: https://github.com/cloudkayl
"""

from linked_code_py import *

# code starts here
def convert_to_nodes(dna_string):
    """
    returns a linked-node data structure representing the input DNA sequence
    :param dna_string: a string of characters corresponding to DNA bases
    :return: linked-node data structure
    """
    if len(dna_string) == 0:
        return None
    else:
        return Node(dna_string[0], convert_to_nodes(dna_string[1:]))

def convert_to_string(dna_seq):
    """
    converts a linked-node data structure into string
    :param dna_seq: a linked sequence in which each node contains as data a
    character representing a base of a DNA sequence
    :return: a string
    """
    dna_str = ' '
    if lengthRec(dna_seq) == 0:
        return dna_str
    else:
        while dna_seq != None:
            dna_str = dna_str + dna_seq.value
            dna_seq = dna_seq.rest
        return dna_str

def is_match(dna_seq1, dna_seq2):
    """
    compares if two linked-sequences are a match or not
    :param dna_seq1: the first linked sequence representing a DNA sequence
    :param dna_seq2: the second linked sequence representing a DNA sequence
    :return: boolean value, True or False
    """
    if dna_seq1 == None and dna_seq2 == None:
        return True
    elif dna_seq1 != None and dna_seq2 != None:
        if dna_seq1.value != dna_seq2.value:
            return False
        else:
            return is_match(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_pairing(dna_seq1, dna_seq2):
    """
    returns true or false to whether the dna sequences have matching pairs: AT or CG in the sequences that is if dna_seq1
    got an 'A' in it, the function returns true if the second sequence got a 'T' at the same index in dna_seq2 and returns
    False for a mismatch in length of nodes
    :param dna_seq1: the first linked dna sequence
    :param dna_seq2: the second linked dna sequence
    :return: boolean, True or False
    """
    if dna_seq1 == None and dna_seq2 == None:
        return True
    elif lengthRec(dna_seq1) != lengthRec(dna_seq2):
        return False
    elif lengthRec(dna_seq1) == lengthRec(dna_seq2):
        while dna_seq1 != None and dna_seq2 != None:
            if ((dna_seq1.value == 'A') and (dna_seq2.value != 'T')) or (
                (dna_seq1.value == 'T') and (dna_seq2.value != 'A')):
                return False
            elif ((dna_seq1.value == 'G') and (dna_seq2.value != 'C')) or (
                (dna_seq1.value == 'C') and (dna_seq2.value != 'G')):
                return False
            else:
                return is_pairing(dna_seq1.rest, dna_seq2.rest)
    else:
        return False

def is_palindrome(dna_seq):
    """
    tests if a sequence is a palindrome or not
    :param dna_seq: the linked sequence its testing
    :return: boolean, True or False
    """
    rev = reverseIter(dna_seq)
    if lengthRec(dna_seq) == 0:
        return True
    elif is_match(dna_seq, rev):
        return True
    else:
        return False

def insertion(dna_seq1, dna_seq2, idx):
    """
    inserts the second dna sequence into the first one at the given index
    :param dna_seq1: the first sequence that it's inserting into
    :param dna_seq2: the sequence being inserted into first one
    :param idx: the index in sequence 1 at which it's placing the second sequence
    :return: a new linked sequence that represents the resulting DNA strand after dna_seq2
    has been inserted into the first
    """
    if idx == 0:
        return cat(dna_seq2, dna_seq1)
    elif dna_seq1 != None:
        return Node(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx-1))
    else:
        raise IndexError("Index out of bound!")


def substitution(dna_seq1, idx, base):
    """
    replaces a base in the mentioned dna sequence at the given index
    :param dna_seq1: the dna sequence it's replacing a base in
    :param idx: the index at which its replacing the existing base
    :param base: the value/base which is going to replace the existing ones
    :return: the updated dna linked-sequence
    """
    if idx == 0:
        dna_seq1.value = base
        return Node(dna_seq1.value, dna_seq1.rest)
    elif dna_seq1 != None:
        return Node(dna_seq1.value, substitution(dna_seq1.rest, idx-1, base))
    else:
        raise IndexError("Index out of bounds!")

def deletion(dna_seq, idx, segment_size):
    """
    deletes a series of values from a linked sequence according to segment_size
    :param dna_seq: the sequence its deleting from
    :param idx: the index at which it's deleting
    :param segment_size: the number of values its deleting
    :return: the updated linked sequence after deleting values/bases from the linked sequence
    """
    if segment_size == 0:
        return dna_seq
    elif dna_seq != None:
        return deletion(removeAt(idx, dna_seq), idx, segment_size-1)
    else:
        raise IndexError("Index out of bounds!")

def value_at_idx(seq, idx, segment_size):
    if idx == 0:
        if segment_size == 0:
            return None
        if seq != None:
            return Node(seq.value, value_at_idx(seq.rest, idx, segment_size-1))
        else:
            raise IndexError("Index out of bounds")
    elif seq != None:
        return value_at_idx(seq.rest, idx-1, segment_size)
    else:
        raise("Index out of range!")

def duplication(dna_seq, idx, segment_size):
    """
    copies a specific segment of elements into the same dna sequence at specified position
    and returns resulting dna strand
    :param dna_seq: the dna sequence from and to, its copying segment of elements from
    :param idx: the index at which the segment to be duplicated begins
    :param segment_size: the number of elements to be duplicated
    :return: a new linked sequence that represents the resulting DNA strand after the specified segment of elements
    from dna_sequence have been copied.
    """
    if segment_size == 0:
        return dna_seq
    return insertion(dna_seq, value_at_idx(dna_seq, idx, segment_size), idx)

# code ends here
"""
Author: Ayush Rout
File: dna.py
language: Python3
email: axr6077@rit.edu
"""