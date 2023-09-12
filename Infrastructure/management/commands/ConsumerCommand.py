from django.core.management.base import BaseCommand, CommandError
from Infrastructure.kafka.consumer import Consumer

class Command(BaseCommand):
    help = 'Starts the consumer'

    def add_arguments(self, parser):
        parser.add_argument('--topic', nargs='+', type=str,action='append' ,help='Topic name')
        parser.add_argument('--group', nargs='+', type=str,help='Group name')

    def handle(self, *args, **options):
        try:
            listTopic = []
            groupConsumer = ""
            
            # # for topic in options['--topic']:
            # #     self.stdout.write(self.style.SUCCESS(topic))
            if options['topic']:
                listTopic = options['topic'][0]
            
            
            if options['group']:
                groupConsumer = options['group'][0]
                
        
            consumer = Consumer(listTopic,groupConsumer)
            consumer.start()
        except Exception as e:
            
            self.stderr.write(self.style.ERROR(e))
            raise CommandError('Consumer failed to start')
        self.stdout.write(self.style.SUCCESS('Consumer started successfully'))