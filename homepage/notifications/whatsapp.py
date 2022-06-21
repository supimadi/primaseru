from time import sleep
import requests

from django.conf import settings


def _reformat_phone_number(phone_number: str) -> str:
    if phone_number.startswith("+"):
        return phone_number.lstrip("+")

    return f"62{phone_number.lstrip('0')}"

def send_register_notif(parent_name: str, full_name: str, school: str, username_user: str, password_user: str, phone_number: list[str]):
    message_template = f"""
    Terima kasih Bapak/ Ibu {parent_name} sudah membuat akun *Penerimaan Peserta Didik Baru* (PRIMASERU) SMK Telkom Bandung T.A. 2022/ 2023, berikut data pendaftaran:

    Nama Lengkap : *{full_name}* 
    Asal Sekolah : *{school}*
    Username : *{username_user}*
    Password : *{password_user}*


    Tahap selanjutnya silahkan Bapak/ Ibu {parent_name} segera membayar uang pendaftaran sebesar Rp.300.000.- ke nomor rekening *Mandiri atas nama SMK Telkom Bandung dengan nomor rekening 131-00-0806150-1*

    Jika Bapak/ Ibu telah membayarkan uang pendaftarannya, silakan Bapak/ Ibu kirimkan buktinya ke nomor ini.

    Terima kasih,
    *SALAM PANITIA PRIMASERU SMK TELKOM BANDUNG*
    """

    data = {
        "api_key": settings.WA_API_KEY,
        "sender": "6281222758538",
        #  "number": _reformat_phone_number(form2.cleaned_data['parent_phone_number']),
        "message": message_template
    }

    timeout = 30.0
    for number in phone_number:
        data["number"] = _reformat_phone_number(number)

        # Give some delay to prefent blocking the phone number
        sleep(timeout)
        timeout += 30.0

        requests.post("https://wa.telkomschools.sch.id/send-message", data=data)
