def is_even(n):
    return n % 2 == 0

def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    if start >= end:
        print("Start of range should be less than the end.")
        return
    even_squares = []
    odd_squares = []
    for num in range(start, end + 1):
        square = num ** 2
        if is_even(square):
            even_squares.append(square)
        else:
            odd_squares.append(square)
    print(f"\nEven squares between {start} and {end}: {even_squares}")
    print(f"Odd squares between {start} and {end}: {odd_squares}")
if __name__ == "__main__":
    main()
