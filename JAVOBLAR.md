# Imtihon Savollariga Javoblar

## 2-topshiriq: Virtual muhit nima?
Virtual muhit (venv) — bu loyiha uchun alohida, mustaqil quticha. U biz o'rnatgan Django va boshqa dasturlarni kompyuterdagi boshqa loyihalar bilan aralashib ketmasligini ta'minlaydi. Har bir loyiha o'z qutichasi ichida tinchgina ishlaydi.

## 4-topshiriq: makemigrations va migrate farqi nima?
- `makemigrations`: Modellarda qilingan o'zgarishlarni tekshirib, bazaga nima qilish kerakligi haqida "reja" (fayl) tayyorlaydi.
- `migrate`: O'sha tayyor bo'lgan rejani ishga tushirib, bazada haqiqiy jadvallarni yaratadi.
- Har doim birinchi bo'lib `makemigrations` ishlatiladi, chunki avval reja tuzish, keyin uni bajarish kerak.

## 8-topshiriq: ForeignKey dagi models.CASCADE nima qiladi?
Bu zanjirli o'chirish degani. Agar biz bazadan biror Muallifni o'chirib tashlasak, unga tegishli bo'lgan barcha Yozuvlar ham bazadan avtomatik ravishda birga o'chib ketadi.
