# Generated by Django 4.1.2 on 2023-02-25 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_id_comment", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
                ("AppStore", models.CharField(max_length=255)),
                ("type_comment", models.CharField(max_length=255)),
                ("Category_comment", models.CharField(max_length=255)),
                ("value_comment", models.CharField(max_length=255)),
                ("subject_comment", models.CharField(max_length=255)),
                ("text_comment", models.TextField(max_length=2000)),
                ("date_comment", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Amount_With",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_id_App", models.CharField(max_length=255)),
                ("db_username_Publisher", models.CharField(max_length=255)),
                ("db_username_PaidBy", models.CharField(max_length=255)),
                ("db_AppName", models.CharField(max_length=255)),
                ("db_price", models.IntegerField()),
                ("db_type", models.CharField(max_length=255)),
                ("is_paid", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_id_Like", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
                ("AppStore", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Transuction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username_trans", models.CharField(max_length=255)),
                ("price", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_id_wishlist", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
                ("AppStore", models.CharField(max_length=255)),
                ("type_wish", models.CharField(max_length=255)),
                ("Category_wish", models.CharField(max_length=255)),
                ("value_wish", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Withdrawal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_username_Pub", models.CharField(max_length=255)),
                ("db_price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="db_Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_username", models.CharField(max_length=255)),
                ("db_email", models.EmailField(max_length=255)),
                (
                    "db_photo",
                    models.ImageField(
                        blank=True, max_length=255, upload_to="media/Profile/"
                    ),
                ),
                ("db_firstName", models.CharField(max_length=255)),
                ("db_lastName", models.CharField(max_length=255)),
                ("db_phoneNumber", models.CharField(max_length=255)),
                ("db_address", models.CharField(max_length=255)),
                ("db_date_DoB", models.DateField(blank=True)),
                ("db_exper", models.CharField(max_length=255)),
                ("db_hourly", models.CharField(max_length=255)),
                ("db_speak", models.CharField(max_length=255)),
                ("db_available", models.CharField(max_length=255)),
                ("db_bio", models.TextField(max_length=1000)),
                ("auth_token", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_account", models.BooleanField(default=False)),
                ("is_verified", models.BooleanField(default=False)),
                ("db_price", models.IntegerField()),
                ("SuperUser_is_verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="db_AppStore",
            fields=[
                ("db_id_App", models.AutoField(primary_key=True, serialize=False)),
                ("db_username", models.CharField(max_length=255)),
                ("db_AppName", models.CharField(max_length=255)),
                ("db_Category", models.CharField(max_length=255)),
                ("db_type", models.CharField(max_length=255)),
                ("db_link_type", models.CharField(max_length=255)),
                ("db_price", models.IntegerField()),
                ("db_Describe", models.TextField(max_length=1000)),
                (
                    "db_link",
                    models.FileField(max_length=500, upload_to="media/AppsFile/"),
                ),
                (
                    "db_photoApp",
                    models.ImageField(
                        blank=True, max_length=255, upload_to="media/AppsImage/"
                    ),
                ),
                (
                    "db_images_list1",
                    models.FileField(blank=True, upload_to="media/ImageList/"),
                ),
                (
                    "db_images_list2",
                    models.FileField(blank=True, upload_to="media/ImageList/"),
                ),
                (
                    "db_images_list3",
                    models.FileField(blank=True, upload_to="media/ImageList/"),
                ),
                (
                    "db_images_list4",
                    models.FileField(blank=True, upload_to="media/ImageList/"),
                ),
                ("db_create_Date", models.DateField(auto_now_add=True)),
                ("db_country", models.CharField(max_length=255)),
                (
                    "db_comment",
                    models.ManyToManyField(
                        related_name="db_comment", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "db_like",
                    models.ManyToManyField(
                        related_name="db_like", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "db_paid",
                    models.ManyToManyField(
                        related_name="db_paid", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "db_wishlist",
                    models.ManyToManyField(
                        related_name="db_wishlist", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]