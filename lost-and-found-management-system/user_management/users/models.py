# import uuid
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, name, password=None, role='user'):
#         if not email:
#             raise ValueError("Users must have an email address")
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name, role=role)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password=None):
#         user = self.create_user(email, name, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     role = models.CharField(max_length=255, default='user')
#     created_at = models.DateTimeField(auto_now_add=True)

#     # Add related_name arguments to resolve conflicts
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',  # Custom related name
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',  # Custom related name
#         blank=True,
#     )

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email


import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom manager to handle creation of users and admins.
    """
    def create_user(self, email, name, password=None, role='user'):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email, name, password=None):
        """
        Create and return an admin user.
        """
        return self.create_user(email, name, password, role='admin')


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with email-based authentication and role-based permissions.
    """
    USER = 'user'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin site access
    created_at = models.DateTimeField(auto_now_add=True)

    # Assign custom manager
    objects = UserManager()

    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        """
        Automatically set `is_staff` and `is_superuser` based on the role.
        """
        if self.role == self.ADMIN:
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.role})"
