
def find_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"

    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return largest - smallest

def main():
    numbers = [5, 3, 8, 1, 0, 4]
    print("Range:", find_range(numbers))

main()
