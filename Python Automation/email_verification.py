import re
import smtplib

def email_verification(email_address):
    # Regular expression pattern for email validation
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    # Check if email address matches the pattern
    if pattern.match(email_address):
        # Split the email address into user and domain
        user, domain = email_address.split("@")
        try:
            # Try to connect to the email server
            server = smtplib.SMTP("smtp." + domain)
            server.ehlo()
            server.starttls()
            server.ehlo()
            # Check if the email address exists
            status, message = server.rcpt(email_address)
            server.quit()
            # Return result of email verification
            if status == 250:
                return True
            else:
                return False
        except:
            # Return False if the email server is not found
            return False
    else:
        # Return False if the email address does not match the pattern
        return False

# Example usage
email = input("Enter an email address: ")
result = email_verification(email)
if result:
    print("Email is valid")
else:
    print("Email is not valid")
