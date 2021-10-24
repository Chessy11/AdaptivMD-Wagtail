# Generated by Django 3.2.8 on 2021-10-21 20:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'About Page'},
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Banner Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_title',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Banner Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='board_member_text1',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='First Board Member Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='board_member_text2',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Second Board Member Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='board_member_text3',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Third Board Member Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='board_member_text4',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fourth Board Member Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Bottom Content Photo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_text_dropdown1',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='First Dropdown Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_text_dropdown2',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Second Dropdown Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_text_dropdown3',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Third Dropdown Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_text_dropdown4',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fourth Dropdown Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_title',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Bottom Content Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_title_dropdown1',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='First Dropdown Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_title_dropdown2',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Second Dropdown Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_title_dropdown3',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Third Dropdown Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='bot_content_title_dropdown4',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Fourth Dropdown Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Content Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='content_title',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Content Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='director_board_title',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name="Director's Board Title"),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='first_board_member_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Bottom Content Photo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_board_member_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Fourth Board Member Photo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_photo1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Middle Content Photo 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_photo2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Middle Content Photo 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_text1',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Middle Content Text 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_text2',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Middle Content Text 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_title1',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Middle Content Title 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mid_content_title2',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Middle Content Title 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='page_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Page Text'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='page_title',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True, verbose_name='Page Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='second_board_member_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Second Board Member Photo'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='third_board_member_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Third Board Member Photo'),
        ),
    ]
