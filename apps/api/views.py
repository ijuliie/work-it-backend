from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Workout.objects.filter(owner=self.request.user)
        return queryset

    serializer_class = WorkoutSerializer

    def create(self, request):
        return super().create(request)

    def update(self, request, *args, **kwargs):
        Workout.objects.get(pk=self.kwargs['pk'])
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        Workout.objects.get(pk=kwargs['pk'])
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WorkoutDetailsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Workout.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = WorkoutSerializer