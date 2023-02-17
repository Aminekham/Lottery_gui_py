import tkinter as tk
import random

def generate_numbers():
    # Generate the numbers for the lottery
    min_num = int(min_entry.get())
    max_num = int(max_entry.get())
    num_of_numbers = int(num_entry.get())
    numbers = random.sample(range(min_num, max_num + 1), num_of_numbers)

    # Display the numbers in the result label
    result_label.config(text=" ".join(str(num) for num in numbers))

    # Export the numbers to a .txt file
    with open("generated_numbers.txt", "w") as file:
        file.write("winning number:\n".join(str(random.sample(numbers, 1))))
        file.write("\n".join(str(num) for num in numbers ))

# Create the main window
root = tk.Tk()
root.title("Lottery System")
root.geometry("1920x1080")


# Create the frames
input_frame = tk.Frame(root)
input_frame.pack(pady=30)

result_frame = tk.Frame(root)
result_frame.pack(pady=30)

# Create the input widgets
min_label = tk.Label(input_frame, text="Minimum number:", font=("Helvetica", 14))
min_entry = tk.Entry(input_frame, font=("Helvetica", 14))

max_label = tk.Label(input_frame, text="Maximum number:", font=("Helvetica", 14))
max_entry = tk.Entry(input_frame, font=("Helvetica", 14))

num_label = tk.Label(input_frame, text="Number of numbers:", font=("Helvetica", 14))
num_entry = tk.Entry(input_frame, font=("Helvetica", 14))

# Place the input widgets on the frame
min_label.grid(row=0, column=0, sticky="W", pady=10)
min_entry.grid(row=0, column=1, pady=10)

max_label.grid(row=1, column=0, sticky="W", pady=10)
max_entry.grid(row=1, column=1, pady=10)

num_label.grid(row=2, column=0, sticky="W", pady=10)
num_entry.grid(row=2, column=1, pady=10)

# Create the result widget
result_label = tk.Label(result_frame, text="", font=("Helvetica", 18))
result_label.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate", font=("Helvetica", 14), command=generate_numbers)
generate_button.pack(pady=30)

# Set the background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.pack(fill="both", expand="yes")

# Start the main loop
root.mainloop()
