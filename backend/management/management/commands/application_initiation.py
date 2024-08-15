# Django - base command import:
from django.core.management.base import CommandError
from django.core.management.base import BaseCommand

# Django - authentication models import:
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

# WanderSwiss - management model import:
from management.models.user_model import UserModel


# Command class:
class Command(BaseCommand):
    help = 'Creates a default administrator if none exists'

    def create_default_groups(self):

        # Check if RW group exist:
        if Group.objects.filter(name='ReadWriteAccess').exists():
            # Deled old RW group:
            Group.objects.get(name='ReadWriteAccess').delete()
            # Inform about old RW group deletion:
            self.stdout.write(self.style.WARNING(
                f'1.0: Old RW group has been deleted.'))
        # Check if RO group exist:
        if Group.objects.filter(name='ReadOnlyAccess').exists():
            # Deled old RO group:
            Group.objects.get(name='ReadOnlyAccess').delete()
            # Inform about old RO group deletion:
            self.stdout.write(self.style.WARNING(
                f'1.0: Old RO group has been deleted.'))

        # Create a nwe groups:
        red_write_group, rw_created = Group.objects.get_or_create(
            name='ReadWriteAccess') 
        read_only_group, ro_created = Group.objects.get_or_create(
            name='ReadOnlyAccess')

        if rw_created and ro_created:
            # Inform about new groups creation:
            self.stdout.write(self.style.SUCCESS(
                f'1.1: Successfully created default groups.'))
            # Create a new permissions:
            red_write_permissions = Permission.objects.filter(codename__in=[
                'read_write', 'read_only'])
            read_only_permissions = Permission.objects.filter(codename='read_only')
            # Assign permissions to groups:
            red_write_group.permissions.set(red_write_permissions)
            read_only_group.permissions.set(read_only_permissions)
            # Return RW group:
            return red_write_group
        else: # Send a error message:
            self.stdout.write(self.style.ERROR(
                f'1.1: An error occurred while creating a group.'))

    def create_default_administrator(self, red_write_group):

        # Prepare administrator data:
        username = 'admin'
        email = 'admin@capybara.com'
        password = 'admin'

        # Check if administrator exist:
        if UserModel.objects.filter(username=username).exists():
            # Get the administrator object:
            admin = UserModel.objects.get(username=username)
            # Delete the administrator object:
            admin.delete()
        try: # Try to create a nwe administrator:
            administrator = UserModel.objects.create_superuser(
                username, email, password)
        except Exception as exception:
            self.stdout.write(self.style.ERROR(f'2.1: {exception}'))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'2.1: Successfully created default administrator.'))
            # Add administrator user to RedWrite group
            red_write_group.user_set.add(administrator)
            self.stdout.write(self.style.SUCCESS(
                '2.2: Successfully added Administrator to ReadWriteAccess group.'))

    def handle(self, *args, **options):
        
        # 1: Create default groups:
        red_write_group = self.create_default_groups()
        
        # 2: Create default administrator:
        self.create_default_administrator(red_write_group)
