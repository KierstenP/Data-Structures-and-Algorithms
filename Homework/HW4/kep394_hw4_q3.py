def print_triangle(n):
    if n == 1:
        print("*")
    if n > 1:
        print_triangle(n - 1)
        print(n * "*")

def print_opposite_triangle(n):
    if n == 1:
        print("*")
        print("*")
    if n > 1:
        print(n * "*")
        print_opposite_triangle(n - 1)
        print(n * "*")
def print_ruler(n):
    if n == 1:
        print("-")
        print("-")
    if n > 1:
        print(n * "-")
        print_ruler(n - 1)
        print(n * "-")

