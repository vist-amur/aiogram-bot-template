import smtplib
from data import config


async def sendmail(message, state):
    sender = config.MAIL_ADMIN
    password = config.PASS_MAIL
    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        # server.starttls()

        server.login(sender, password)
        server.sendmail(sender, sender, f'Subject: Bot telegram\n{message}')
        server.quit()

        return "Successfully!"
    except Exception as _ex:
        await state.finish()
        await state.reset_state()
        print(_ex)
        return f'{_ex}'
