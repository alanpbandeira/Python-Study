from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from games.models import Game
from games.serializers import GameSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_serializer = GameSerializer(games, many=True)
        # return JsonResponse(game_serializer.data, safe=False)
        return Response(game_serializer.data)
    elif request.method == 'POST':
        # game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            # return JsonResponse(game_serializer.data, 
                                # status=status.HTTP_201_CREATED)
            return Response(game_serializer.data, 
                            status=status.HTTP_201_CREATED)
    else:
        # return JsonResponse(game_serializer.errors, 
        #                      status=status.HTTP_400_BAD_REQUEST)
        return Response(game_serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        # return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serialized = GameSerializer(game)
        # return JsonResponse(game_serialized.data)
        return Response(game_serialized.data)
    elif request.method == 'PUT':
        # game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=request.data)
        if game_serializer.is_valid:
            game_serializer.save()
            # return JsonResponse(game_serializer.data)
            return Response(game_serializer.data)
        else:
            # return JsonResponse(game_serializer.errors,
            #                     status=status.HTTP_400_BAD_REQUEST)
            return Response(game_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        game.delete()
        # return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)