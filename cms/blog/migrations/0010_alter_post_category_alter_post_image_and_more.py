# Generated by Django 4.2.11 on 2024-04-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('LS', 'Lifestyle'), ('W', 'World'), ('BS', 'Business'), ('TC', 'Tech'), ('DS', 'Design'), ('CL', 'Culture'), ('PL', 'Politics'), ('OP', 'Opinion'), ('SC', 'Science'), ('HL', 'Health'), ('ST', 'Style'), ('TV', 'Travel'), ('SP', 'Sports'), ('UC', 'Uncategorized')], default='UC', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/how-to-write-a-blog-post.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quote',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
