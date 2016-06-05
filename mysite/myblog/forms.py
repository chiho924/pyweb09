from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        # send email using the self.cleaned_data dictionary
        pass
