from django.core.paginator import Paginator

class PageBack:
    def __init__(self, request, _list):
        if _list:
            self.paginator = Paginator(_list, 10)
            self.page = self.paginator.get_page(request.GET.get('page'))
        else:
            self.paginator = None
            self.page = None