"""
Restframework base viewsets.
"""
from rest_framework import permissions, viewsets


class ModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"

    def get_queryset(self):
        """
        We define this function as setting `queryset` on the class causes the
        query to be cached which will result that when an object is deleted
        (which gets caught and is instead archived), to still return that
        archived object, even though the query manager should now filter it out.
        """
        return self.serializer_class.Meta.model.objects.all()
