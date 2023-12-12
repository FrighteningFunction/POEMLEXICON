import os
import shutil

def copy_txt_to_poems(root_dir):
    """Copy all .txt files from root directory to 'poems' subdirectory with new names."""
    poem_dir = os.path.join(root_dir, 'poems')
    if not os.path.exists(poem_dir):
        os.makedirs(poem_dir)

    # Collect existing poem files to determine the next unique number
    existing_poems = [f for f in os.listdir(poem_dir) if f.startswith('poem_') and f.endswith('.txt')]
    existing_numbers = [int(f.split('_')[1].split('.')[0]) for f in existing_poems]
    next_number = max(existing_numbers, default=0) + 1

    # Look for .txt files in the root directory only
    for file in os.listdir(root_dir):
        if file.endswith('.txt'):
            new_name = f'poem_{next_number}.txt'
            shutil.copy2(os.path.join(root_dir, file), os.path.join(poem_dir, new_name))
            next_number += 1

# Example usage
root_directory = './'  # Replace with your root directory path
copy_txt_to_poems(root_directory)
