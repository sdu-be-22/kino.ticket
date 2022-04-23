from .models import *


class DataMixin:
    # paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        # context['header_menu'] = header_menu
        context['movies'] = Movie.objects.all()
        return context