from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email_address = models.EmailField(unique=True, max_length=90)  # Email validation and unique constraint
    password = models.CharField(max_length=128)  # Supports hashed passwords
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    home_address = models.CharField(max_length=90, blank=True)  # Allow optional fields
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email_address})"


class Role(models.TextChoices):
    TEACHING_ASSISTANT = "TA", "TA"
    INSTRUCTOR = "INSTRUCTOR", "Instructor"
    ADMIN = "ADMIN", "Admin"


class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grader_status = models.BooleanField(default=True)
    skills = models.TextField(null=True, default="No skills listed")
    max_assignments = models.PositiveIntegerField(
        default=6,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - TA"


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_assignments = models.IntegerField(
        default=6,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Instructor"


class Administrator(User):  # Administrator inherits from User
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Administrator"


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - Administrator"


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - Administrator"


class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    num_of_sections = models.IntegerField()
    semester = models.CharField(
        max_length=10,
        choices=[
            ("Fall", "Fall"),
            ("Spring", "Spring"),
            ("Summer", "Summer"),
        ]
    )
    modality = models.CharField(
        max_length=50,
        choices=[
            ("Online", "Online"),
            ("In-person", "In-person"),
            ("Hybrid", "Hybrid"),
        ],
        default="In-person"
    )

    def __str__(self):
        return f"{self.course_id}: {self.name}"


class RoleToCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=Role,
    )

    def __str__(self):
        return f"{self.user} ({self.get_role_display()})- {self.course}"


    
    
    def edit_Course(self, **kwargs):
            # Validate and update basic fields
            if 'name' in kwargs:
                if not kwargs['name']:  # Check for empty values
                    raise ValueError("Course name cannot be empty.")
                self.name = kwargs['name']

            if 'num_of_sections' in kwargs:
                if kwargs['num_of_sections'] < 0:  # Check for negative values
                    raise ValueError("Number of sections cannot be negative.")
                self.num_of_sections = kwargs['num_of_sections']

            # Update other fields
            for field, value in kwargs.items():
                if hasattr(self, field) and field != 'instructors':  # Skip 'instructors'
                    setattr(self, field, value)

            # Handle instructor assignments if provided
            if 'instructors' in kwargs:
                instructor_list = kwargs['instructors']
                if not isinstance(instructor_list, list):
                    raise ValueError("Instructors should be a list of Instructor instances.")
                
                # Clear existing assignments
                InstructorToCourse.objects.filter(course=self).delete()
                
                # Add new assignments
                for instructor in instructor_list:
                    if isinstance(instructor, Instructor):
                        InstructorToCourse.objects.create(instructor=instructor, course=self)
                    else:
                        raise ValueError("Each instructor must be an instance of the Instructor model.")

            # Save the updated course instance
            self.save()

class Section(models.Model):
    section_id = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    location = models.CharField(max_length=30)
    meeting_time = models.TextField()

    def __str__(self):
        return f"Section {self.section_id} - {self.course}"


class Lab(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="labs")
    ta = models.ForeignKey("TA", on_delete=models.SET_NULL, null=True, related_name="assigned_labs")

    def __str__(self):
        return f"Lab: {self.section_id} - {self.course}"


class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="lectures")
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True, related_name="assigned_lectures")
    ta = models.ForeignKey("TA", on_delete=models.SET_NULL, null=True, related_name="grading_lectures")

    def __str__(self):
        return f"Lecture: {self.section_id} - {self.course}"


