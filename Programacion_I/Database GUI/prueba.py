class py_solution:
    def int_to_Roman(self, num):
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, roman) in lookup:
            (d, num) = divmod(num, n)
            res += roman * d
        return res
print(py_solution().int_to_Roman(3))