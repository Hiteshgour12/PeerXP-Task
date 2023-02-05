from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from .serializer import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = NewUserSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
       
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


    # def delete(self, request, pk, format=None):
    #         user = request.user
    #         try:
    #             if user.role == 'admin':
    #                 item =  User.objects.get(pk=pk)
    #                 item.delete()
    #                 return Response({
    #                     'message': 'User Deleted Successfully'
    #                 })
    #             else:
    #                 response = {
    #                     # 'success': False,
    #                     # 'status_code': status.HTTP_403_FORBIDDEN,
    #                     'message': 'You are not authorized to perform this action'
    #                 }
    #                 return Response(response, status.HTTP_403_FORBIDDEN)
    #         except:
    #             return Response("User cannot be deleted")

class DepartmentView(generics.GenericAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        if user.role == 'admin':
            # user1 = User.objects.get(email=user)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(created_by=user.role)
            user_data = serializer.data

            return Response(user_data, status=status.HTTP_201_CREATED)
        else:
                response = {
                    # 'success': False,
                    # 'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'You are not authorized to perform this action'
                }
                return

    def get(self,request):
            user = request.user
        # try:
            if user.role == 'admin':
                item = Deparments.objects.all()
                
                serializer = DepartmentListSerializer(item, many=True)
                response = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Successfully fetched Deparments',
                    'Deparments': serializer.data

                }
                return Response(response, status=status.HTTP_200_OK)
                
            else:
                response = {
                    # 'success': False,
                    # 'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'You are not authorized to perform this action'
                }
                return Response(response, status.HTTP_403_FORBIDDEN)
        # except:
        #     return Response("There is no Deparments")

class DepartmentUpdateView(generics.GenericAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)

    
    def put(self, request, pk=None, format=None):
            user = request.user
        # try:
            if user.role == 'admin':
                update = Deparments.objects.get(pk=pk)
                serializer = self.serializer_class(instance=update,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save(last_update_at=True)
                response = Response()
                response.data = {
                    'message': 'Deparment Updated Successfully',
                    'data': serializer.data
                }

                return response
            else:
                response = {
                    # 'success': False,
                    # 'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'You are not authorized to perform this action'
                }
                return Response(response, status.HTTP_403_FORBIDDEN)

        # except:
        #     return Response('Product already exist')

    def delete(self, request, pk, format=None):
        user = request.user
        try:
            if user.role == 'admin':
                item =  Deparments.objects.get(pk=pk)
                item.delete()
                return Response({
                    'message': 'Departments Deleted Successfully'
                })
            else:
                response = {
                    # 'success': False,
                    # 'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'You are not authorized to perform this action'
                }
                return Response(response, status.HTTP_403_FORBIDDEN)
        except:
            return Response("Department cannot be deleted")



    def get(self,request,pk):
            user = request.user
        # try:
            if user.role == 'admin':
                    item = Deparments.objects.get(pk=pk)
                # print(item[0].id)
                # if item[0].id == pk:
                    serializer = self.serializer_class(item)
                    response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Successfully fetched Deparments',
                        'Departments': serializer.data

                    }
                    return Response(response, status=status.HTTP_200_OK)
                # else:
                #     response={
                #         "No Product Found"
                #     }
                    return Response (response)
            else:
                response = {
                    # 'success': False,
                    # 'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'You are not authorized to perform this action'
                }
                return Response(response, status.HTTP_403_FORBIDDEN)
        # except:
        #     return Response("There is no product")


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = request.data
        # user1 = MyUser.objects.get(name=user['name'])
        # print(user1)
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
       

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(generics.GenericAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        if user.role != 'admin':
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.filter(role='user')
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)


class UserView(generics.GenericAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
       
        users = User.objects.get(email=user)
        serializer = self.serializer_class(users)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched users',
            'users': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)


class TicketView(generics.GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=user)
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
        

    def get(self,request):
            user = request.user
        
            if user.role == 'admin':
                item = Tickets.objects.all()
                
                serializer = TicketListSerializer(item, many=True)
                response = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Successfully fetched Tickets',
                    'Tickets': serializer.data

                }
                return Response(response, status=status.HTTP_200_OK)
                
            else:
                
                item = Tickets.objects.get(created_by=user)
                
                serializer = TicketListSerializer(item)
                response = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Successfully fetched Tickets',
                    'Tickets': serializer.data

                }
                return Response(response, status=status.HTTP_200_OK)
                

    def delete(self, request, pk, format=None):
        user = request.user
        try:
            if user.role == 'admin':
                item =  Tickets.objects.get(pk=pk)
                item.delete()
                return Response({
                    'message': 'Ticket Deleted Successfully'
                })
            else:
                response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        except:
            return Response("Ticket cannot be deleted")

class TicketsingleView(generics.GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        user=request.user
        item = Tickets.objects.filter(created_by=user)
        serializer = TicketListSerializer(item,many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched Tickets',
            'Tickets': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)