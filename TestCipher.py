# File: TestCipher.py

#  Description: Test Cipher and Decipher

#  Student Name: William Kwon

#  Student UT EID: uk669

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/7/18

#  Date Last Modified: 9/10/18
# takes a single string as input parameter and returns a string

def substitution_encode ( strng ):
  cipher = [ 'q', 'a', 'z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p' , 'o', 'l', 'p' ]  
  encoded=' '
  strng.lower()                               
  for x in strng:
      if  x.isalpha():                      # for non char character        
          idx = ord(x) - ord('a')           #turn into unicode for ciphering    
          encoded += cipher[idx]
      else:
          encoded += x                        
  
  return encoded
# takes a single string as input parameter and returns a string
def substitution_decode ( strng ):
  cipher = [ 'q', 'a', 'z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p' , 'o', 'l', 'p' ]  
  decoded=' '
  strng.lower()
  for x in strng:
      if  x.isalpha():                # for non char character                 
          idx = cipher.index(x) + ord('a')         #turn into unicode for ciphering             
          decoded += chr(idx)
      else:
          decoded += x                        
  
  return decoded

# takes two strings as input parameter and returns a string
def vigenere_encode ( strng, passwd ):
  alphabet= [ 'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

  strng_len=len(strng)
  strng.lower()
  passwd_length = len(passwd)                                
  count_index = 0                                                  # this will work as move letter to next position
  v_encoded = ''
  for x in range(len(strng)):                  
      if strng[x].isalpha():  
          raw_pass=strng[x]                                # for non char character
          alphabettoindex = alphabet.index(raw_pass)            # convert passwoerd into alphabate base index
          passwd_index = count_index % passwd_length              # index of letter in password used to cipher
          count_index += 1                                             # move letters to next position
          passwedtoalphabet = alphabet.index(passwd[passwd_index])  # index of passwords in to alphbet base index
          v_index = (passwedtoalphabet + alphabettoindex) % 26       # put into right index
                                                                                     
          v_encoded += alphabet[v_index]         #assign letter from alphabet list using index
      else:
          v_encoded += strng[x]  
  return v_encoded



# takes two strings as input parameter and returns a string
def vigenere_decode ( strng, passwd ):
  alphabet= [ 'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
  strng_len=len(strng)
  strng.lower()
  passwd_length = len(passwd)                                
  count_index = 0                                                    
  v_decoded = ''
  for x in range(len(strng)):
       if strng[x].isalpha():
           
           raw_pass = strng[x]
           passwd_index = count_index % passwd_length
           count_index += 1                                           
           passwedtoalphabet = alphabet.index(passwd[passwd_index])
           alphabettoindex = alphabet.index(raw_pass)                              # same as encode steps above
           if alphabettoindex < passwedtoalphabet:                                 # check if alphabet index greater than index of passwords in alphabaset base to convert back 
                                                                                    
            alphabettoindex = alphabettoindex + len(alphabet) - passwedtoalphabet  # put itin to right index
           else:
            alphabettoindex = alphabettoindex - passwedtoalphabet
           v_decoded += alphabet[alphabettoindex]                                  #assign letter from alphabet list using index
       else:
        v_decoded += strng[x]
  return v_decoded
  
def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()