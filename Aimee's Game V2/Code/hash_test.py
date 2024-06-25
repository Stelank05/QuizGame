from tkinter import *

window = Tk()

window.geometry("420x420")

image = PhotoImage(file = "C:\\Users\\Steph\\Downloads\\GEM S16.png")
button = Button(window, image = image)
button.place(x = 10, y = 10)#, width = 400, height = 400)

window.mainloop()




"""import hashlib

def calculate_sha256(data):
    # Convert data to bytes if it’s not already
    if isinstance(data, str):
        data = data.encode()

    # Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).hexdigest()

    return sha256_hash

# Example usage:
input_data = "He11o, World!"
hash_value = calculate_sha256(input_data)
print("SHA-256 Hash:", hash_value)"""