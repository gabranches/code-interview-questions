def is_substring(s, ss):
    return s in ss

def is_rotation(old, new):
    return is_substring(new, old + old)

if __name__ == '__main__':    

    print(is_rotation('waterbottle', 'erbottlewat'))