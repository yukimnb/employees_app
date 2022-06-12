import csv
import datetime
import os

from django.conf import settings_dev
from django.core.management.base import BaseCommand

from ...models import Employee


class Command(BaseCommand):
    help = "Backup Employees data"

    def handle(self, *args, **options):
        date = datetime.date.today().strftime("%Y%m%d")
        # 保存ファイルの相対パス
        file_path = settings_dev.BACKUP_PATH + "employees_" + date + ".csv"
        os.makedirs(settings_dev.BACKUP_PATH, exist_ok=True)

        with open(file_path, "w") as file:
            writer = csv.writer(file)
            header = [field.name for field in Employee._meta.fields]
            writer.writerow(header)

            employees = Employee.objects.all()

            for employee in employees:
                writer.writerow([
                    employee.id,
                    employee.name,
                    employee.sub_name,
                    employee.post,
                    employee.gender,
                    str(employee.age),
                    str(employee.birthday),
                    employee.address,
                    employee.phone,
                    employee.assignment,
                    employee.team,
                    employee.license,
                    str(employee.experience),
                    str(employee.length_of_service),
                    str(employee.joined_date),
                    str(employee.retired_date),
                    employee.evaluation,
                    str(employee.photo),
                    str(employee.created_at),
                    str(employee.updated_at),
                ])

        files = os.listdir(settings_dev.BACKUP_PATH)
        if len(files) >= settings_dev.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings_dev.BACKUP_PATH + files[0])
