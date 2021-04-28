# Generated by Django 3.1.1 on 2021-04-28 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_polls_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Place_ID_Yelp',
            fields=[
                ('restaraunt_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('category', models.CharField(max_length=256)),
                ('phone_num', models.CharField(max_length=256)),
                ('rating', models.IntegerField()),
                ('image_url', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('zip_code', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Place_ID_Zomato',
            fields=[
                ('restaraunt_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256, null=True)),
                ('cusine', models.CharField(max_length=256)),
                ('menu_url', models.CharField(max_length=256)),
                ('average_cost_for_two', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.IntegerField()),
                ('cusine', models.CharField(max_length=256, null=True)),
                ('title', models.CharField(max_length=256)),
                ('readyInMinutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=256)),
                ('user_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User_search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_query', models.CharField(max_length=256)),
                ('user_selected_food_place', models.CharField(max_length=256)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user_detail')),
            ],
        ),
    ]
