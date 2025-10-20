name = input("Type your name: ")
print("Hello, {}!".format(name))
print("="*50)
original_message = "010"
secret_key = "110"

# Extract and encrypt each digit step by step
# --- First digit ---
first_digit_orig_msg = int(original_message[0])
first_digit_secret_key = int(secret_key[0])
first_digit_encrypt_msg = str(first_digit_orig_msg ^ first_digit_secret_key)

formatted_input = "The first digits of original messsage and secrete key are {} and {}, respectively."
print(formatted_input.format(first_digit_orig_msg, first_digit_secret_key))
formatted_output = "The first digit of encrypted messsage is {}."
print(formatted_output.format(first_digit_encrypt_msg))

# --- Second digit ---
second_digit_orig_msg = int(original_message[1])
second_digit_secret_key = int(secret_key[1])
second_digit_encrypt_msg = str(second_digit_orig_msg ^ second_digit_secret_key)

formatted_input = "The second digits of original messsage and secrete key are {} and {}, respectively."
print(formatted_input.format(second_digit_orig_msg, second_digit_secret_key))
formatted_output = "The second digit of encrypted messsage is {}."
print(formatted_output.format(second_digit_encrypt_msg))

# --- Third digit ---
third_digit_orig_msg = int(original_message[2])
third_digit_secret_key = int(secret_key[2])
third_digit_encrypt_msg = str(third_digit_orig_msg ^ third_digit_secret_key)

formatted_input = "The third digits of original messsage and secrete key are {} and {}, respectively."
print(formatted_input.format(third_digit_orig_msg, third_digit_secret_key))
formatted_output = "The third digit of encrypted messsage is {}."
print(formatted_output.format(third_digit_encrypt_msg))

# Combine encrypted digits
encrypted_msg = first_digit_encrypt_msg + second_digit_encrypt_msg + third_digit_encrypt_msg
print("The encrypted message is {}".format(encrypted_msg))

# --- Message Decryption ---
# XOR again with the same secret key to recover original message
decrypted_msg = "".join([str(int(encrypted_msg[i]) ^ int(secret_key[i])) for i in range(3)])
print("The decrypted message is {}".format(decrypted_msg))