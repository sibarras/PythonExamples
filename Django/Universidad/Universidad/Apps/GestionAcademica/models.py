from django.db import models

# Create your models here.

class Alumno(models.Model):
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    dni = models.CharField(max_length=8)
    fechaNacimiento = models.DateField()
    sexos = (('M', 'Masculino'), ('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')

    def nombreCompleto(self):
        return "{} {}, {}".format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        return self.nombreCompleto()

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.nombre, self.creditos)

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return '{} => {}'.format(self.alumno, self.curso.nombre)

    