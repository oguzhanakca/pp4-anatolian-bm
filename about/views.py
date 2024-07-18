from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def about(request):
    """
    Display About Us page
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            body = f"Name: {name}\nEmail : {email}\nMessage: {message}"
            send_mail(
                subject=f"Contact Message from {name}",
                message=body,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            return redirect("about")
    else:
        form = ContactForm()

    return render(request,"about/about.html",{"form":form})