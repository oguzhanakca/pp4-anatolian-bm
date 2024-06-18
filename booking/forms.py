from datetime import datetime
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    # Custom field for phone number
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Phone Number (Optional)'}))

    class Meta:
        model = Booking
        fields = ['requested_date','requested_time','guests','message']
        widgets =  {
            'requested_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': datetime.now().date()}),
            'requested_time': forms.Select(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'How many guests will be coming?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional Information (Optional)'})
        }


    