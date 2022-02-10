from rest_framework.pagination import PageNumberPagination

class MyCustomPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p' # will override .../?page=3 to .../?p=3
    page_size_query_param = 'records'  # client can set page size or how many records per page
    
    # link to use above feature : http://127.0.0.1:8000/api1/v1/viewset/students/?p=2&page=1&records=2
    
    max_page_size = 6       
    
    # http://127.0.0.1:8000/api1/v1/viewset/students/?page=1&records=8
    # in above link page_size set by client is 8 > max_page_size. So per page only
    # 6 records or max_page_size shown

    last_page_strings = 'end'   # .../?page=last to .../?page=end 