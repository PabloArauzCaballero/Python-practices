class OrderinAlgorithms:
    @staticmethod
    def quicksort(arr: list) -> list:
        """
        Este tipo de algoritmo de ordenamiento se basa en el principio: "DIVIDE Y VENCERAS",
        dado que divide una tarea compleja en partes a través de la recursividad. Su algoritmo es:

            ALGORITMO quicksort (lista_valores):
                SI lista_valores.longitud <= 1:
                    RETORNAR lista_valores

                pivote = lista_valores[lista_valores.longitud // 2]

                menores = [elemento in lista_menores if elemento < pivote]
                iguales = [elemento in lista_menores if elemento = pivote]
                mayores = [elemento in lista_menores if elemento > pivote]

                RETORNAR quicksort(menores).concatenar(iguales).concatenar(quicksort(mayores));

        :param arr: lista_valores_desordenada
        :return: list
        """

        # Caso base
        if len(arr) <= 1:
            # Se retorna un val de tipo 'list' de modo de cumplir la restriccion return y asegurar la concatenación de cadenas
            return arr

        # Algoritmo
        pivote = arr[len(arr)//2]

        menores = [val for val in arr if val < pivote]
        iguales = [val for val in arr if val == pivote]
        mayores = [val for val in arr if val > pivote]

        return OrderinAlgorithms.quicksort(menores) + iguales + OrderinAlgorithms.quicksort(mayores)
