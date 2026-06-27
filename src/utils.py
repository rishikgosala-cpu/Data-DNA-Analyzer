import os


def check_file_exists(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return True


def print_title(title):

    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)