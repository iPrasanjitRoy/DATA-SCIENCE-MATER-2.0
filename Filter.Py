def check_even(number):
 
 if number % 2 == 0:
        return True 
 return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers_iterator = filter(check_even, numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers) 

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
 vowels = ['a', 'e', 'i', 'o', 'u']
 return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)
vowels = tuple(filtered_vowels)
print(vowels) 

