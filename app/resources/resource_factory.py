import random
from flask import request, render_template, json
from flask_restful import Resource, request
import os
import sys

spcResources = [
    'departamento',
    'carrera',
    'asignatura',
    'plan'
]

def getAll(resource):
    fileName = '/app/resources/schemes/examples/' + resource + '.json'
    if not os.path.exists(os.path.realpath(fileName)):
        return None

    file =  open(
        os.path.realpath(fileName)
    )
    return json.load(file)

def getOneOf(resource, depends, dependsId):
    fileName = '/app/resources/schemes/examples/' + resource + '_' + depends + '_' + dependsId + '.json'
    if not os.path.exists(os.path.realpath(fileName)):
        return None

    file = open(
        os.path.realpath(fileName)
    )
    return json.load(file)

class All(Resource):
    def get(self, resource):
        if not resource in spcResources:
            return {}, 404

        responseResource = getAll(resource)
        return responseResource, 200

class One(Resource):
    def get(self, resource, resourceId):
        if not resource in spcResources or resourceId <= 0:
            return {}, 404

        responseResource = getAll(resource)
        resoucesFilteredById = filter(lambda item: item["id"] == int(resourceId), responseResource)
        return list(resoucesFilteredById), 200

class OneOf(Resource):
    def get(self, resource, depends):
        if not (resource in spcResources and depends in spcResources):
            return {}, 404

        dependsId = request.args.get('id')
        responseResource = getOneOf(resource, depends, dependsId)
        if not responseResource:
            return [], 404
        return responseResource, 200
