
def count_pairs_with_sum_ten(numbers):
    pair_count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                pair_count += 1
    return pair_count

def main():
    numbers = [2, 7, 4, 1, 3, 6]
    print("Pair count:", count_pairs_with_sum_ten(numbers))

main()
