import os

folder_path = "/home/najib/Extra/Merger/data/text"
output_file = os.path.join(folder_path, "merged.txt")

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt") and filename != "merged.txt":
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n")

print(f"Merged file successfully created: {output_file}")