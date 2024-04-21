
from django.shortcuts import render
from core.models import Setting
from core.forms import SubscriberForm
  

        
        
def my_setting(request):
    setting_data = Setting.objects.get(id=4)
    subscriber_form = SubscriberForm()  # Create a form instance
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Clear the form after successful submission
            subscriber_form = SubscriberForm()
    return{
        'setting_data':setting_data,
        'subscriber_form': subscriber_form
    } 