from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import validate_only_youtube_links
from users.models import Subscription


class LessonSerializer(ModelSerializer):
    validators = [validate_only_youtube_links]

    class Meta:
        model = Lesson
        fields = "__all__"
        extra_kwargs = {
            "link": {"validators": [validate_only_youtube_links], "required": False}
        }


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    validators = [validate_only_youtube_links]
    is_subscribed = SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "title",
            "preview",
            "description",
            "lessons_count",
            "lessons",
            "is_subscribed",
        )

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False
