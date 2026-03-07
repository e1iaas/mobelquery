print("IMPORTING VIEWS")

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator

from query.query import run_query


@api_view(["GET"])
def search_view(request):
    print("VIEW CALLED")
    query = request.query_params.get("q", "").strip()
  
    if not query:
        return Response({"Error": "Query not found"}, status=400)

    chunk = run_query(query)
    results = chunk["results"]

    page_size = 12

    paginator = Paginator(results, page_size)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    return Response({
        "query": query,
        "count": paginator.count,
        "page_obj":{
            "page_number": page_obj.number,
            "page_size": page_size,
            "has_next": page_obj.has_next(),
            "has_prev": page_obj.has_previous()
        },
        "results": page_obj.object_list,
    })
