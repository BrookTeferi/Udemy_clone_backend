from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course, Comment, Course_section, Episode
from users.serializers import UserSerializer 


class CourseDisplaySerializer(ModelSerializer):
    student_no= serializers.IntegerField(source="get_enrolled_student")
    author=UserSerializer() 
    image_url=serializers.CharField(source='get_absolute_img_url')

    class Meta:
        model=Course
        fields=[
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url'
        ] 

class CommentSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Comment
        exclude=[
            'id'
        ]

class EpisodeUnpaidSerializer(ModelSerializer):
    length=serializers.CharField(source='get_video_length_time')
    class Meta:
        model=Episode
        exclude=[
            'file',
        ]

class EpisodepaidSerializer(ModelSerializer):
     length=serializers.CharField(source='get_video_length_time')
     class Meta:
        model=Episode
        fields=[
            'file',
            'length',
            'title',
            ]

class CourseSectionUnpaidSerialzier(ModelSerializer):
    episods=EpisodeUnpaidSerializer(many=True)
    total_duration=serializers.CharField(source='total_length')
    
    class Meta:
        model=Course_section
        fields=[
            'section_title',
            'episods' ,
            'total_duration',
        ]

class CourseSectionpaidSerialzier(ModelSerializer):
    episodes=EpisodepaidSerializer(many=True)
    total_duration=serializers.CharField(source='total_length')
    
    class Meta:
        model=Course_section
        fields=[
            'section_title',
            'episodes',
            'total_duration',
        ]

class CourseUnpaidSerializer(ModelSerializer):
    comments=CommentSerializer(many=True)
    author=UserSerializer()
    course_section=CourseSectionUnpaidSerialzier(many=True)
    student_no=serializers.IntegerField(source='get_enrolled_student')
    total_lectures=serializers.IntegerField(source='get_total_lectures')
    total_duration=serializers.CharField(source='total_course_length')
    image_url=serializers.CharField(source='get_absolute_img_url')
    class Meta:
        model=Course
        exclude=[
            'id'
        ]

class CoursePaidSerializer(ModelSerializer):
    comments=CommentSerializer(many=True)
    author=UserSerializer()
    course_section=CourseSectionpaidSerialzier(many=True)
    student_no=serializers.IntegerField(source='get_enrolled_student')
    total_lectures=serializers.IntegerField(source='get_total_lectures')
    total_duration=serializers.CharField(source='total_course_length')
    image_url=serializers.CharField(source='get_absolute_img_url')
    class Meta:
        model=Course
        exclude=[
            'id',
        ]

class CourseListSerializer(ModelSerializer):

    student_no= serializers.IntegerField(source='get_enrolled_student')
    author=UserSerializer()
    description=serializers.CharField(source='get_breif_description')
    total_lecters=serializers.IntegerField(source='get_total_lectures')
    class Meta:
         model=Course
         fields=[
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url',
            'description',
            'total_lectures'
         ]

class CartItemSerializer(ModelSerializer):

    author=UserSerializer()
    image_url=serializers.CharField(source='get_absolute_img_url')

    class Meta:
        model=Course
        fields=[
            'author',
            'title',
            'price',
            'image_url',

        ]


