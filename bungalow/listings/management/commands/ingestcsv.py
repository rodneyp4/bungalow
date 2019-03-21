import csv
import argparse

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from bungalow.listings.models import Listing

class Command(BaseCommand):
    help = 'Import csv into database.'

    def add_arguments(self, parser):
        # the type argument will help making sure the file is readable
        parser.add_argument('csv_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        csvfile = options['csv_file']
        # pass the file object to csv module
        reader = csv.reader(csvfile, delimiter=',')
        # The first row contains the header, i.e. field names
        fields_name = next(reader)

        rows_saved = 0
        for row in reader:
            try:
                # Note: The input from csv contains empty strings for empty columns 
                # We need to convert those to None so our Django model can handle
                row = [ None if x == '' else x for x in row ]
                # zip field name and actual value together to form key,value pairs
                content = dict(zip(fields_name, row))
                Listing.objects.create(**content)
                rows_saved += 1
            except Exception as e:
                raise CommandError(e)
        print('Succesfully saved %d rows!' % rows_saved)
