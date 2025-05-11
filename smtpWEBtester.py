from flask import Flask, render_template, request
import smtplib
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Untuk CSRF
load_dotenv()

class SMTPForm(FlaskForm):
    smtp_host = StringField('SMTP Host', validators=[DataRequired()])
    smtp_port = IntegerField('Port', validators=[DataRequired(), NumberRange(min=1, max=65535)])
    security = SelectField('Security', choices=[('none', 'None'), ('ssl', 'SSL'), ('tls', 'TLS'), ('auto', 'Auto')], default='auto')
    username = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    mailfrom = StringField('Mail From', validators=[DataRequired(), Email()])
    mailreceive = StringField('Mail To', validators=[DataRequired(), Email()])
    submit = SubmitField('Test SMTP')

@app.route('/', methods=['GET', 'POST'])
def smtp_tester():
    form = SMTPForm()
    message = ""
    api_key = os.getenv("OPENAI_API_KEY")

    if form.validate_on_submit():
        smtp_host = form.smtp_host.data
        smtp_port = form.smtp_port.data
        security = form.security.data
        username = form.username.data
        password = form.password.data
        mailfrom = form.mailfrom.data
        mailreceive = form.mailreceive.data

        try:
            validate_email(mailfrom, check_deliverability=False)
            validate_email(mailreceive, check_deliverability=False)
        except EmailNotValidError as e:
            message = f"Invalid email address: {str(e)}"
            return render_template('index.html', form=form, message=message, api_key=api_key)

        try:
            server = None
            if security == 'ssl':
                server = smtplib.SMTP_SSL(smtp_host, smtp_port)
                server.ehlo()
            else:
                server = smtplib.SMTP(smtp_host, smtp_port)
                server.ehlo()
                if security in ['tls', 'auto']:
                    try:
                        server.starttls()
                        server.ehlo()
                    except smtplib.SMTPException:
                        pass

            try:
                server.login(username, password)
            except smtplib.SMTPNotSupportedError:
                message = "Server does not support authentication, trying to send without login."
            except smtplib.SMTPException as e:
                message = f"Login failed: {str(e)}"
                server.quit()
                return render_template('index.html', form=form, message=message, api_key=api_key)

            email_message = "Subject: SMTP Test\n\nTest Email from SMTP Tester"
            server.sendmail(mailfrom, [mailreceive], email_message)
            server.quit()
            message = "Email sent successfully!"
        except smtplib.SMTPAuthenticationError:
            message = "Authentication failed: Check username and password."
        except smtplib.SMTPConnectError:
            message = "Failed to connect to the SMTP server. Check the host and port."
        except smtplib.SMTPRecipientsRefused:
            message = "Recipient address rejected. Verify recipient email."
        except smtplib.SMTPSenderRefused:
            message = "Sender address rejected. Check sender email."
        except smtplib.SMTPException as e:
            message = f"SMTP Error: {str(e)}"
        except Exception as e:
            message = f"Unexpected error: {str(e)}"

    return render_template('index.html', form=form, message=message, api_key=api_key)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)