from django.core.mail import send_mail


def mail_sender(to,subjectt,textt):
    
    to = [to]
    print("subject:",subjectt)
    print("text:",textt)
    html = "<h1 style='color:red'> this is a <strong>test</strong> email </h1>"

    send_mail(
        from_email="swathiaparna0@gmail.com",
        message=textt,
        subject=subjectt,
        recipient_list=to,
        html_message=html
    )
    return "Mail Send"