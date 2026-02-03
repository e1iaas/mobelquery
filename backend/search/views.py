from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from query.query import run_query



@api_view(["GET"])
def search_view(request):
    query = request.query_params.get("q", "")
    chunk = run_query(query)
    return Response({
        "query": query,
        "results": chunk
    })
