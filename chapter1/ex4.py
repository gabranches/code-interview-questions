def count_letters(s):
    letter_counts = {}
    for char in s.lower().replace(' ', ''):
        if char in letter_counts.keys():
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts


def check_odds(dict):
    count = 0
    for key in dict:
        if dict[key] == 1:
            count += 1
            if count > 1: return False
    return True


def check_palindrome(input):
    return check_odds(count_letters(input))


if __name__ == '__main__':
    
    input = 'a car a man a maraca'
    print(check_palindrome(input))

