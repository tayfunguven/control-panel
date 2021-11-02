from import_export import resources
from Staff.models import *

class ReportResource(resources.ModelResource):
    model = Report

class AdvanceRequestResource(resources.ModelResource):
    model = AdvanceRequest

class PermitRequestResource(resources.ModelResource):
    model = PermitRequest