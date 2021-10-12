import random
import datetime
import smtplib
from email.mime.text import MIMEText


def color_red(text):
    """Returns red text (for output to the console)."""
    return "\033[31m {}" .format(text)

def color_green(text):
    """Returns green text (for output to the console)."""
    return "\033[32m {}" .format(text)

def get_date():
    """Returns today's date in the format DD.MM.YYYY."""
    date = datetime.datetime.now()
    return date.strftime("%d.%m.%Y")

def send_email(message, recipient, sender, password):
    """Sends an email.

    Log in to gmail using the variable "sender" as login 
    and variable "password" as password. Sends text from
    variable "message" to to the address stored in variable "recipient"

    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = f"0371 Копылов К.А. отчет ОФП {get_date()}"
        server.sendmail(sender, recipient, msg.as_string())

        return color_green("The message was sent succesfully!")
    except Exception as _ex:
        return color_red(f"{_ex}\nOops, something went wrong... Please, check your email or password")


def main():
    recipient = "example@example.com" #Change email
    sender = "example@gmail.com" #Change email
    password = "password" #Change password

    print(f"Отчет ОФП от {get_date()}")

    number_of_exercise_set = input("Введите номер комплекса упражнений: ")
    first_lesson_link = input("Вставьте ссылку на первое занятие: ")
    second_lesson_link = input("Вставьте ссылку на второе занятие: ")
    first_lesson_length = random.randint(45, 60)
    second_lesson_length = random.randint(45, 60)
    
    message = f"""
        Добрый день! Отправляю вам отчет по занятиям на этой неделе.
        «{first_lesson_link}», комплекс {number_of_exercise_set}, занятие №1, общая продолжительность занятия {first_lesson_length} мин, {get_date()}.
        «{second_lesson_link}», комплекс {number_of_exercise_set}, занятие №2, общая продолжительность занятия {second_lesson_length} мин, {get_date()}.

        Копылов Кирилл Андреевич, гр 0371
    """
    print(send_email(message=message, recipient=recipient, sender=sender, password=password))


if __name__ == "__main__":
    main()