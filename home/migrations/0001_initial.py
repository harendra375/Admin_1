# Generated by Django 5.0.4 on 2024-04-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserAdminTable",
            fields=[
                ("USER_ID", models.AutoField(primary_key=True, serialize=False)),
                ("USER_NAME", models.CharField(max_length=30)),
                ("MOBILE_NUMBER", models.CharField(max_length=15)),
                ("PASSWORD", models.CharField(max_length=200)),
                ("IS_KYC", models.BooleanField(default=False)),
                ("IS_BLOCKED", models.BooleanField(default=False)),
                ("CREATE_DATE", models.DateTimeField(auto_now_add=True)),
                ("BALANCE", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "USER_ADMIN",
            },
        ),
    ]
