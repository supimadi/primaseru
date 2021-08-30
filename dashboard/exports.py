from .models import Participant
import io

import xlsxwriter

workbook = xlsxwriter.Workbook('Expenses01.xlsx')

ws1 = workbook.add_worksheet('Data Peserta')
ws2 = workbook.add_worksheet('Profile Peserta')
ws3 = workbook.add_worksheet('Profile Ayah')
ws4 = workbook.add_worksheet('Profile Ibu')
ws5 = workbook.add_worksheet('Profile Wali')

participant = Participant.objects.all()

participant_header = []
for f in participant.first()._meta.fields:
    participant_header.append(f.verbose_name)

col = 0
for h in participant_header:
    ws1.write(0, col, h)
    col += 1


# for row in ws1.iter_rows(min_row=1, max_col=len(participant_header), max_row=1):
#     for index,cell in enumerate(row):
#         cell.value = participant_header[index]
