def less(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        for file_name in params:
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    page_size = 20  # Number of lines to display at a time
                    start_line = 0

                    while start_line < len(lines):
                        end_line = min(start_line + page_size, len(lines))
                        page = lines[start_line:end_line]
                        
                        output=""
                        for line in page:
                            output += line
                        print(output)

                        user_input = input("\nPress 'q' to quit, 'n' for the next page: ")

                        if user_input == 'q':
                            break
                        elif user_input == 'n':
                            start_line += page_size
                        else:
                            return "Invalid input. Press 'q' to quit, 'n' for the next page."
            except FileNotFoundError:
                return f"File '{file_name}' not found."
    else:
        return "Usage: less [directory_path]"

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    less(file_name)
