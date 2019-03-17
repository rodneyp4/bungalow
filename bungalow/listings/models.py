from django.db import models
from datetime import datetime

class CustomizedDateField(models.DateField):
    def to_python(self, value):
        if value is '':
            return None
        if value is None:
            return value
        # It seems django DateField model only supports one date format
        # Manually convert here
        value = datetime.strptime(value, '%m/%d/%Y').strftime('%Y-%m-%d')
        return super(CustomizedDateField, self).to_python(value)

class Listing(models.Model):
  # Constants
  SQFT = 'SqFt'
  AREA_UNIT_CHOICES = (
      (SQFT, 'Square Footage'),
  )
  SINGLEFAMILY = 'SingleFamily'
  VACANTRESIDENTIALLAND = 'VacantResidentialLand'
  MULTIFAMILY2TO4 = 'MultiFamily2To4'
  DUPLEX = 'Duplex'
  CONDOMINIUM = 'Condominium'
  APARTMENT = 'Apartment'
  MISCELLANEOUS = 'Miscellaneous'
  HOME_TYPE_CHOICES = (
    (SINGLEFAMILY ,'SingleFamily'),
    (VACANTRESIDENTIALLAND ,'VacantResidentialLand'),
    (MULTIFAMILY2TO4 ,'MultiFamily2To4'),
    (DUPLEX ,'Duplex'),
    (CONDOMINIUM ,'Condominium'),
    (APARTMENT ,'Apartment'),
    (MISCELLANEOUS ,'Miscellaneous'),
  )
  # Table Columns
  area_unit = models.CharField(
    max_length = 4,
    choices=AREA_UNIT_CHOICES,
    default=SQFT,
  )
  bathrooms = models.FloatField(null=True)
  bedrooms = models.FloatField(null=True)
  home_size = models.FloatField(null=True)
  home_type = models.CharField(
    max_length=30,
    choices=HOME_TYPE_CHOICES,
  )
  last_sold_date = CustomizedDateField(blank=True, null=True)
  last_sold_price = models.FloatField(null=True)
  link = models.URLField(blank=True)
  price = models.CharField(blank=True, max_length=30)
  property_size = models.FloatField(null=True)
  rent_price = models.FloatField(null=True)
  rentzestimate_amount = models.FloatField(null=True)
  rentzestimate_last_updated = CustomizedDateField(blank=True, null=True)
  tax_value = models.FloatField(null=True)
  tax_year = models.FloatField(null=True)
  year_built = models.FloatField(null=True)
  zestimate_amount = models.FloatField(null=True)
  zestimate_last_updated = CustomizedDateField(blank=True, null=True)
  zillow_id = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30)
  zipcode = models.CharField(max_length=30)
