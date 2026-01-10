
import random

def generate_random_numbers():
    numbers = []
    for i in range(25):
        numbers.append(random.randint(1, 10))
    return numbers

def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    return numbers[len(numbers)//2]

def calculate_mode(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    mode = numbers[0]
    max_count = freq[mode]

    for num in freq:
        if freq[num] > max_count:
            mode = num
            max_count = freq[num]

    return mode

def main():
    nums = generate_random_numbers()
    print("Numbers:", nums)
    print("Mean:", calculate_mean(nums))
    print("Median:", calculate_median(nums))
    print("Mode:", calculate_mode(nums))

main()
