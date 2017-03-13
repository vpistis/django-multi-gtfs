#
# Copyright 2012-2014 John Whitlock
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals

from django.contrib.gis import admin

from multigtfs.app_settings import MULTIGTFS_OSMADMIN
from multigtfs.models import (
    Agency, Block, Fare, FareRule, Feed, FeedInfo, Frequency, Route, Service,
    ServiceDate, Shape, ShapePoint, Stop, StopTime, Transfer, Trip, Zone)

geo_admin = admin.OSMGeoAdmin if MULTIGTFS_OSMADMIN else admin.GeoModelAdmin


class AgencyAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)
    list_display = ("id", "name", "url")
    search_fields = ['name']


class BlockAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)


class FareAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)


class FareRuleAdmin(admin.ModelAdmin):
    raw_id_fields = ('fare', 'route', 'origin', 'destination', 'contains')


class FeedInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)


class FrequencyAdmin(admin.ModelAdmin):
    raw_id_fields = ('trip',)


class RouteAdmin(geo_admin):
    raw_id_fields = ('feed', 'agency')
    list_display = ("route_id", "agency", "short_name", "long_name")
    search_fields = ["route_id", "agency__name", "short_name", "long_name"]


class ServiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)
    list_display = ("id", "feed", "start_date", "end_date")
    search_fields = ["feed__name", "start_date", "end_date"]


class ServiceDateAdmin(admin.ModelAdmin):
    raw_id_fields = ('service',)
    list_display = ("id", "service", "date", "exception_type")


class ShapeAdmin(geo_admin):
    raw_id_fields = ('feed',)
    list_display = ("id", "shape_id", "feed",)
    search_fields = ["id", "shape_id", "feed__name", ]


class ShapePointAdmin(geo_admin):
    raw_id_fields = ('shape',)


class StopAdmin(geo_admin):
    raw_id_fields = ('feed', 'zone', 'parent_station')
    list_display = ("id", "feed", "stop_id", "code", "name", "desc", "point")
    search_fields = ["id", "stop_id", "code", "name", "desc"]


class StopTimeAdmin(admin.ModelAdmin):
    """tempi delle fermate"""
    raw_id_fields = ('stop', 'trip')
    list_display = ("id", "trip", "arrival_time", "departure_time", "stop_sequence", "stop_headsign")
    search_fields = ["stop_headsign"]


class TransferAdmin(admin.ModelAdmin):
    raw_id_fields = ('from_stop', 'to_stop')


class TripAdmin(geo_admin):
    raw_id_fields = ('route', 'service', 'block', 'shape')
    list_display = ("route", "service", "headsign")


class ZoneAdmin(admin.ModelAdmin):
    raw_id_fields = ('feed',)


admin.site.register(Agency, AgencyAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Fare, FareAdmin)
admin.site.register(FareRule, FareRuleAdmin)
admin.site.register(Feed)
admin.site.register(FeedInfo, FeedInfoAdmin)
admin.site.register(Frequency, FrequencyAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceDate, ServiceDateAdmin)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(ShapePoint, ShapePointAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(StopTime, StopTimeAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Zone, ZoneAdmin)
