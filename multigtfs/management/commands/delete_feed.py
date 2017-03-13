"""
Created on 22/lug/2016

@author: matteomallus
"""
from django.core.management.base import BaseCommand, CommandError

from multigtfs.models.feed import Feed


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('feed_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for feed in options['feed_id']:
            try:
                feed = Feed.objects.get(pk=feed)
                print(feed)
                feed.delete()
                self.stdout.write(self.style.SUCCESS('Successfully closed feed '))
            except Exception as e:
                raise CommandError('Feed "%s" does not exist' % feed)
