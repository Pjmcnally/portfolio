from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as send


class ContactForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': "Name"}))
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': "Email *"}))
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': "Message *"}))

    def send_mail(self):
        name = self.cleaned_data.get('name')
        from_email = self.cleaned_data.get('email')
        text = self.cleaned_data.get('text')
        body = 'Message From: {} at {}\n\n{}\n'.format(
            name, from_email, text)
        subject = "Inquiry from contact me"
        try:
            # shortcut for send mail
            send(
                subject,
                body,
                from_email,
                ['patrick@pjmcnally.net'],
                fail_silently=False,
            )
        except BadHeaderError:
            self.add_error(
                None,
                ValidationError(
                    'Could Not Send Email.\n'
                    'Extra Headers not allowed '
                    'in email body.',
                    code='badheader'))
            return False
        else:
            return True
