from django.forms import widgets

class FilePickerURLWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        all_widgets = (
                widgets.TextInput(attrs={'class': 'filepicker_url'}),
                widgets.HiddenInput(attrs={'class': 'filepicker_name'}),
                widgets.HiddenInput(attrs={'class': 'filepicker_key'}),
        )
        super(FilePickerURLWidget, self).__init__(all_widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(':::')[0:3]
        return ['','','']

    class Media:
        js = ('path/to/filepickerwidget.js',
                '//api.filepicker.io/v0/filepicker.js',
                )
