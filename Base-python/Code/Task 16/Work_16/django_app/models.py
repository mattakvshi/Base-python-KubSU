
from django.db import models


class Users(models.Model):
    type = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=32)

    def __str__(self):
        return (f"{self.id} {self.type} {self.surname} {self.name} {self.patronymic} {self.email} "
                f"{self.password}")


class Subjects(models.Model):
    name_subject = models.CharField(max_length=30)
    id_creator = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.name_subject} {self.id_creator}"


class Teachers(models.Model):
    surname_teacher = models.CharField(max_length=30)
    name_teacher = models.CharField(max_length=30)
    patronymic_teacher = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="teachers")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_teacher} {self.name_teacher} {self.patronymic_teacher} "
                f"{self.subject_id} {self.id_creator}")


class Listeners(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="listeners")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.subject_id} {self.id_creator}")


class AcademicRecords(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="academic_records")
    listener_id = models.IntegerField()
    mark = models.IntegerField()
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.subject_id} {self.listener_id} {self.mark} {self.id_creator}")


class Group1(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group1")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.listener_id} {self.id_creator}")


class Group2(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group2")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.listener_id} {self.id_creator}")


class Group3(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group3")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.listener_id} {self.id_creator}")


class Group4(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group4")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.listener_id} {self.id_creator}")


class Group5(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group5")
    id_creator = models.IntegerField()

    def __str__(self):
        return (f"{self.id} {self.surname_listener} {self.name_listener} {self.patronymic_listener} "
                f"{self.listener_id} {self.id_creator}")
