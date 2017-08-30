# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from server import models
from server import serializers

class houseList(APIView):
	def get(self, request, format=None):
		objects = models.house.objects.all()
		serializer = serializers.houseSerializer(objects, many=True)
		return Response(serializer.data)

class memberList(APIView):
	def get(self, request, format=None):
		objects = models.member.objects.all()
		serializer = serializers.memberSerializer(objects, many=True)
		return Response(serializer.data)

class housePhotoList(APIView):
	def get(self, request, format=None):
		objects = models.housePhoto.objects.all()
		serializer = serializers.housePhotoSerializer(objects, many=True)
		return Response(serializer.data)

class houseAudioList(APIView):
	def get(self, request, format=None):
		objects = models.houseAudio.objects.all()
		serializer = serializers.houseAudioSerializer(objects, many=True)
		return Response(serializer.data)

class farmList(APIView):
	def get(self, request, format=None):
		objects = models.farm.objects.all()
		serializer = serializers.farmSerializer(objects, many=True)
		return Response(serializer.data)

class pointList(APIView):
	def get(self, request, format=None):
		objects = models.point.objects.all()
		serializer = serializers.pointSerializer(objects, many=True)
		return Response(serializer.data)

class cropList(APIView):
	def get(self, request, format=None):
		objects = models.crop.objects.all()
		serializer = serializers.cropSerializer(objects, many=True)
		return Response(serializer.data)

class seasonList(APIView):
	def get(self, request, format=None):
		objects = models.season.objects.all()
		serializer = serializers.seasonSerializer(objects, many=True)
		return Response(serializer.data)

class croppingList(APIView):
	def get(self, request, format=None):
		objects = models.cropping.objects.all()
		serializer = serializers.croppingSerializer(objects, many=True)
		return Response(serializer.data)

class farmPhotoList(APIView):
	def get(self, request, format=None):
		objects = models.farmPhoto.objects.all()
		serializer = serializers.farmPhotoSerializer(objects, many=True)
		return Response(serializer.data)

class farmAudioList(APIView):
	def get(self, request, format=None):
		objects = models.farmAudio.objects.all()
		serializer = serializers.farmAudioSerializer(objects, many=True)
		return Response(serializer.data)

class wellList(APIView):
	def get(self, request, format=None):
		objects = models.well.objects.all()
		serializer = serializers.wellSerializer(objects, many=True)
		return Response(serializer.data)
		
class dateTimeList(APIView):
	def get(self, request, format=None):
		objects = models.dateTime.objects.all()
		serializer = serializers.dateTimeSerializer(objects, many=True)
		return Response(serializer.data)
		
class wellPhotoList(APIView):
	def get(self, request, format=None):
		objects = models.wellPhoto.objects.all()
		serializer = serializers.wellPhotoSerializer(objects, many=True)
		return Response(serializer.data)

class wellAudioList(APIView):
	def get(self, request, format=None):
		objects = models.wellAudio.objects.all()
		serializer = serializers.wellAudioSerializer(objects, many=True)
		return Response(serializer.data)
