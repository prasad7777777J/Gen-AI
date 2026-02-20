def is_non_prime(n):
    """Check if a number is non-prime (composite or special cases)."""
    if n < 2:
        return True  # 0, 1, and negatives are non-prime
    if n == 2:
        return False  # 2 is prime
    if n % 2 == 0:
        return True  # Even numbers > 2 are non-prime
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    
    return False  # Prime


# Test cases
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 9, 15, 20, 29]
    for num in test_numbers:
        print(f"{num} is non-prime: {is_non_prime(num)}")