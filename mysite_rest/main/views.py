from django.shortcuts import render
from .models import ToDoList, Item
from .serializer import ToDoListSerializer, ItemSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# @csrf_exempt
# def ToDoList_main(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         todo = ToDoList.objects.all()
#         item = Item.objects.all()
#         serializer = ToDoListSerializer(todo, many=True)
#         serializer2 = ItemSerializer(item, many=True)
#         return JsonResponse(serializer.data, safe=False), JsonResponse(serializer2.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ToDoListSerializer(data=data)
#         serializer2 = ItemSerializer(data=data)
#         if serializer.is_valid() and serializer2.is_valid():
#             serializer.save()
#             serializer2.save()
#             return JsonResponse(serializer.data, status=201), JsonResponse(serializer2.data, status=201)
#         return JsonResponse(serializer.errors, status=400), 

# @csrf_exempt
# def ToDoList_detail(request, pk):
#     try:
#         todo = ToDoList.objects.get(pk=pk)
#         item = Item.objects.get(pk=pk)
#     except ToDoList.DoesNotExist or Item.DoesNotExist:
#         return HttpResponse(status=404)


#     if request.method == 'GET':
#         serializer = ToDoListSerializer(todo, many=True)
#         serializer2 = ItemSerializer(item, many=True)
#         return JsonResponse(serializer.data, safe=False), JsonResponse(serializer2.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ToDoListSerializer(data=data)
#         serializer2 = ItemSerializer(data=data)
#         if serializer.is_valid() and serializer2.is_valid():
#             serializer.save()
#             serializer2.save()
#             return JsonResponse(serializer.data, status=201), JsonResponse(serializer2.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         todo.delete()
#         item.delete()
#         return HttpResponse(status=204)

@csrf_exempt
def ToDoList_main(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        todolist = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ToDoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def ToDoList_detail(request,pk):
    try:
        snippet = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ToDoListSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ToDoListSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def Item_main(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Item.objects.all()
        serializer = ItemSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def Item_detail(request,pk):
    try:
        snippet = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
