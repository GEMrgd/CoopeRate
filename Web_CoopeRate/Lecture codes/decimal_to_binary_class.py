def recursive_decimal_to_binary_str(n):
    if n == 0:
        return ''
    else:
        return recursive_decimal_to_binary_str(n // 2) + str(n % 2)

def main():
    print(recursive_decimal_to_binary_str(6)) # 110
    print(recursive_decimal_to_binary_str(13)) # 1101
    print(recursive_decimal_to_binary_str(126)) # 1111110
    print(recursive_decimal_to_binary_str(509)) # 111111101

main()
