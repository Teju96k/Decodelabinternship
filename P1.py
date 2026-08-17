import re


def check_password(password):
    """
    Analyze a password and return its security score,
    strength, and suggestions.
    """

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, feedback


def main():
    print("=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("\nEnter your password: ")

    if not password:
        print("Password cannot be empty.")
        return

    strength, score, feedback = check_password(password)

    print("\n" + "-" * 50)
    print("PASSWORD ANALYSIS")
    print("-" * 50)

    print("Length              :", len(password))
    print("Uppercase Letter    :", "Yes" if re.search(r"[A-Z]", password) else "No")
    print("Lowercase Letter    :", "Yes" if re.search(r"[a-z]", password) else "No")
    print("Number              :", "Yes" if re.search(r"[0-9]", password) else "No")
    print("Special Character   :", "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No")

    print("\nScore               :", f"{score}/5")
    print("Password Strength   :", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(" -", item)
    else:
        print("\nExcellent! Your password satisfies all basic security checks.")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()