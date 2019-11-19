from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, UserDetailSerializer
from .models import Todo

User = get_user_model()

# 특정 method 의 요청만 허용
@api_view(['POST'])
def todo_create(request):
    # 사용자의 데이터 받아오기
    # request.data 는 axios 의 body 로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    # raise_exception => valid 하지 않을 경우 오류 메시지
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 사용자가 새롭게 작성한 data 를 응답해준다.
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'PUT':
        # data=request.data => 수정하려고 하는 데이터
        # instance todo 를 request.data 로 넘어온 값으로 수정하겠다.
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) # 수정한 값을 return 해준다.
    if request.method == 'DELETE':
        # 204 코드 : 삭제했음.
        todo.delete()
        return Response(status=204) # 요청에 성공했지만 컨텐츠는 없다는 걸 알려주는 status code


@api_view(['GET'])
def user_detail(request, user_id):
    # pk가 user_id 인 user 를 찾겠다. 없으면 404를 주겠다.
    user = get_object_or_404(User, pk=user_id)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)