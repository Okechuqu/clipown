from django import forms


class YoutubeVideoForm(forms.Form):
    video_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter video URL', 'type': 'url', 'id': 'video-url'}))
    quality = forms.ChoiceField(label='', choices=[(
        'highest', 'Highest'), ('lowest', 'Lowest')], required=True, widget=forms.Select(attrs={'class': 'custom-select'}))
