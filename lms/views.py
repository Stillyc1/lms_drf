from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lms.models import Course, Lesson, SubscriptionCourse
from lms.paginators import CustomPagination
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionCourseSerializer
from lms.services import SaveOwner
from lms.tasks import send_mail_receiver
from users.permissions import IsModerator, IsOwner
from django.views.generic import ListView


class MailingView(ListView):
    """Класс представления Всех рассылок на главной странице"""

    model = Lesson
    template_name = "lms/home.html"
    context_object_name = "lms"


class CourseViewSet(SaveOwner, viewsets.ModelViewSet):
    """Реализация представления курсов через ViewSet (полный crud)"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        SaveOwner.save_owner(self, serializer)  # вынесен в сервисный модуль

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action in ["retrieve", "update"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def partial_update(self, request, *args, **kwargs):
        course_id = self.get_object().id
        all_sub_course = SubscriptionCourse.objects.filter(course=course_id)

        if all_sub_course.exists():
            send_mail_receiver.delay([sub.user.email for sub in all_sub_course])

        return super().partial_update(request=request, *args, **kwargs)


class SubscriptionCourseAPIView(generics.ListAPIView):
    queryset = SubscriptionCourse.objects.all()
    serializer_class = SubscriptionCourseSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = SubscriptionCourse.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка отключена'
        else:
            SubscriptionCourse.objects.create(user=user, course=course_item)
            message = 'Подписка включена'
        return Response({"message": message})


class LessonCreateAPIView(SaveOwner, generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        SaveOwner.save_owner(self, serializer)  # -||-


class LessonListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Реализация представления удаления урока через generic. DestroyAPIView"""
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner,)
