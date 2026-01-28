import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def create_or_update_superuser(sender, **kwargs):
    username = os.getenv("DJANGO_SUPERUSER_USERNAME")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

    if not username or not password:
        return

    user, created = User.objects.get_or_create(
        username=username,
        defaults={"email": email}
    )

    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()

    if created:
        print("✅ Superusuario creado automáticamente")
    else:
        print("🔁 Superusuario actualizado automáticamente")
