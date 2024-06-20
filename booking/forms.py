from datetime import datetime
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Book a Table form
    """
    class Meta:
        model = Booking
        fields = ['requested_date','requested_time','guests','message','phone']
        widgets =  {
            'requested_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': datetime.now().date()}),
            'requested_time': forms.Select(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'How many guests will be coming?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional Information (Optional)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Phone Number (Optional)'})
        }



    