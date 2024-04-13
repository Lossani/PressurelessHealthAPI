# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission



class PermisoSoloUsuarioInterno(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.esUsuarioInterno)



class PermisoClienteSoloRetrieve(BasePermission):
    """
    Allows access to clients only to GET by PK.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and ((not request.user.esUsuarioInterno and view.action == 'retrieve') or request.user.esUsuarioInterno)
        )



class PermisoSoloRetrieve(BasePermission):
    """
    Allows access only to GET by PK.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and view.action == 'retrieve')



class AllowPOSTWithoutToken(BasePermission):
    """
    Allows access without token only to POST.
    """

    def has_permission(self, request, view):
        return ((request.user and request.user.is_authenticated) or view.action == 'create')


class AllowPUTWithoutToken(BasePermission):
    """
    Allows access without token only to POST.
    """

    def has_permission(self, request, view):
        return ((request.user and request.user.is_authenticated) or view.action == 'update')


class AllowPOSTPUTWithoutToken(BasePermission):
    """
    Allows access without token only to POST.
    """

    def has_permission(self, request, view):
        return ((request.user and request.user.is_authenticated) or request.stream.method in ['POST', 'PUT', 'PATCH'])