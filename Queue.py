class Queue:
    """
    Structure de donnée d'une file FIFO
    """

    def __init__(self):
        self.data = []

    def __str__(self):
        return " - ".join(map(str, self.data))

    def __repr__(self):
        return str(self)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Queue):
            return False
        return self.data == obj.data

    def add(self, value):
        """
        Ajoute la valeur dans la file si elle n'existait pas
        """
        if value in self.data:
            raise ValueError(f"La valeur {value} existe déjà dans la file")
        self.data.insert(0, value)
        return True

    def remove(self):
        """
        Retourne et supprime la première entrée de la file
        """
        if self.data:
            return self.data.pop()
        raise IndexError("La file est déjà vide")

    def size(self):
        """
        Retourne la taille actuelle de la file
        """
        return len(self.data)
