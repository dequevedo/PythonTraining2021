#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def getNumber(binary: SinglyLinkedListNode):
    lista = []
    getBinaryArray(binary, lista)
    lista.reverse()

    total = 0
    for indice, valor in enumerate(lista):
        conta = int(math.pow(2, indice)) * valor
        total += conta

    return total


def getBinaryArray(binary, lista):
    lista.append(binary.data)
    if (binary.next):
        getBinaryArray(binary.next, lista)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')

    fptr.close()
