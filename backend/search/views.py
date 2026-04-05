print("IMPORTING VIEWS")

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from search.blocklist import block_list
from query.query import run_query
import psutil
import traceback


@api_view(["GET"])
def search_view(request):
    print("VIEW CALLED")
    query = request.query_params.get("q", "").strip()
    if not query:
        return Response({"Error": "Query not found"}, status=400)
    if query.lower() in block_list:
        return Response({"Error": "Unprocessable Content"}, status=422)
    try:
        chunk = run_query(query)
        if "Error" in chunk:
            return Response({"Error": chunk["Error"]}, status=500)

        results = chunk["results"]
        page_size = 12
        paginator = Paginator(results, page_size)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        return Response({
            "query": query,
            "count": paginator.count,
            "page_obj": {
                "page_number": page_obj.number,
                "page_size": page_size,
                "has_next": page_obj.has_next(),
                "has_prev": page_obj.has_previous()
            },
            "results": page_obj.object_list,
        })
    except Exception as e:
        traceback.print_exc()
        return Response({"Error": str(e)}, status=500)


@api_view(["GET"])
def health_view(request):
    print("Health View called")

    cpu_health = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_available = memory.available
    memory_percent = memory.percent

    return Response({
        "cpu_percentage": cpu_health,
        "memory": {"total_memory": round(memory_total / (1024 ** 3), 4), "available_memory": round(memory_available / (1024 ** 3),4), "percent_memory": memory_percent} 
    })
