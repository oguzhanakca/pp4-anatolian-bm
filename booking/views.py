from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import BookingForm
from .models import Booking
from .utils import send_booking_success_email

@login_required
def book(request):
    """
    If user logged in, shows the booking page.
    If not, redirects to login page.
    """

    # Ordering
    order = request.GET.get('order', '-created_date')
    if order.startswith('-'):
        new_order_date = order[1:] if order == "-requested_date" else "requested_date"
        new_order_time = order[1:] if order == "-requested_time" else "requested_time"
        new_order_guests = order[1:] if order == "-guests" else "guests"
        new_order_status = order[1:] if order == "-status" else "status"
    else:
        new_order_date = '-' + order if order == 'requested_date' else 'requested_date'
        new_order_time = '-' + order if order == 'requested_time' else 'requested_time'
        new_order_guests = '-' + order if order == 'guests' else 'guests'
        new_order_status = '-' + order if order == 'status' else 'status'

    # User Role and Pagination
    user = request.user
    if user.is_staff:
        bookings = Booking.objects.all().order_by(order)
        paginator = Paginator(bookings, 10)  # Show 15 bookings per page.
    else:
        bookings = Booking.objects.filter(user=user).order_by(order)
        paginator = Paginator(bookings, 5)  # Show 5 bookings per page.

    page_number = request.GET.get("page")
    paginated_list = paginator.get_page(page_number)

    # Form data
    form = BookingForm(data=request.POST)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = user
        booking.save()
        send_booking_success_email(user, booking)
        return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(
        request, 
        'booking/booking.html', 
        {
            'form' : form, 
            'paginated_list' : paginated_list, 
            'user': user, 
            'current_order': order, 
            'new_order_date': new_order_date, 
            'new_order_time': new_order_time, 
            'new_order_guests': new_order_guests, 
            'new_order_status': new_order_status,
        }
    )

def booking_success(request):
    return render(request, 'booking/booking_success.html')