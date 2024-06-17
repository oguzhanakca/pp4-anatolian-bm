from django.shortcuts import render, redirect
from .forms import BookingForm


# Create your views here.
def book(request):
    """
    Booking function
    """
    form = BookingForm(data=request.POST)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(
        request, 'booking/booking.html', {'form' : form}
    )

def booking_success(request):
    return render(request, 'booking/booking_success.html')