# Generated by Django 4.0.4 on 2022-04-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_course_section_alter_course_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comments',
            field=models.ManyToManyField(blank=True, to='courses.comment'),
        ),
    ]