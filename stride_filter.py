import os

# Path to the cloned repository
attacks_dir = "known-cyber-attacks"

# Ask user for STRIDE category
stride_category = input("Enter STRIDE category (e.g., Tampering): ").strip().lower()

# List to store matching attacks
matching_attacks = []

# Iterate over each folder in the attacks directory
for attack_name in os.listdir(attacks_dir):
    attack_path = os.path.join(attacks_dir, attack_name)
    if os.path.isdir(attack_path):
        # Look for .md files inside the attack folder
        for file_name in os.listdir(attack_path):
            if file_name.endswith(".md"):
                file_path = os.path.join(attack_path, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                    if stride_category in content:
                        matching_attacks.append(attack_name)

# Print results
if matching_attacks:
    print(f"Attacks matching STRIDE category '{stride_category}':")
    for attack in matching_attacks:
        print(f"- {attack}")
else:
    print(f"No attacks found for STRIDE category '{stride_category}'.")
