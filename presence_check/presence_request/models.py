from django.db import models
import qrcode
import qrcode.image.svg
import io
from presence_check import settings
from django.core.mail import EmailMessage, send_mail


class PresenceRequest(models.Model):
    email = models.EmailField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.email}'

    def get_absolute_url(self):
        return f'{settings.BASE_DOMAIN}/admin/presence_request/presencerequest/{self.pk}/change/'

    def generate_qrcode(self):
        img = qrcode.make(self.email)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

    def approve(self):
        if self.is_approved == None:
            self.is_approved = True
            self.save()
            message = f'Your presence request created at {self.created_at} is approved.'
            qrcode = self.generate_qrcode()
            mail = EmailMessage("Request Approved!!",
                                message,
                                settings.DEFAULT_FROM_EMAIL,
                                [self.email])
            mail.attach("QRcode", qrcode)
            mail.send()

    def refuse(self):
        if self.is_approved == None:
            self.is_approved = False
            self.save()
            message = f'Your presence request created at {self.created_at} is refused.'
            send_mail("Request Refused!!",
                      message,
                      settings.DEFAULT_FROM_EMAIL,
                      [self.email])
