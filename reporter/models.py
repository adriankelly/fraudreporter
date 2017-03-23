from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Case(models.Model):
    """
    Model representing a case containing reports.
    """
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


    CASE_STATUS = (
      ('u', 'Unresolved'),
      ('r', 'Resolved'),
    )

    status = models.CharField(max_length=1, choices=CASE_STATUS, blank=True, default='u', help_text='Case status')

    class Meta:
        ordering = ["published_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular case instance.
        """
        return reverse('case-detail', args=[str(self.id)])




class Report(models.Model):
    """
    Model representing a fraud report.
    """
    case = models.ForeignKey('Case', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    details = models.TextField(max_length=1000, help_text="Provide a description of the circumstances surrounding the fraud event. Please be as specific as possible.")

    class Meta:
        ordering = ["published_date"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.subject
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return reverse('report-detail', args=[str(self.id)])




class Author(models.Model):
    """
    Model representing an auhtor.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
