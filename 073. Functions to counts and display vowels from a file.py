def vowelCount():
    # Define the path to the file
    file_path = 'sample//story.txt'
    
    # Define vowels
    vowels = 'aeiouAEIOU'
    
    try:
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Count the vowels
        count = sum(1 for char in content if char in vowels)
        
        # Display the result
        print(f"Number of vowels in '{file_path}': {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

vowelCount()