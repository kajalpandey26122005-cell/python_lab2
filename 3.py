"""
Simple Password Manager
Uses only built-in Python libraries (no pip install needed)
"""

import os
import json
import getpass
import secrets
import string
import hashlib
import base64


class PasswordManager:
    def __init__(self):
        self.passwords_file = "passwords.json"
        self.master_hash_file = "master.hash"
        self.passwords = {}
        self.key = None
        
    def hash_password(self, password: str) -> str:
        """Create a hash of the password"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def simple_encrypt(self, text: str) -> str:
        """Simple XOR encryption with key"""
        encrypted = []
        key_bytes = self.key.encode()
        text_bytes = text.encode()
        
        for i, char in enumerate(text_bytes):
            key_char = key_bytes[i % len(key_bytes)]
            encrypted.append(char ^ key_char)
        
        return base64.b64encode(bytes(encrypted)).decode()
    
    def simple_decrypt(self, encrypted_text: str) -> str:
        """Simple XOR decryption with key"""
        try:
            encrypted_bytes = base64.b64decode(encrypted_text.encode())
            decrypted = []
            key_bytes = self.key.encode()
            
            for i, char in enumerate(encrypted_bytes):
                key_char = key_bytes[i % len(key_bytes)]
                decrypted.append(char ^ key_char)
            
            return bytes(decrypted).decode()
        except:
            return None
    
    def verify_master_password(self, master_password: str) -> bool:
        """Verify the master password"""
        if not os.path.exists(self.master_hash_file):
            # First time setup
            password_hash = self.hash_password(master_password)
            with open(self.master_hash_file, 'w') as f:
                f.write(password_hash)
            return True
        else:
            # Verify existing password
            with open(self.master_hash_file, 'r') as f:
                stored_hash = f.read()
            return self.hash_password(master_password) == stored_hash
    
    def initialize(self, master_password: str) -> bool:
        """Initialize the password manager"""
        if not self.verify_master_password(master_password):
            return False
        
        self.key = master_password
        
        if os.path.exists(self.passwords_file):
            self.load_passwords()
        
        return True
    
    def load_passwords(self):
        """Load and decrypt passwords from file"""
        try:
            with open(self.passwords_file, 'r') as f:
                encrypted_data = json.load(f)
            
            self.passwords = {}
            for service, data in encrypted_data.items():
                decrypted_password = self.simple_decrypt(data['password'])
                if decrypted_password:
                    self.passwords[service] = {
                        'username': data['username'],
                        'password': decrypted_password
                    }
        except Exception as e:
            print(f"Error loading passwords: {e}")
            self.passwords = {}
    
    def save_passwords(self):
        """Encrypt and save passwords to file"""
        try:
            encrypted_data = {}
            for service, data in self.passwords.items():
                encrypted_data[service] = {
                    'username': data['username'],
                    'password': self.simple_encrypt(data['password'])
                }
            
            with open(self.passwords_file, 'w') as f:
                json.dump(encrypted_data, f, indent=2)
            
            print("✓ Passwords saved successfully")
        except Exception as e:
            print(f"Error saving passwords: {e}")
    
    def add_password(self, service: str, username: str, password: str):
        """Add a new password entry"""
        self.passwords[service] = {
            "username": username,
            "password": password
        }
        self.save_passwords()
        print(f"✓ Password for '{service}' added successfully")
    
    def get_password(self, service: str):
        """Retrieve a password for a service"""
        if service in self.passwords:
            data = self.passwords[service]
            print(f"\n{'='*50}")
            print(f"Service:  {service}")
            print(f"Username: {data['username']}")
            print(f"Password: {data['password']}")
            print(f"{'='*50}\n")
        else:
            print(f"✗ No password found for '{service}'")
    
    def list_services(self):
        """List all stored services"""
        if not self.passwords:
            print("No passwords stored yet.")
            return
        
        print(f"\n{'='*50}")
        print("Stored Services:")
        print(f"{'='*50}")
        for i, service in enumerate(self.passwords.keys(), 1):
            username = self.passwords[service]['username']
            print(f"{i}. {service} ({username})")
        print(f"{'='*50}\n")
    
    def delete_password(self, service: str):
        """Delete a password entry"""
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            print(f"✓ Password for '{service}' deleted successfully")
        else:
            print(f"✗ No password found for '{service}'")
    
    def update_password(self, service: str, new_password: str):
        """Update password for existing service"""
        if service in self.passwords:
            self.passwords[service]['password'] = new_password
            self.save_passwords()
            print(f"✓ Password for '{service}' updated successfully")
        else:
            print(f"✗ No password found for '{service}'")
    
    @staticmethod
    def generate_password(length: int = 16, use_symbols: bool = True):
        """Generate a strong random password"""
        characters = string.ascii_letters + string.digits
        if use_symbols:
            characters += string.punctuation
        
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    @staticmethod
    def check_password_strength(password: str) -> str:
        """Check password strength"""
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        score = sum([length >= 8, length >= 12, has_upper, has_lower, has_digit, has_symbol])
        
        if score <= 2:
            return "Weak 😟"
        elif score <= 4:
            return "Medium 😐"
        else:
            return "Strong 💪"


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("          PASSWORD MANAGER")
    print("="*50)
    print("1. Add new password")
    print("2. Get password")
    print("3. List all services")
    print("4. Update password")
    print("5. Delete password")
    print("6. Generate strong password")
    print("7. Check password strength")
    print("8. Exit")
    print("="*50)


def main():
    pm = PasswordManager()
    
    print("\n🔐 Welcome to Password Manager")
    print("=" * 50)
    
    # Check if this is first time use
    if not os.path.exists(pm.master_hash_file):
        print("First time setup!")
        master_password = getpass.getpass("Create a master password: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        
        if master_password != confirm_password:
            print("✗ Passwords don't match. Please try again.")
            return
        
        if len(master_password) < 6:
            print("✗ Master password must be at least 6 characters.")
            return
    else:
        master_password = getpass.getpass("Enter your master password: ")
    
    if not pm.initialize(master_password):
        print("✗ Incorrect master password!")
        return
    
    print("✓ Password manager initialized\n")
    
    while True:
        display_menu()
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == "1":
            service = input("Enter service name (e.g., Gmail, GitHub): ").strip()
            if not service:
                print("✗ Service name cannot be empty")
                continue
                
            username = input("Enter username/email: ").strip()
            
            use_generated = input("Generate strong password? (y/n): ").lower().strip()
            if use_generated == 'y':
                length = input("Password length (default 16): ").strip()
                length = int(length) if length.isdigit() else 16
                password = pm.generate_password(length)
                print(f"Generated password: {password}")
            else:
                password = getpass.getpass("Enter password: ")
            
            pm.add_password(service, username, password)
        
        elif choice == "2":
            service = input("Enter service name: ").strip()
            pm.get_password(service)
        
        elif choice == "3":
            pm.list_services()
        
        elif choice == "4":
            service = input("Enter service name: ").strip()
            
            use_generated = input("Generate new strong password? (y/n): ").lower().strip()
            if use_generated == 'y':
                length = input("Password length (default 16): ").strip()
                length = int(length) if length.isdigit() else 16
                new_password = pm.generate_password(length)
                print(f"Generated password: {new_password}")
            else:
                new_password = getpass.getpass("Enter new password: ")
            
            pm.update_password(service, new_password)
        
        elif choice == "5":
            service = input("Enter service name: ").strip()
            confirm = input(f"Are you sure you want to delete '{service}'? (y/n): ").lower()
            if confirm == 'y':
                pm.delete_password(service)
        
        elif choice == "6":
            length = input("Password length (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            use_symbols = input("Include symbols? (y/n, default y): ").lower().strip()
            use_symbols = use_symbols != 'n'
            
            password = pm.generate_password(length, use_symbols)
            print(f"\nGenerated password: {password}")
            print(f"Strength: {pm.check_password_strength(password)}\n")
        
        elif choice == "7":
            password = getpass.getpass("Enter password to check: ")
            strength = pm.check_password_strength(password)
            print(f"\nPassword strength: {strength}\n")
        
        elif choice == "8":
            print("\n👋 Goodbye! Your passwords are secure.")
            break
        
        else:
            print("✗ Invalid option. Please try again.")


if __name__ == "__main__":
    main()