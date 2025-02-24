# Generated by Django 4.2.6 on 2023-10-18 04:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import review_pub.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='code')),
                ('name_language', models.CharField(max_length=30, verbose_name='natural name')),
                ('name_english', models.CharField(max_length=30, verbose_name='english name')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('date_submitted', models.DateField(auto_created=True, editable=False, verbose_name='submission date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(unique=True, verbose_name='paper title')),
                ('filename', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to=review_pub.models.random_path)),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='keywords')),
                ('date_approved', models.DateField(editable=False, null=True, verbose_name='approved date')),
                ('status', models.CharField(choices=[('SUBMITTED', 'Submitted'), ('REVIEW_PENDING', 'Awaiting reviews'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='SUBMITTED', max_length=20, verbose_name='paper status')),
                ('authors', models.ManyToManyField(related_name='papers', to=settings.AUTH_USER_MODEL, verbose_name='authors')),
                ('domains', models.ManyToManyField(related_name='papers', to='review_pub.domain', verbose_name='domain')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papers', to='review_pub.language', verbose_name='language')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cancelled_reason', models.CharField(editable=False, max_length=100, null=True, verbose_name='cancelled reason')),
                ('status', models.CharField(choices=[('REQUESTED', 'Requested'), ('IN_PROGRESS', 'In progress'), ('CANCELLED', 'Cancelled'), ('DONE', 'Done')], default='REQUESTED', max_length=20, verbose_name='review status')),
                ('result', models.CharField(choices=[('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], max_length=20, null=True, verbose_name='review result')),
                ('feedback', models.TextField(verbose_name="Reviewer's feedback")),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review_pub.paper', verbose_name='paper')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='domains',
            field=models.ManyToManyField(related_name='users', to='review_pub.domain', verbose_name='domains'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(related_name='users', to='review_pub.language', verbose_name='spoken languages'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
