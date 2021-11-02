from django.db import models
LEVEL_CHOICES = (
     ('UYARI', 'UYARI'),
     ('HATA', 'HATA'),
     ('YENİ', 'YENİ'),
     ('BİLGİ', 'BİLGİ'),
)
class Announcement(models.Model):
    """
    Model to hold global announcements
    """
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7,
                choices=LEVEL_CHOICES, default=LEVEL_CHOICES[0][0])
                
    def __str__(self):
        return str(self.level) + " " + str(self.body)

    def __unicode__(self):
        return self.body[:50]