INFO
======
A custom field and widget to store filepicker.io urls in a Django project.

Usage
======
    In models.py just add the field:

    filepicker_url = FilePickerURLModelField()

    When retreiving the data:

    URL = filepicker_url.0

    Name = filepicker_url.1

    Key = filepicker_url.2

TODO
======
    Use named properties instead of indices
