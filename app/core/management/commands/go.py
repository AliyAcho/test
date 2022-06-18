from django.core.management.base import BaseCommand, CommandError
from core.upDB import *
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            try:
                update_data()
                time.sleep(60)
            except:
                time.sleep(60)
