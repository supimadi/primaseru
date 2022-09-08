from datetime import datetime
from datetime import timedelta

from django.test import TestCase

from users.models import CustomUser
from participant_profile.models import MajorStudent

from dashboard import models


class PrimaseruContactsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        models.PrimaseruContacts.objects.create(
            name="Siapa Ayo?", wa_number="082218533980",
            link_wa="https://whatsapp.me/029992"
        )

    def test_name_label(self):
        name = models.PrimaseruContacts.objects.get(pk=1)
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Nama Kontak")

    def test_name_max_length(self):
        name = models.PrimaseruContacts.objects.get(pk=1)
        field_label = name._meta.get_field("name").max_length
        self.assertEqual(field_label, 100)

    def test_wa_number_label(self):
        wa_number = models.PrimaseruContacts.objects.get(pk=1)
        field_label = wa_number._meta.get_field("wa_number").verbose_name
        self.assertEqual(field_label, "Nomor Whatsapp")

    def test_object_name(self):
        contact = models.PrimaseruContacts.objects.get(pk=1)
        expected_object_name = f'Contacts {contact.wa_number}'
        self.assertEqual(str(contact), expected_object_name)


class ParticipantCountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        models.ParticipantCount.objects.create(
            count="001", year=datetime.today().year
        )

    def test_count_label(self):
        count = models.ParticipantCount.objects.get(pk=1)
        field_label = count._meta.get_field("count").verbose_name
        self.assertEqual(field_label, "Hitungan")

    def test_count_max_length(self):
        count = models.ParticipantCount.objects.get(pk=1)
        field_label = count._meta.get_field("count").max_length
        self.assertEqual(field_label, 10)

    def test_year_label(self):
        count = models.ParticipantCount.objects.get(pk=1)
        field_label = count._meta.get_field("year").verbose_name
        self.assertEqual(field_label, "Tahun")

    def test_year_max_length(self):
        count = models.ParticipantCount.objects.get(pk=1)
        field_label = count._meta.get_field("year").max_length
        self.assertEqual(field_label, 4)

    def test_object_name(self):
        count = models.ParticipantCount.objects.get(pk=1)
        expected_object_name = f'{count.count}'
        self.assertEqual(str(count), expected_object_name)


class ParticipantLMSModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user("082218533980", "Lukman1_")
        models.ParticipantLMS.objects.create(
            participant=user, username="Lukman",
            password="lukman111", schedule=datetime.now(), time="08.00 - 10.00"
        )

    def test_username_label(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        field_label = lms_account._meta.get_field("username").verbose_name
        self.assertEqual(field_label, "Username")

    def test_username_length(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        max_length = lms_account._meta.get_field("username").max_length
        self.assertEqual(max_length, 120)

    def test_password_label(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        field_label = lms_account._meta.get_field("password").verbose_name
        self.assertEqual(field_label, "Password")

    def test_password_length(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        max_length = lms_account._meta.get_field("password").max_length
        self.assertEqual(max_length, 120)

    def test_schedule_label(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        field_label = lms_account._meta.get_field("schedule").verbose_name
        self.assertEqual(field_label, "Tanggal")

    def test_time_label(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        field_label = lms_account._meta.get_field("time").verbose_name
        self.assertEqual(field_label, "Pukul")

    def test_time_length(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        max_length = lms_account._meta.get_field("time").max_length
        self.assertEqual(max_length, 20)

    def test_object_name(self):
        lms_account = models.ParticipantLMS.objects.get(pk=1)
        obj_name = f'LMS {lms_account.participant.username}'
        self.assertEqual(str(lms_account), obj_name)


class ParticipantGraduationTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user("082218533980", "Lukman1_")
        MajorStudent.objects.create(
            participant=user, first_major="TKJ", second_major="MM",
            enter_smk="Orang Tua", charity="0", way_in="Jalur Reguler 1"
        )
        models.ParticipantGraduation.objects.create(
            participant=user, passed="L", chose_major="TKJ",
            date_announce=datetime.now(), clock_announce=datetime.now()
        )

    def test_passed_label(self):
        graduation = models.ParticipantGraduation.objects.get(pk=1)
        field_label = graduation._meta.get_field("passed").verbose_name
        self.assertEqual(field_label, "Lulus/Tidak Lulus")

    def test_chose_major_label(self):
        graduation = models.ParticipantGraduation.objects.get(pk=1)
        field_label = graduation._meta.get_field("chose_major").verbose_name
        self.assertEqual(field_label, "Diterima di Jurusan:")

    def test_date_announce_label(self):
        graduation = models.ParticipantGraduation.objects.get(pk=1)
        field_label = graduation._meta.get_field("date_announce").verbose_name
        self.assertEqual(field_label, "Tanggal Diumumkan")

    def test_clock_announce_label(self):
        graduation = models.ParticipantGraduation.objects.get(pk=1)
        field_label = graduation._meta.get_field("clock_announce").verbose_name
        self.assertEqual(field_label, "Jam Diumumkan")

    def test_object_name(self):
        graduation = models.ParticipantGraduation.objects.get(pk=1)
        obj_name = f'Graduation {graduation.participant}'
        self.assertEqual(str(graduation), obj_name)

class ParticipantModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user("082218533980", "Lukman1_")
        info = models.InfoSourcePPDB.objects.create(info_source="Website")

        participant = models.Participant.objects.create(
                account=user, full_name="Lukman Hakim", registration_number="222010",
                participant_phone_number=user.username,previous_school="SMP Telkom Bandung",
                parent_full_name="Father of Lukman", parent_phone_number="082218533983",
                homeroom_teacher_phone_number="082218533983", bk_teacher_phone_number="082218533988",
                )
        participant.info.add(info)

    # FIELD: full_name
    def test_full_name_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("full_name").verbose_name
        self.assertEqual(field_label, "Nama Lengkap")

    def test_full_name_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("full_name").max_length
        self.assertEqual(max_length, 100)

    # FIELD: registration_number
    def test_registration_number_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("registration_number").verbose_name
        self.assertEqual(field_label, "Nomor Pendaftaran")

    def test_registration_number_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("registration_number").max_length
        self.assertEqual(max_length, 20)

    def test_registration_number_is_index(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("registration_number").db_index
        self.assertTrue(field)

    def test_registration_number_is_unique(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("registration_number").unique
        self.assertTrue(field)

    def test_registration_number_is_nullabel(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("registration_number").null
        self.assertTrue(field)

    # FIELD: participant_phone_number
    def test_participant_phone_number_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("participant_phone_number").verbose_name
        self.assertEqual(field_label, "No. HP Calon Siswa")

    def test_participant_phone_number_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("participant_phone_number").max_length
        self.assertEqual(max_length, 15)

    def test_participant_phone_number_is_index(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("participant_phone_number").db_index
        self.assertTrue(field)

    def test_participant_phone_number_is_unique(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("participant_phone_number").unique
        self.assertTrue(field)

    # FIELD: previous_school
    def test_previous_school_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("previous_school").verbose_name
        self.assertEqual(field_label, "Nama Asal Sekolah")

    def test_previous_school_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("previous_school").max_length
        self.assertEqual(max_length, 100)

    def test_previous_school_is_index(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("previous_school").db_index
        self.assertTrue(field)

    def test_previous_school_is_nullabel(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("previous_school").null
        self.assertTrue(field)

    # FIELD: parent_phone_number
    def test_parent_phone_number_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("parent_phone_number").verbose_name
        self.assertEqual(field_label, "No. HP Orang Tua/Wali")

    def test_parent_phone_number_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("parent_phone_number").max_length
        self.assertEqual(max_length, 15)

    # FIELD: parent_full_name
    def test_parent_full_name_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("parent_full_name").verbose_name
        self.assertEqual(field_label, "Nama Lengkap Orang Tua")

    def test_parent_full_name_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("parent_full_name").max_length
        self.assertEqual(max_length, 100)

    def test_parent_full_name_is_nullabel(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("parent_full_name").null
        self.assertTrue(field)

    # FIELD: homeroom_teacher_phone_number
    def test_homeroom_teacher_phone_number_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("homeroom_teacher_phone_number").verbose_name
        self.assertEqual(field_label, "No. HP Wali Kelas")

    def test_homeroom_teacher_phone_number_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("homeroom_teacher_phone_number").max_length
        self.assertEqual(max_length, 15)

    def test_homeroom_teacher_phone_number_is_nullabel(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("homeroom_teacher_phone_number").null
        self.assertTrue(field)

    def test_homeroom_teacher_phone_number_is_blankable(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("homeroom_teacher_phone_number").blank
        self.assertTrue(field)

    # FIELD: bk_teacher_phone_number
    def test_bk_teacher_phone_number_label(self):
        participant = models.Participant.objects.get(pk=1)
        field_label = participant._meta.get_field("bk_teacher_phone_number").verbose_name
        self.assertEqual(field_label, "No. HP Guru BK")

    def test_bk_teacher_phone_number_length(self):
        participant = models.Participant.objects.get(pk=1)
        max_length = participant._meta.get_field("bk_teacher_phone_number").max_length
        self.assertEqual(max_length, 15)

    def test_bk_teacher_phone_number_is_nullabel(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("bk_teacher_phone_number").null
        self.assertTrue(field)

    def test_bk_teacher_phone_number_is_blankable(self):
        participant = models.Participant.objects.get(pk=1)
        field = participant._meta.get_field("bk_teacher_phone_number").blank
        self.assertTrue(field)

    def test_object_name(self):
        participant = models.Participant.objects.get(pk=1)
        expected_object_name = f'{participant.full_name}-{participant.registration_number}'
        self.assertEqual(str(participant), expected_object_name)
        
class RegisterScheduleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        models.RegisterSchedule.objects.create(
            name="Gelombang 1", start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30)
        )

    def test_name_label(self):
        name = models.RegisterSchedule.objects.get(pk=1)
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Nama Gelombang Pendaftaran")

    def test_name_max_length(self):
        name = models.RegisterSchedule.objects.get(pk=1)
        field_label = name._meta.get_field("name").max_length
        self.assertEqual(field_label, 120)

    def test_is_ongoing(self):
        data = models.RegisterSchedule.objects.get(pk=1)
        isongoing = data.is_ongoing
        self.assertTrue(isongoing)

    def test_is_past_date(self):
        data = models.RegisterSchedule.objects.get(pk=1)
        is_past_date = data.is_past_date
        self.assertFalse(is_past_date)

    def test_object_name(self):
        schedule = models.RegisterSchedule.objects.get(pk=1)
        obj_name = f'{schedule.name}'
        self.assertEqual(str(schedule), obj_name)

class PaymentBannerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        models.PaymentBanner.objects.create(
            sub_title="Silahkan Lakukan Pembayaran",
            rek_num="123-3332-4492-11",
            whom_rek="SMK Telkom Bandung",
            bank="Mandiri",
            money="3000000",
            wa_number="+621234234234",
            wa_link="https://wa.link/1039483910489",
        )

    def test_sub_title_label(self):
        sub_title = models.PaymentBanner.objects.get(pk=1)
        field_label = sub_title._meta.get_field("sub_title").verbose_name
        self.assertEqual(field_label, "Sub Judul")

    def test_sub_title_max_length(self):
        sub_title = models.PaymentBanner.objects.get(pk=1)
        field_label = sub_title._meta.get_field("sub_title").max_length
        self.assertEqual(field_label, 100)

    def test_sub_title_is_nullabel(self):
        sub_title = models.PaymentBanner.objects.get(pk=1)
        is_null = sub_title._meta.get_field("sub_title").null
        self.assertTrue(is_null)

    def test_rek_num_label(self):
        rek_num = models.PaymentBanner.objects.get(pk=1)
        field_label = rek_num._meta.get_field("rek_num").verbose_name
        self.assertEqual(field_label, "Nomor Rekening")

    def test_rek_num_max_length(self):
        rek_num = models.PaymentBanner.objects.get(pk=1)
        field_label = rek_num._meta.get_field("rek_num").max_length
        self.assertEqual(field_label, 50)

    def test_whom_rek_label(self):
        whom_rek = models.PaymentBanner.objects.get(pk=1)
        field_label = whom_rek._meta.get_field("whom_rek").verbose_name
        self.assertEqual(field_label, "Rekening Atas Nama")

    def test_whom_rek_max_length(self):
        whom_rek = models.PaymentBanner.objects.get(pk=1)
        field_label = whom_rek._meta.get_field("whom_rek").max_length
        self.assertEqual(field_label, 100)

    def test_bank_label(self):
        bank = models.PaymentBanner.objects.get(pk=1)
        field_label = bank._meta.get_field("bank").verbose_name
        self.assertEqual(field_label, "Bank")

    def test_bank_max_length(self):
        bank = models.PaymentBanner.objects.get(pk=1)
        field_label = bank._meta.get_field("bank").max_length
        self.assertEqual(field_label, 100)

    def test_money_label(self):
        money = models.PaymentBanner.objects.get(pk=1)
        field_label = money._meta.get_field("money").verbose_name
        self.assertEqual(field_label, "Nominal Pembayaran")

    def test_money_max_length(self):
        money = models.PaymentBanner.objects.get(pk=1)
        field_label = money._meta.get_field("money").max_length
        self.assertEqual(field_label, 7)

    def test_wa_number_label(self):
        wa_number = models.PaymentBanner.objects.get(pk=1)
        field_label = wa_number._meta.get_field("wa_number").verbose_name
        self.assertEqual(field_label, "Nomor Whatsapp")

    def test_wa_number_max_length(self):
        wa_number = models.PaymentBanner.objects.get(pk=1)
        field_label = wa_number._meta.get_field("wa_number").max_length
        self.assertEqual(field_label, 20)

    def test_wa_link_label(self):
        wa_link = models.PaymentBanner.objects.get(pk=1)
        field_label = wa_link._meta.get_field("wa_link").verbose_name
        self.assertEqual(field_label, "Link Whatsapp")

    def test_wa_link_max_length(self):
        wa_link = models.PaymentBanner.objects.get(pk=1)
        field_label = wa_link._meta.get_field("wa_link").max_length
        self.assertEqual(field_label, 100)

    def test_object_name(self):
        banner = models.PaymentBanner.objects.get(pk=1)
        obj_name = f'{banner.wa_number}'
        self.assertEqual(str(banner), obj_name)


