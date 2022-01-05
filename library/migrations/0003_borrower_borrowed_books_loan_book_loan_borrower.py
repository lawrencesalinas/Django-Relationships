# Generated by Django 4.0.1 on 2022-01-05 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='borrowed_books',
            field=models.ManyToManyField(through='library.Loan', to='library.Book'),
        ),
        migrations.AddField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='borrower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.borrower'),
            preserve_default=False,
        ),
    ]