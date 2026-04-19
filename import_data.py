import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Beverage

with open('starbucks.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            fat = row.get(' Total Fat (g)', '0').strip()
            fat = float(fat) if fat and fat.replace('.', '',
                                                    1).isdigit() else 0.0

            sugar = row.get(' Sugars (g)', '0').strip()
            sugar = int(sugar) if sugar and sugar.isdigit() else 0

            caffeine = row.get('Caffeine (mg)', '0').strip()
            if caffeine.lower() == 'varies' or caffeine.lower() == 'v':
                caffeine = 0.0
            else:
                caffeine = float(caffeine) if caffeine and caffeine.replace(
                    '.', '', 1).isdigit() else 0.0

            Beverage.objects.create(
                category=row['Beverage_category'],
                name=row['Beverage'],
                preparation=row['Beverage_prep'],
                calories=int(row['Calories']),
                total_fat_g=fat,
                sugar_g=sugar,
                caffeine_mg=caffeine
            )
        except Exception:
            pass