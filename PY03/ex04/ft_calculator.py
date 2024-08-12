class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        STATIC METHOD
        Function that prints the dot product of 2 vectors
        zip Function to Automatically Loop Over Multiple Lists"""
        try:
            if (len(V1) != len(V2)):
                raise AssertionError("Vectors  must be the same length")
        except AssertionError as e:
            print(e)
            exit(1)
        dot_product = 0
        for v1, v2 in zip(V1, V2):
            dot_product += v1 * v2
        print(f"Dot product is : {dot_product}")



    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        STATIC METHOD
        Function that prints the addition of 2 vectors
        zip Function to Automatically Loop Over Multiple Lists"""
        try:
            if (len(V1) != len(V2)):
                raise AssertionError("Vectors  must be the same length")
        except AssertionError as e:
            print(e)
            exit(1)
        add = []
        for v1, v2 in zip(V1, V2):
            add.append(float(v1 + v2))
        print(f"Add Vector is : {add}")

    #your code here
    # decorator
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        STATIC METHOD
        Function that prints the substraction of 2 vectors
        zip Function to Automatically Loop Over Multiple Lists"""
        try:
            if (len(V1) != len(V2)):
                raise AssertionError("Vectors  must be the same length")
        except AssertionError as e:
            print(e)
            exit(1)
        sous = []
        for v1, v2 in zip(V1, V2):
            sous.append(float(v1 - v2))
        print(f"Sous Vector is : {sous}")
