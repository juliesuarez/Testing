class Furniture:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def assemble(self):
        print(f"{self.name} is being assembled.")

    def clean(self):
        print(f"{self.name} is being cleaned.")

    def move(self):
        print(f"{self.name} is being moved.")

    def store(self):
        print(f"{self.name} is being stored.")


class Sofa(Furniture):
    def __init__(self, name, material, color):
        super().__init__(name, material)
        self.color = color

    def sit(self):
        print(f"{self.name} is being sat on.")


class Bed(Furniture):
    def __init__(self, name, material, size):
        super().__init__(name, material)
        self.size = size

    def sleep(self):
        pass
