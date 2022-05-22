import asyncio

from fastapi_mail import MessageSchema

from src.settings.mailer import fm

def send_activation_mail(first_name, email, token):
    email_body = f"""
Hello {first_name},

Congratulations your account has been created. in order login you need to activate your account.
Here is the code {token}"""
    message = MessageSchema(
        subject="Welecom to our platform [Activation needed]",
        recipients=[email],
        headers={'Token': token },
        body=email_body)
    asyncio.run(fm.send_message(message))
