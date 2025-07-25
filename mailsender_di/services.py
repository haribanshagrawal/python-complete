from email_sender import EmailService


class Smtp(EmailService):
    def __init__(self, smtp_server: str, signature: str = "") -> None:
        self.smtp_server = smtp_server
        self.signature = signature

    def send_email(self, to_address: str, subject: str, body: str) -> str:
        # Implement SMTP email sending logic
        formatted_body = f"{body}\n\n-- {self.signature}"
        return f"Sent email to {to_address} with subject '{subject}' and body: {formatted_body} using SMTP"


class SendGrid(EmailService):
    def send_email(self, to_address: str, subject: str, body: str) -> str:
        return f"Sent email to {to_address} with subject '{subject}' and body: {body} using SendGrid"


class MailChimp(EmailService):
    def __init__(self, attachment: str = "") -> None:
        self.attachment: str = attachment

    def send_email(self, to_address: str, subject: str, body: str) -> str:
        base_message = f"Sent email to {to_address} with subject '{subject}' and body: {body} using MailChimp"
        if self.attachment:
            return base_message + f"with attachement {self.attachment}"

        return base_message

    def add_attachment(self, file_path: str) -> None:
        """
        Add an attachment to the email.
        """
        self.attachment = f"Added {file_path} attachment"