from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import BookingForm
from .models import Booking



# Create your views here.
@login_required
def book(request):
    """
    If user logged in, shows the booking page.
    If not, redirects to login page.
    """

    #Reservation List
    reservation_list = Booking.objects.filter(user=request.user).order_by("-requested_date")
    paginator = Paginator(reservation_list, 5)  # Show 5 reservations per page.
    page_number = request.GET.get("page")
    paginated_list = paginator.get_page(page_number)

    # Form data
    form = BookingForm(data=request.POST)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(
        request, 'booking/booking.html', {'form' : form, 'paginated_list' : paginated_list}
    )

def booking_success(request):
    return render(request, 'booking/booking_success.html')