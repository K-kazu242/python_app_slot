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
            name='SlotRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('amount', models.IntegerField(default=0, verbose_name='収支')),
                ('memo', models.CharField(blank=True, max_length=200, verbose_name='メモ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='ユーザー',
                )),
            ],
            options={
                'verbose_name': 'スロット記録',
                'verbose_name_plural': 'スロット記録',
                'ordering': ['-date', '-created_at'],
            },
        ),
    ]
