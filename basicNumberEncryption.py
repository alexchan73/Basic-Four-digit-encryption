#Created by Alex Chan

#Setting input from the user in split
def to_list(user_input):
  separate_elements_list = []
  separate_elements_list[:] = user_input  
  return separate_elements_list
encrypted_list = [] 

#Encryption Algortihm
def encrypt_algorithm(encrypted_list, user_input):
  for digit in user_input:
    encrypt = int(digit) + 7 % 10 #take the digit, add it by 7, moduluo 10
    encrypted_list.append(encrypt) #append the encrypted digit back into the list
  return encrypted_list

def swap( encrypted_list):
  encrypted_list[0] , encrypted_list[2] = encrypted_list[2] , encrypted_list[0] #swapping index 0 with index 2
  encrypted_list[1] , encrypted_list[3] = encrypted_list[3] , encrypted_list[1] #swapping index 1 with index 3
  return encrypted_list

def no_whitespace(encrypted_list):
  encrypted_list = [str(x) for x in encrypted_list]  #removing whitespace in final output
  encrypted_list = ''.join(encrypted_list)
  return encrypted_list


user_input = input("Hello! Please Enter a 4 digit number for me to encrypt: ")

print("Here is the the 4 digits in a list: " + str(to_list(user_input)))

print("Here is the encrypted digits before swapping: " + str(encrypt_algorithm(encrypted_list, user_input)))

print("Here is the encrypted digits AFTER swapping: " + str(swap(encrypted_list)))

print("Here is the digits without whitespace: " + str(no_whitespace(encrypted_list)))
