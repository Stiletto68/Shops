from rest_framework import viewsets

from shops.models import Organization, Shop
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from drf_renderer_xlsx.renderers import XLSXRenderer
from drf_renderer_xlsx.mixins import XLSXFileMixin
from shops.rest.shops_rest import ShopsJSONSerializer
from shops.rest.organizations_rest import OrganizationJSONSerializer


class ShopsAsJSON(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая создавать, просматривать и изменять записи shop
    """
    queryset = Shop.objects.all()
    serializer_class = ShopsJSONSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer)

    def dispatch(self, *args, **kwargs):
        return super(ShopsAsJSON, self).dispatch(*args, **kwargs)


class OrganizationsAsJSON(XLSXFileMixin, viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая создавать, просматривать и изменять записи organizacion
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationJSONSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XLSXRenderer)
    filename = 'organizations.xlsx'

    def dispatch(self, *args, **kwargs):
        return super(OrganizationsAsJSON, self).dispatch(*args, **kwargs)

    # Properties for XLSX
    column_header = {
        'titles': [
            "Column_1_name",
            "Column_2_name",
            "Column_3_name",
        ],
        'column_width': [17, 30, 17],
        'height': 25,
        'style': {
            'fill': {
                'fill_type': 'solid',
                'start_color': 'FFCCFFCC',
            },
            'alignment': {
                'horizontal': 'center',
                'vertical': 'center',
                'wrapText': True,
                'shrink_to_fit': True,
            },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
            },
            'font': {
                'name': 'Arial',
                'size': 14,
                'bold': True,
                'color': 'FF000000',
            },
        },
    }
    body = {
        'style': {
            'fill': {
                'fill_type': 'solid',
                'start_color': 'FFCCFFCC',
            },
            'alignment': {
                'horizontal': 'center',
                'vertical': 'center',
                'wrapText': True,
                'shrink_to_fit': True,
            },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
            },
            'font': {
                'name': 'Arial',
                'size': 14,
                'bold': False,
                'color': 'FF000000',
            }
        },
        'height': 40,
    }
