from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


# Create your views here.
def book(request):
    """
    Booking function
    """
    form = BookingForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(
        request, 'booking/booking.html', {'form' : form},
    )

def booking_success(request):
    return render(request, 'booking/booking_success.html'),