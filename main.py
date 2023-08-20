import tkinter as tk
from tkinter import filedialog
import webbrowser

# Variables to track the state of the UI components
file_selected = False
data_pulled = False
browser_opened = False
file_path = ""


# Function to open a file dialog and get the selected file path
def select_file():
    global file_selected, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_selected = True
        file_status.config(text="Selected", fg="green")


# Function to process the selected file
def process_file():
    global data_pulled
    if not file_selected or data_pulled:
        return

    # Convert the extracted values from hex to IP using the provided link
    with open(file_path, 'r') as file:
        lines = file.readlines()
        extracted_values = [line.strip().split(',')[2] for line in lines]
        data_pulled = True
        pull_status.config(text="Pulled", fg="green")
        pull_button.config(state=tk.DISABLED)

        # Write the extracted values to a new file named "pulled_data"
        with open('pulled_data.txt', 'w') as output_file:
            for value in extracted_values:
                output_file.write(value + '\n')


# Function to open the Browserling URL for hex to IP conversion
def open_browserling():
    global browser_opened
    if not browser_opened:
        url = "https://www.browserling.com/tools/hex-to-ip"
        webbrowser.open(url)
        browser_opened = True


# Function to open "pulled_data.txt" in a new window
def open_pulled_data():
    with open('pulled_data.txt', 'r') as pulled_data_file:
        data = pulled_data_file.read()

    # Create a new window for displaying "pulled_data.txt"
    window = tk.Toplevel(root)
    window.title("Pulled Data")
    window.geometry("800x300")

    text_widget = tk.Text(window, wrap=tk.WORD)
    text_widget.insert(tk.END, data)
    text_widget.pack(fill=tk.BOTH, expand=True)


# Create the main window
root = tk.Tk()
root.title("Data Processor")
root.geometry("800x800")

# Create "Select File" button
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)

# Create label to indicate file selection status
file_status = tk.Label(root, text="", fg="green")
file_status.pack()

# Create "Pull Data" button
pull_button = tk.Button(root, text="Pull Data", command=process_file)
pull_button.pack(pady=10)

# Create label to indicate data pulling status
pull_status = tk.Label(root, text="", fg="green")
pull_status.pack()

# Create "Hex To IP" button
hex_to_ip_button = tk.Button(root, text="Hex To IP", command=open_browserling, fg="red")
hex_to_ip_button.pack(pady=10)

# Create "Open Pulled Data" button
open_pulled_data_button = tk.Button(root, text="Open Pulled Data", command=open_pulled_data)
open_pulled_data_button.pack(pady=10)

# Run the main loop
root.mainloop()
