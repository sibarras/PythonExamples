from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = '{}. (Duracion: {} año(s)).'.format(self.nombre, self.duracion)
        return txt
    

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [('F','Femenino'),('M','Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=False)

    def nombreCompleto(self) -> str:
        txt = '{} {}, {}'.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
        return txt
    
    def __str__(self):
        txt = '{} {}, {}'.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
        return txt

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = '{}. (Codigo: {} Docente: {}.)'.format(self.nombre, self.codigo, self.docente)
        return txt

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = 'Id:{}. (Estudiante: {} Curso: {} Fecha: {} )'.format(self.id, self.estudiante, self.curso, self.fechaMatricula)
        return txt