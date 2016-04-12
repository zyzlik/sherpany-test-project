from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS = settings.CREDENTIALS
SCOPES = settings.SCOPES


class Location(models.Model):
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('latitude')
    )
    lng = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('longitude')
    )
    address = models.CharField(
        verbose_name=_('address'),
        max_length=50,
    )


def authorize():
    # Preparing for making API calls
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS, SCOPES
    )
    http_auth = credentials.authorize(Http())
    service = build("fusiontables", "v2", http=http_auth)
    return service


class FusionTable:

    def create_fusion_table():
        service = authorize()
        sql = "CREATE TABLE 'locations' (lat: NUMBER, lng: NUMBER, address: STRING)"
        response = service.query().sql(sql=sql).execute()
        print(response)
        return response['rows'][0][0]

    def __init__(self, table_id=None):
        if table_id:
            self.table_id = table_id
        else:
            self.table_id = FusionTable.create_fusion_table()

    def get_fusion_table(self):
        service = authorize()
        t = service.table()
        response = t.get(tableId=self.table_id).execute()
        return response

    def reset_fusion_table(self):
        service = authorize()
        sql = "DELETE FROM %s" % (self.table_id)
        response = service.query().sql(sql=sql).execute()
        return response

    def insert_fusion_table(self, lat, lng, address):
        service = authorize()
        sql = "INSERT INTO %s (lat, lng, address) VALUES (%s, %s, '%s')" % (
            self.table_id, lat, lng, address
        )
        service.query().sql(sql=sql).execute()

    def check_dublicate_fusion_table(self, address):
        service = authorize()
        sql = "SELECT * FROM %s WHERE address = '%s'" % (
            self.table_id, address
        )
        response = service.query().sql(sql=sql).execute()
        if response.get('rows'):
            print('DUBLICATE!')
            return True
        return False

    def get_data_from_fusion_table(self):
        service = authorize()
        sql = "SELECT * FROM %s" % (self.table_id)
        response = service.query().sql(sql=sql).execute()
        return response.get('rows')
