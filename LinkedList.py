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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"value : {self.value}"

    def __eq__(self, node: object):
        return self.value == node.value


class LinkedList:
    """
    Stocke les données sous la forme de liste chainée
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
                liste += f" {current.value} -->"
            else:
                liste += f" {current.value}"
            current = current.next
        return liste

    def append(self, value):
        """
        Ajoute une nouvelle valeur unique à la fin liste chainée
        """
        if self.head is None:
            self.head = Node(value)

        if self.__contain(value) is False:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return True
        else:
            return False

    def insert(self, value, new_value, before=False):
        """
        Insère par défaut une nouvelle valeur derrière la valeur donnée.
        Si before est passé à True, il fait l'insertion devant
        """
        node = self.__contain(value)
        if node is False:
            raise ValueError('La valeur saisie exite déjà.')

        new_node = Node(new_value)
        if before:
            current = self.head

            if current == node:
                # Cas où il s'agit d'une insertion devant la tête de la liste chainée
                new_node.next = self.head
                self.head = new_node
                return True

            while current.next:
                if current.next == node:
                    break
                current = current.next

            current.next = new_node
            new_node.next = node
            return True

        else:

            """
            Ici, la valeur est insérée juste après le noeud s'il existe
            """
            new_node = Node(new_value)
            new_node.next = node.next
            node.next = new_node
            return True

    def remove(self, value):
        """
        supprime le noeud s'il elle existe
        """
        node_rm = self.__contain(value)
        if node_rm is False:
            return

        current = self.head
        if current == node_rm:  # Au cas où l'élément à supprimer est la tête
            self.head = current.next
            del node_rm
            return True

        while current.next:
            if current.next == node_rm:
                break
            current = current.next

        current.next = current.next.next
        del node_rm
        return True

    def size(self):
        """
        Retourne le nombre d'éléments dans une liste chainée
        """
        taille = 0
        current = self.head
        while current:
            taille += 1
            current = current.next
        return taille
