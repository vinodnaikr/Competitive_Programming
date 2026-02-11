class Vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def display(self):
        print(f"{self.i}i+{self.j}j")
    
class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def display(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")

v2=Vector2D(1,3)
v3=Vector3D(1,9,7)

v2.display()
v3.display()