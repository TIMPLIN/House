# Generated by Django 3.0.8 on 2020-07-19 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='小区')),
                ('city', models.CharField(choices=[('bj', '北京'), ('sh', '上海'), ('sz', '深圳'), ('gz', '广州'), ('hz', '杭州')], max_length=2, verbose_name='城市')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': '小区',
                'verbose_name_plural': '小区',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=108, verbose_name='描述')),
                ('bedroom', models.CharField(choices=[('1', '1室1厅'), ('2', '2室1厅'), ('3', '3室1厅'), ('4', '4室2厅')], max_length=1, verbose_name='房型')),
                ('direction', models.CharField(choices=[('e', '东'), ('s', '南'), ('w', '西'), ('n', '北')], max_length=2, verbose_name='朝向')),
                ('floor', models.CharField(choices=[('l', '低楼层'), ('m', '中楼层'), ('h', '高楼层')], max_length=1, verbose_name='楼层')),
                ('area', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='面积(平方米)')),
                ('area_class', models.CharField(blank=True, choices=[('1', '<50平米'), ('2', '50-70平米'), ('3', '70-90平米'), ('4', '90-140平米'), ('5', '>140平米')], max_length=1, null=True, verbose_name='面积')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格(万元)')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhouse.Community', verbose_name='小区')),
            ],
            options={
                'verbose_name': '二手房',
                'verbose_name_plural': '二手房',
            },
        ),
    ]
