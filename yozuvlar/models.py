from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=100, verbose_name="Muallif ismi")
    bio = models.TextField(verbose_name="Tarjimai hol")
    tugilgan_sana = models.DateField(verbose_name="Tug'ilgan sana")

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"

    def __str__(self):
        return self.ism

class Yozuv(models.Model):
    sarlavha = models.CharField(max_length=200, verbose_name="Yozuv sarlavhasi")
    matn = models.TextField(verbose_name="Yozuv matni")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    kayfiyat_vaqti = models.TimeField(verbose_name="Kayfiyat vaqti")
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE, verbose_name="Muallifi")

    class Meta:
        ordering = ['-yaratilgan_vaqt'] 
        verbose_name = "Yozuv"
        verbose_name_plural = "Yozuvlar"

    def __str__(self):
        return self.sarlavha

