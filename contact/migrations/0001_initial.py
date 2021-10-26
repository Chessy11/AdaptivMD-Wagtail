# Generated by Django 3.2.8 on 2021-10-22 12:52

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('left_block_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name="Contact's Title")),
                ('left_block_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name="Contact's Text")),
                ('office_address', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Office Address')),
                ('factory_address', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Factory Address')),
                ('email_address', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Email Address')),
                ('phone_number_c', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Phone Number')),
                ('form_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Form Title')),
            ],
            options={
                'verbose_name': 'Contact Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]