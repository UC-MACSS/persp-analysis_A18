def pal_three_digit():
    '''
    Find the product of three digit numbers that is a palindrome

    Input: None

    Returns: (int) a product of three digit number which 
            is a palindrome
    '''
    max_product = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j 
            if is_palindrome(str(product)):
                if product > max_product:
                    max_product = product
    return max_product

def is_palindrome(string):
    '''
    Test if a string is a palindrome
    
    Input: (str) a string 

    Returns: (bool) True if a string is a palindrome, False otherwise

    '''
    return string == string[::-1]

if __name__=='__main__':

    print(pal_three_digit())