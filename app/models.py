from django.db import models


class Animal(models.Model):
    GENDER_TYPES = (
        ('Male', 'Мальчик'),
        ('Female', 'Девочка')
    )
    ANIMAL_SPECIES = (
        ('Dog', 'Собака'),
        ('Cat', 'Кошка'),
    )
    name = models.CharField("Имя", max_length=20)
    species = models.CharField(max_length=20, choices=ANIMAL_SPECIES)
    gender = models.CharField("Пол", max_length=10, choices=GENDER_TYPES)
    short_text = models.CharField("Короткое описание", max_length=255)
    description = models.TextField("Описание", )
    caretaker = models.ForeignKey('Volunteer', null=True, blank=True, on_delete=models.SET_NULL)
    main_image = models.ImageField("Главное изображение", upload_to='animal_images', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.gender} - {self.species}'


class Volunteer(models.Model):
    name = models.CharField("Имя волонтера", max_length=100)
    phone_number = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.name


class AnimalImage(models.Model):
    image = models.ImageField("Изображение животного", upload_to='animal_images')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
