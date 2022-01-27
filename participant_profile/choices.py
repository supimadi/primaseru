#!/usr/bin/env python3

SEX = [
    ('P', 'Perempuan'),
    ('L', 'Laki - Laki'),
]

SPESIAL_NEED_CHOICES = [
    ('Y', 'Ya, Berkebutuhan Khusus'),
    ('N', 'Tidak Berkebutuhan Khusus'),
]

COLOR_BLIND = [
    ('N', 'Tidak'),
    ('YP', 'Ya, Buta Warna Parsial (Sebagian)'),
    ('YT', 'Ya, Buta Warna Total'),
]

RAPORT_SEMESTER = [
    ('SEM_1', 'Semester 1'),
    ('SEM_2', 'Semester 2'),
    ('SEM_3', 'Semester 3'),
    ('SEM_4', 'Semester 4'),
    ('SEM_5', 'Semester 5'),
]

RAPORT_PART = [
    ('P_1', 'Lembar 1'),
    ('P_2', 'Lembar 2'),
    ('P_3', 'Lembar 3'),
]

RELIGION = [
    ('ISL', 'Islam'),
    ('PRS', 'Protestan'),
    ('KTH', 'Katolik'),
    ('HDN', 'Hindu'),
    ('BDH', 'Budha'),
    ('KHC', 'Konghucu'),
]

EDUCATION_LEVEL = [
    ('SD', 'SD'), ('SLTP', 'SLTP'),
    ('SLTA', 'SLTA'), ('D2', 'D2'),
    ('D3', 'D3'), ('D4', 'D4'),
    ('S1', 'S1'), ('S2', 'S2'),
    ('S3', 'S3'),
]

MAJOR = [
    ('TKJ', 'Teknik Komputer dan Jaringan'),
    ('TJAT', 'Teknik Jaringan Akses Telekomunikasi'),
    ('MM', 'Multimedia'),
]

BLOOD_TYPE = [
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O'),
    ('0', 'Tidak Tahu'),
]

INFORMATION_PRIMASERU = [
    ('WEB', 'Website'),
    ('IG', 'Instagram'),
    ('FB', 'Facebook'),
    ('TW', 'Twitter'),
    ('TK', 'Tiktok'),
    ('SDR', 'Sodara/Keluarga'),
    ('ALK', 'Alumni SMK Telkom'),
    ('ALS', 'Alumni SMP'),
    ('GMP', 'Guru SMP'),
    ('GRK', 'Guru SMK'),
    ('BRS', 'Brosur'),
    ('RDO', 'Radio'),
    ('LLY', 'Lainnya'),
]

ENTER_SMK_CHOICES = [
    ('Orang Tua', 'Orang Tua'),
    ('Sendiri', 'Sendiri'),
    ('Orang Tua dan Sendiri', 'Orang Tua dan Sendiri'),
]

CHARITY_AMOUNT = [
    ('0', 'Rp. 0'),
    ('Rp. 500.000,-', 'Rp. 500.000,-'),
    ('Rp. 1.000.000,-', 'Rp. 1.000.000,-'),
    ('Rp. 1.500.000,-', 'Rp. 1.500.000,-'),
    ('Rp. 2.000.000,-', 'Rp. 2.000.000,-'),
    ('Rp. 2.500.000,-', 'Rp. 2.500.000,-'),
    ('Rp. 3.000.000,-', 'Rp. 3.000.000,-'),
]

JALUR_MASUK = [
    ('Jalur Prestasi', 'Jalur Prestasi'),
    ('Jalur Reguler 1', 'Jalur Reguler 1'),
    ('Jalur Reguler 2', 'Jalur Reguler 2'),
    ('Jalur Reguler 3', 'Jalur Reguler 3'),
]
