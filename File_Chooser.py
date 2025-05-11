from plyer import filechooser

file_path = filechooser.open_file()
print("File-path is: ",file_path)

file_paths = filechooser.open_file(multiple= True)
print("File-paths is: ",file_paths)

file_path = filechooser.save_file()
print("Save-path is: ",file_path)