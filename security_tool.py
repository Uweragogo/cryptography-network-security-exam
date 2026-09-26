from cryptography.fernet import Fernet
from pathlib import Path
import hashlib

KEY_FILE = Path.home() / "student_records_key.key"


def get_key():
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        print(f"Encryption key created at: {KEY_FILE}")
    else:
        key = KEY_FILE.read_bytes()

    return key


def encrypt_file(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        return False

    try:
        key = get_key()
        cipher = Fernet(key)

        data = input_path.read_bytes()
        encrypted_data = cipher.encrypt(data)

        output_path.write_bytes(encrypted_data)

        print(f"File encrypted successfully: {output_file}")
        return True

    except Exception as error:
        print(f"Encryption error: {error}")
        return False


def decrypt_file(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        return False

    try:
        key = get_key()
        cipher = Fernet(key)

        encrypted_data = input_path.read_bytes()
        decrypted_data = cipher.decrypt(encrypted_data)

        output_path.write_bytes(decrypted_data)

        print(f"File decrypted successfully: {output_file}")
        return True

    except Exception as error:
        print(f"Decryption error: {error}")
        return False


def verify_files(original_file, decrypted_file):
    original_path = Path(original_file)
    decrypted_path = Path(decrypted_file)

    if not original_path.exists() or not decrypted_path.exists():
        print("Error: One or both files are missing.")
        return False

    try:
        original_data = original_path.read_bytes()
        decrypted_data = decrypted_path.read_bytes()

        if original_data == decrypted_data:
            print("Verification successful: decrypted file matches the original.")
            return True
        else:
            print("Verification failed: files do not match.")
            return False

    except Exception as error:
        print(f"Verification error: {error}")
        return False


def calculate_sha256(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File not found: {file_path}")
        return None

    try:
        sha256 = hashlib.sha256()

        with path.open("rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        file_hash = sha256.hexdigest()

        print(f"SHA-256: {file_hash}")

        return file_hash

    except Exception as error:
        print(f"Hashing error: {error}")
        return None


def save_baseline_hash(file_path, hash_file):
    file_hash = calculate_sha256(file_path)

    if file_hash is None:
        return False

    Path(hash_file).write_text(file_hash)

    print(f"Baseline hash saved to: {hash_file}")

    return True


def check_integrity(file_path, hash_file):
    hash_path = Path(hash_file)

    if not hash_path.exists():
        print("Error: Baseline hash file not found.")
        return False

    expected_hash = hash_path.read_text().strip()
    current_hash = calculate_sha256(file_path)

    if current_hash == expected_hash:
        print("Integrity check passed: file has not changed.")
        return True
    else:
        print("Integrity check failed: file has changed.")
        return False


if __name__ == "__main__":

    # Encryption
    encrypt_file(
        "student_record.txt",
        "student_record.encrypted"
    )

    # Decryption
    decrypt_file(
        "student_record.encrypted",
        "student_record_decrypted.txt"
    )

    # Verification
    verify_files(
        "student_record.txt",
        "student_record_decrypted.txt"
    )

    # Integrity testing
    print("\n--- Integrity Test ---")

    hash_file = "student_record.sha256"

    if not Path(hash_file).exists():

        print("No baseline hash found.")
        print("Creating baseline hash...")

        save_baseline_hash(
            "student_record.txt",
            hash_file
        )

        print("Baseline hash created.")
        print("Run the program again after changing the file to test detection.")

    else:

        print("Checking file against the baseline hash...")

        check_integrity(
            "student_record.txt",
            hash_file
        )