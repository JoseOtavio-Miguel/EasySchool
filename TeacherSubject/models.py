from django.db import models

# Create your models here.
class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    school_year = models.IntegerField()

    class Meta:
        unique_together = (
            "teacher",
            "subject",
            "class_room",
            "school_year"
        )
