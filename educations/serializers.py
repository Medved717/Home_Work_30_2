from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from educations.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()

    def get_count_lesson(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
