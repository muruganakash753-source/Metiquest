from django.db import models

class Coordinator(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
    ]
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='coordinators/')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('Non-Technical', 'Non-Technical'),
    ]
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    rules = models.TextField()
    coordinator = models.ForeignKey(Coordinator, on_delete=models.SET_NULL, null=True, related_name='events')
    start_time = models.TimeField(help_text="Format: HH:MM:SS (e.g., 09:30:00)")
    end_time = models.TimeField(help_text="Format: HH:MM:SS (e.g., 15:00:00)")
    max_members = models.PositiveIntegerField(default=1, help_text="Max participants per team")

    def __str__(self):
        return self.name

class Gallery(models.Model):
    heading = models.CharField(max_length=100, help_text="E.g., 'Inauguration', 'Robo Wars'")
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return f"{self.heading} - {self.id}"

# NEW: A place to store your Google Form link
class SiteSetting(models.Model):
    registration_link = models.URLField(max_length=500, help_text="Paste your Google Form URL here")
    is_active = models.BooleanField(default=True, help_text="Check to make this the active link")

    def __str__(self):
        return "Symposium Registration Link"