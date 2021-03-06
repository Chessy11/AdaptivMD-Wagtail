# Generated by Django 3.2.8 on 2021-10-22 12:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Title')),
                ('page_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Text')),
                ('first_card_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='First Card Title')),
                ('first_card_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='First Card Text')),
                ('second_card_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Second Card Title')),
                ('second_card_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Second Card Text')),
                ('third_card_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Third Card Title')),
                ('third_card_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Third Card Text')),
                ('fourth_card_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fourth Card Title')),
                ('fourth_card_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fourth Card Text')),
                ('fifth_card_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fifth Card Title')),
                ('fifth_card_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fifth Card Text')),
                ('fifth_card_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Fifth Card Photo')),
                ('first_card_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='First Card Photo')),
                ('fourth_card_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Fourth Card Photo')),
                ('second_card_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Second Card Photo')),
                ('third_card_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Third Card Photo')),
            ],
            options={
                'verbose_name': "Patient's Page",
            },
            bases=('wagtailcore.page',),
        ),
    ]
