# from rest_framework import routers
from .viewsets import CalcadoViewSet
from rest_framework.routers import DefaultRouter, Route, DynamicRoute

class CustomRouter(DefaultRouter):
    routes = [
        # List route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'post': 'custom_create',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]

router = CustomRouter()
router.register(r'resources', CalcadoViewSet)
