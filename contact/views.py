from django.shortcuts import render, redirect
from contact.models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        name = request.POST['name'],
        email = request.POST['email'],
        topic = request.POST['topic'],
        message = request.POST['message']

        contact = Contact(name=name, email=email, topic=topic, message=message)

        contact.save()

        send_mail(
            subject='New Contact Message',
            message='A contact message has been sent to you. Sign into the Admin Panel to see it ',
            from_email='emmandukwe26@gmail.com',
            recipient_list=['ellamoves01@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been successfully sent. We will get back to you soon.')
        return redirect(to='all:index')

    return render(request, 'contact/contact.html')