class Stack:
    """
    Structure de donnée d'une pile LIFO
    """

    def __init__(self):
        self.data = []

    def __str__(self):
        return " - ".join(map(str, reversed(self.data)))

    def __repr__(self):
        print(self)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Stack):
            return False
        return self.data == obj.data

    def add(self, value):
        """
        Ajoute la valeur dans la pile si elle n'existait pas
        """
        if value in self.data:
            raise ValueError(f"La valeur {value} existe déjà dans la pile")
        self.data.append(value)
        return True

    def peek(self):
        """
        Retourne la dernière entrée de la pile sans la supprimer
        """
        if self.data:
            return self.data[-1]
        raise IndexError("La pile est déjà vide")

    def remove(self):
        """
        Retourne et supprime la dernière entrée de la pile
        """
        if self.data:
            return self.data.pop()
        raise IndexError("La pile est déjà vide")

    def size(self):
        """
        Retourne la taille actuelle de la pile
        """
        return len(self.data)
