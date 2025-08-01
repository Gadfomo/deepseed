
import re

common_passwords = [
    "123456", "password", "123456789", "12345678", "12345",
    "111111", "1234567", "sunshine", "qwerty", "iloveyou",
    "princess", "admin", "welcome", "monkey", "abc123",
    "football", "letmein", "dragon", "baseball", "starwars",
    "passw0rd", "loveme"
]

suggestions = {
    "Length (8+ chars)": "Use at least 8 characters",
    "Uppercase letter": "Add uppercase letters (A–Z)",
    "Lowercase letter": "Add lowercase letters (a–z)",
    "Number": "Include numbers (0–9)",
    "Special character (!@#$%^&*)": "Use special characters like !, @, #, etc.",
    "Not a common password": "Avoid common password patterns"
}

def analyze_password(password):
    results = {}

    results["Length (8+ chars)"] = len(password) >= 8
    results["Uppercase letter"] = any(char.isupper() for char in password)
    results["Lowercase letter"] = any(char.islower() for char in password)
    results["Number"] = any(char.isdigit() for char in password)
    results["Special character (!@#$%^&*)"] = any(char in "!@#$%^&*" for char in password)
    results["Not a common password"] = password not in common_passwords

    return results


print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")

# Analyze the password
results = analyze_password(password)

# Calculate score
points_per_criterion = 20
score = sum(points_per_criterion for passed in results.values() if passed)

# Determine strength
if score <= 40:
    strength = "Weak"
elif score <= 60:
    strength = "Fair"
elif score <= 80:
    strength = "Good"
elif score <= 100:
    strength = "Strong"
else:
    strength = "Excellent"

# Display results
print("\n🔒 SECURITY ANALYSIS RESULTS")
print(f"Password: {password}")
print(f"Score: {score}/120 ({strength})\n")

for criterion, passed in results.items():
    print(f"{'✅' if passed else '❌'} {criterion}")

# Suggestions for improvement
failed = [criterion for criterion, passed in results.items() if not passed]

if failed:
    print("\n💡 SUGGESTIONS:")
    for item in failed:
        print(f"- {suggestions[item]}")
else:
    print("\n🎉 Your password is excellent! No improvements needed.")
