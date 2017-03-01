from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.messages import success
from .forms import ContactForm


class EmailMe(View):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent = bound_form.send_mail()
            if mail_sent:
                # shortcut for add_message
                success(request, 'Thanks for sending me an email. I will respond quickly as I can.')
                return render(request, self.template_name, {'form': self.form_class()})
        return render(request, self.template_name, {'form': bound_form})
