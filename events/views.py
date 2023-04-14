from rest_framework import status
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'event_title',
        'location',
        'country',
        'difficulty'
    ]

    filterset_fields = [
        'owner__profile',
        'owner__followed__owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()
