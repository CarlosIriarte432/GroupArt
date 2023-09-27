# Generated by Django 4.2.2 on 2023-09-27 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='involved_user',
        ),
        migrations.RemoveField(
            model_name='analyticsdata',
            name='involved_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_user',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='recipient_user',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
        migrations.RemoveField(
            model_name='problemreport',
            name='provider_user',
        ),
        migrations.RemoveField(
            model_name='problemreport',
            name='service',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.RemoveField(
            model_name='ratingandcomment',
            name='client_user',
        ),
        migrations.RemoveField(
            model_name='ratingandcomment',
            name='provider_user',
        ),
        migrations.RemoveField(
            model_name='ratingandcomment',
            name='service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
        migrations.RemoveField(
            model_name='servicehistory',
            name='service',
        ),
        migrations.DeleteModel(
            name='SocialMediaIntegration',
        ),
        migrations.RemoveField(
            model_name='supportmessage',
            name='receiver_user',
        ),
        migrations.RemoveField(
            model_name='supportmessage',
            name='sender_user',
        ),
        migrations.RemoveField(
            model_name='tagsserviceposts',
            name='service_post',
        ),
        migrations.RemoveField(
            model_name='tagsserviceposts',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='client_user',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='service',
        ),
        migrations.DeleteModel(
            name='ActivityLog',
        ),
        migrations.DeleteModel(
            name='AnalyticsData',
        ),
        migrations.DeleteModel(
            name='ContentType',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Multimedia',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='ProblemReport',
        ),
        migrations.DeleteModel(
            name='RatingAndComment',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceCategory',
        ),
        migrations.DeleteModel(
            name='ServiceHistory',
        ),
        migrations.DeleteModel(
            name='ServiceStatus',
        ),
        migrations.DeleteModel(
            name='SupportMessage',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='TagsServicePosts',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
