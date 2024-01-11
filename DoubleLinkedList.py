"""
MIT License

Copyright (c) 2023 Espérance AYIWAHOUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"value : {self.value}"

    def __eq__(self, node: object):
        return self.value == node.value


class DoubleLinkedList:
    """
    Stocke les données sous la forme de double liste chainée
    """

    def __init__(self):
        self.head = None

    def __contain(self, value):
        """
        Retourne le noeud si elle existe déjà dans la liste et un pointeur sur le noeud sinon
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return False

    def __contains__(self, value):
        """
        Retourne le noeud si elle existe déjà dans la liste et False sinon
        """
        if self.__contain(value) is not False:
            return True
        return False

    def __str__(self):
        liste = ""
        current = self.head
        while current:
            if current.next:
                liste += f" {current.value} <--> "
            else:
                liste += f" {current.value}"
            current = current.next
        return liste

    def append(self, value):
        """
        Ajoute une nouvelle valeur unique à la fin de la double liste chainée
        """
        if self.head is None:
            self.head = DoubleNode(value)
        else:
            new_node = DoubleNode(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        return True

    def insert(self, value, new_value, before=False):
        """
        Insère par défaut une nouvelle valeur derrière la valeur donnée.
        Si before est passé à True, il fait l'insertion devant
        """
        node = self.__contain(value)
        if node is False:
            return False

        new_node = DoubleNode(new_value)
        if before:
            if node.prev is None:
                # Cas où il s'agit d'une insertion devant la tête de la double liste chainée
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
            return True
        else:
            new_node.next = node.next
            new_node.prev = node
            if node.next:
                node.next.prev = new_node
            node.next = new_node
            return True

    def remove(self, value):
        """
        supprime le noeud s'il elle existe
        """
        node_rm = self.__contain(value)
        if node_rm is False:
            return False

        if node_rm.prev:
            node_rm.prev.next = node_rm.next
        else:
            self.head = node_rm.next

        if node_rm.next:
            node_rm.next.prev = node_rm.prev

        del node_rm
        return True

    def size(self):
        """
        Retourne le nombre d'éléments dans une double liste chainée
        """
        taille = 0
        current = self.head
        while current:
            taille += 1
            current = current.next
        return taille
