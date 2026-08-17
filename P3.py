import re
from urllib.parse import urlparse


# Common words found in phishing messages
SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "verification",
    "password",
    "otp",
    "account suspended",
    "account locked",
    "click now",
    "confirm",
    "login",
    "winner",
    "prize",
    "refund",
    "limited time",
    "immediately"
]


def extract_urls(message):
    """
    Extract HTTP and HTTPS URLs from a message.
    """

    pattern = r"https?://[^\s]+"

    return re.findall(pattern, message)


def check_url(url):
    """
    Check a URL for basic phishing indicators.
    """

    red_flags = []

    parsed_url = urlparse(url)

    # Check HTTPS
    if parsed_url.scheme != "https":
        red_flags.append("Website does not use HTTPS.")

    hostname = parsed_url.hostname

    if not hostname:
        red_flags.append("Invalid or suspicious URL.")
        return red_flags

    hostname = hostname.lower()

    # IP address instead of domain
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    if re.match(ip_pattern, hostname):
        red_flags.append(
            "URL uses an IP address instead of a domain name."
        )

    # @ symbol can hide the real destination
    if "@" in url:
        red_flags.append(
            "URL contains '@', which can hide the actual destination."
        )

    # Suspicious words
    suspicious_domain_words = [
        "login",
        "verify",
        "secure",
        "account",
        "update",
        "confirm"
    ]

    for word in suspicious_domain_words:

        if word in hostname:
            red_flags.append(
                f"Domain contains suspicious word: '{word}'."
            )

    # Excessively long URL
    if len(url) > 100:
        red_flags.append(
            "URL is unusually long."
        )

    # Too many subdomains
    if hostname.count(".") >= 4:
        red_flags.append(
            "URL contains an unusually large number of subdomains."
        )

    return red_flags


def analyze_message(message):
    """
    Analyze an email/message for common phishing indicators.
    """

    red_flags = []

    message_lower = message.lower()

    # Check suspicious keywords
    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in message_lower:
            found_keywords.append(keyword)

    if found_keywords:
        red_flags.append(
            "Suspicious keywords detected: "
            + ", ".join(found_keywords)
        )

    # Generic greeting
    generic_greetings = [
        "dear customer",
        "dear user",
        "dear member",
        "dear account holder"
    ]

    for greeting in generic_greetings:

        if greeting in message_lower:
            red_flags.append(
                "Generic greeting detected."
            )
            break

    # Requests for sensitive information
    sensitive_words = [
        "password",
        "otp",
        "credit card",
        "debit card",
        "bank account",
        "pin"
    ]

    if any(word in message_lower for word in sensitive_words):

        red_flags.append(
            "Message may request sensitive information."
        )

    # Urgency
    urgency_words = [
        "urgent",
        "immediately",
        "within 24 hours",
        "act now",
        "limited time"
    ]

    if any(word in message_lower for word in urgency_words):

        red_flags.append(
            "Message creates a sense of urgency."
        )

    # Extract and analyze URLs
    urls = extract_urls(message)

    url_analysis = {}

    for url in urls:

        url_flags = check_url(url)

        url_analysis[url] = url_flags

        for flag in url_flags:

            red_flags.append(
                f"{url} -> {flag}"
            )

    # Remove duplicate red flags
    red_flags = list(dict.fromkeys(red_flags))

    # Determine risk level
    if len(red_flags) >= 4:

        risk = "HIGH RISK - LIKELY PHISHING"

    elif len(red_flags) >= 2:

        risk = "MEDIUM RISK - SUSPICIOUS"

    elif len(red_flags) == 1:

        risk = "LOW/MEDIUM RISK - VERIFY MESSAGE"

    else:

        risk = "LOW RISK - NO OBVIOUS RED FLAGS"

    return risk, red_flags, urls, url_analysis


def main():

    print("=" * 65)
    print("             PHISHING AWARENESS ANALYZER")
    print("=" * 65)

    print("\nEnter the email/message to analyze.")
    print("Press ENTER on an empty line when finished.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    message = "\n".join(lines)

    if not message.strip():

        print("\nNo message entered.")
        return

    risk, red_flags, urls, url_analysis = analyze_message(message)

    print("\n" + "=" * 65)
    print("                 ANALYSIS RESULT")
    print("=" * 65)

    print("\nRisk Assessment:")
    print(risk)

    print("\nLinks Detected:")

    if urls:

        for url in urls:
            print(" -", url)

    else:

        print(" - No links detected.")

    print("\nRed Flags:")

    if red_flags:

        for number, flag in enumerate(red_flags, 1):
            print(f" {number}. {flag}")

    else:

        print(" - No obvious red flags detected.")

    print("\nWhy could this be unsafe?")

    if red_flags:

        print(
            "The message contains one or more indicators "
            "commonly associated with phishing. Verify the "
            "sender and website through an official channel "
            "before clicking links or providing information."
        )

    else:

        print(
            "No obvious phishing indicators were detected. "
            "However, this does not guarantee that the message "
            "is safe."
        )

    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()