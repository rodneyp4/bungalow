import os
import csv
import argparse

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from bungalow.listings.models import Listing

class Command(BaseCommand):
    args = 'data.csv'
    help = 'Import csv into database.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        csvfile = options['csv_file']

        model_fields = Listing._meta.fields
        fields_name = []
        reader = csv.reader (csvfile, delimiter=',')
        fields_name = next(reader)
        for i, _ in enumerate(fields_name):
            fields_name[i] = fields_name[i].lower ()

        for row in reader:
            try:
                obj = Listing()
                for i, field in enumerate(row):
                    # FloatField doesn't handle serializing empty string too well, convert to 0 instead
                    # model_fields has one more `id` field than the csv fields, so i+1 here 
                    if field == '' and isinstance(model_fields[i+1], models.FloatField):
                        field = 0
                    setattr(obj, fields_name[i], field)
                obj.save ()
            except Exception as e:
                raise CommandError(e)
