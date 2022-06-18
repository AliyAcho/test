from django.core.management.base import BaseCommand, CommandError
from core.upDB import *
import time


class Command(BaseCommand):


    def handle(self, *args, **options):
        while True:
            try:
                update_data()
                self.stdout.write(self.style.SUCCESS('Good'))
                time.sleep(60)
            except:
                self.stdout.write(self.style.SUCCESS('Bad'))
                time.sleep(60)
                