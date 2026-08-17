import getpass
import platform
import re
import subprocess
import shutil


class SecurityChecker:
    """
    Basic defensive security assessment tool.

    Checks:
    1. Password strength
    2. Software/update status guidance
    3. Unsafe user practices
    """

    def __init__(self):
        self.results = []

    # ---------------------------------------------------------
    # PASSWORD CHECK
    # ---------------------------------------------------------

    def check_password(self):

        print("\n" + "=" * 60)
        print("1. PASSWORD SECURITY CHECK")
        print("=" * 60)

        password = getpass.getpass(
            "Enter a test password: "
        )

        checks = {
            "Minimum length (8 characters)": len(password) >= 8,
            "Contains uppercase letter": bool(
                re.search(r"[A-Z]", password)
            ),
            "Contains lowercase letter": bool(
                re.search(r"[a-z]", password)
            ),
            "Contains number": bool(
                re.search(r"[0-9]", password)
            ),
            "Contains special character": bool(
                re.search(r"[^A-Za-z0-9]", password)
            )
        }

        score = sum(checks.values())

        print("\nPassword Analysis:")

        for check, passed in checks.items():

            status = "PASS" if passed else "FAIL"

            print(f"[{status}] {check}")

        print(f"\nPassword Security Score: {score}/5")

        if score == 5:

            print("Result: Strong password")

        elif score >= 3:

            print("Result: Medium password")

        else:

            print("Result: Weak password")

        self.results.append({
            "category": "Password Security",
            "score": score,
            "maximum": 5
        })

    # ---------------------------------------------------------
    # SOFTWARE UPDATE CHECK
    # ---------------------------------------------------------

    def check_software_updates(self):

        print("\n" + "=" * 60)
        print("2. SOFTWARE UPDATE STATUS")
        print("=" * 60)

        operating_system = platform.system()

        print("Operating System:", operating_system)

        if operating_system == "Windows":

            print("\nWindows detected.")

            print(
                "Please check:"
            )

            print(
                "Settings -> Windows Update -> Check for Updates"
            )

            print(
                "\nSecurity Recommendation:"
            )

            print(
                "Install important security updates regularly."
            )

        elif operating_system == "Linux":

            print("\nLinux detected.")

            print(
                "Use your distribution's package manager "
                "to check for updates."
            )

            print("\nFor Debian/Ubuntu:")
            print("sudo apt update")
            print("sudo apt upgrade")

        elif operating_system == "Darwin":

            print("\nmacOS detected.")

            print(
                "Open System Settings -> General -> "
                "Software Update."
            )

        else:

            print(
                "\nUnable to identify the operating system."
            )

        print(
            "\nNOTE: This program does not automatically "
            "install or modify system updates."
        )

    # ---------------------------------------------------------
    # SECURITY TOOLS CHECK
    # ---------------------------------------------------------

    def check_basic_tools(self):

        print("\n" + "=" * 60)
        print("3. BASIC SECURITY ENVIRONMENT CHECK")
        print("=" * 60)

        tools = [
            "python",
            "git",
            "curl"
        ]

        for tool in tools:

            path = shutil.which(tool)

            if path:

                print(f"[FOUND] {tool}")
                print(f"        Location: {path}")

            else:

                print(f"[NOT FOUND] {tool}")

    # ---------------------------------------------------------
    # USER SECURITY PRACTICES
    # ---------------------------------------------------------

    def check_user_practices(self):

        print("\n" + "=" * 60)
        print("4. USER SECURITY PRACTICES")
        print("=" * 60)

        questions = [
            "Do you use Multi-Factor Authentication (MFA)?",
            "Do you regularly update your software?",
            "Do you keep important data backed up?",
            "Do you avoid unknown links and attachments?",
            "Do you avoid installing software from untrusted sources?",
            "Do you lock your computer when away?"
        ]

        score = 0

        for question in questions:

            while True:

                answer = input(
                    f"\n{question} (y/n): "
                ).strip().lower()

                if answer == "y":

                    print("[PASS]")
                    score += 1
                    break

                elif answer == "n":

                    print("[FAIL]")
                    break

                else:

                    print(
                        "Invalid input. Please enter y or n."
                    )

        self.results.append({
            "category": "User Security Practices",
            "score": score,
            "maximum": len(questions)
        })

        return score, len(questions)

    # ---------------------------------------------------------
    # FINAL REPORT
    # ---------------------------------------------------------

    def generate_report(self):

        print("\n" + "=" * 60)
        print("             SECURITY ASSESSMENT REPORT")
        print("=" * 60)

        total_score = 0
        total_possible = 0

        for result in self.results:

            total_score += result["score"]
            total_possible += result["maximum"]

            percentage = (
                result["score"] /
                result["maximum"]
            ) * 100

            print(
                f"\n{result['category']}"
            )

            print(
                f"Score: {result['score']}/"
                f"{result['maximum']} "
                f"({percentage:.1f}%)"
            )

        if total_possible > 0:

            overall_percentage = (
                total_score /
                total_possible
            ) * 100

        else:

            overall_percentage = 0

        print("\n" + "-" * 60)

        print(
            f"Overall Score: "
            f"{total_score}/{total_possible}"
        )

        print(
            f"Overall Percentage: "
            f"{overall_percentage:.1f}%"
        )

        if overall_percentage >= 80:

            print("Risk Level: LOW")

        elif overall_percentage >= 60:

            print("Risk Level: MEDIUM")

        else:

            print("Risk Level: HIGH")

        print("\nRecommendations:")

        print("1. Use strong and unique passwords.")
        print("2. Enable Multi-Factor Authentication.")
        print("3. Keep operating systems and software updated.")
        print("4. Avoid suspicious links and attachments.")
        print("5. Maintain regular backups.")
        print("6. Install software only from trusted sources.")

        print("\n" + "=" * 60)


def main():

    print("=" * 60)
    print("          SYSTEM VULNERABILITY CHECKLIST")
    print("=" * 60)

    print(
        "\nPurpose: Identify basic security vulnerabilities "
        "through defensive checks."
    )

    checker = SecurityChecker()

    checker.check_password()

    checker.check_software_updates()

    checker.check_basic_tools()

    checker.check_user_practices()

    checker.generate_report()


if __name__ == "__main__":
    main()