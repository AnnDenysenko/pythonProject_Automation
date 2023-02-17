folder_path = "resources/text_documents"

file_name = "example.txt"

full_filename = f"{folder_path}/{file_name}"

with open(full_filename, "w+", encoding="utf-8") as file:
    file.write("our data")
