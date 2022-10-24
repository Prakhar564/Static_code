def classify_triangle(side_a, side_b, side_c):
    if validation(side_a, side_b, side_c)== 'InvalidInput':
        return "InvalidInput"
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) \
            or ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2) \
            or ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2):
        return 'Right'
    if (side_b not in (side_a, side_c)) and (side_c not in (side_a, side_b)):
        return 'Scalene'
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return 'Isosceles'
    return None

def validation(side_a, side_b, side_c):
    if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_a >= 200 or side_b >= 200:
        return 'InvalidInput'
    if not (isinstance(side_a, int)
            and isinstance(side_b, int)
            and isinstance(side_c, int)) or side_c >= 200:
        return 'InvalidInput'
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return 'NotATriangle'
    return None