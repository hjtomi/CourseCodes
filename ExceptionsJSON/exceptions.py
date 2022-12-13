# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "x")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


