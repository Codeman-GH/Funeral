import django.dispatch


# Create your Signals here.

tribute_approved = django.dispatch.Signal(providing_args=["tribute_id"])
memory_approved = django.dispatch.Signal(providing_args=["memory_id"])
photo_approved = django.dispatch.Signal(providing_args=["photo_id"])
