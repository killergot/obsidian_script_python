def calculate_rectangle_area_perimeter(dimensions: str) -> str:
    """Ваш код"""
    a = list(map(int, dimensions.split()))

    return f'{a[0] * a[1]} {(a[0] + a[1]) * 2}'


dimensions = input()
result = calculate_rectangle_area_perimeter(dimensions)
print(result)
