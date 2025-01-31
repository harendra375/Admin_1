# Generated by Django 5.0.4 on 2024-04-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentTable",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("MOBILE_NUMBER", models.CharField(max_length=15)),
                ("IS_DEPOSIT", models.BooleanField(default=False)),
                ("IS_WITHDRAW", models.BooleanField(default=False)),
                ("APPROVE_PAYMENT", models.BooleanField(default=False)),
                ("CREATE_DATE", models.DateTimeField(auto_now_add=True)),
                ("AMOUNT", models.IntegerField()),
            ],
            options={
                "db_table": "PAYMENT",
            },
        ),
    ]
