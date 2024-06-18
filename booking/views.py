from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def book(request):
    """
    If user logged in, shows the booking page.
    If not, redirects to login page.
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