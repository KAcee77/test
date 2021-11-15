from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=256)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    middle_name = models.CharField('Отчество', max_length=256)
    photo = models.ImageField('Фото', upload_to='photo')
    position = models.CharField('Должность', max_length=256)
    salary = models.DecimalField('Оклад', max_digits=8, decimal_places=2)
    age = models.IntegerField('Возраст')
    department = models.ForeignKey(Department, verbose_name='Департамент', 
                                   on_delete=models.CASCADE, related_name='departament', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
