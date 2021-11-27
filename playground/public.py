from django.core.paginator import Paginator

def get_data_for_current_page(data, page_number, data_per_page):
    paginated_data = Paginator(data, data_per_page)
    return paginated_data.page(page_number)