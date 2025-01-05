class SaveOwner:
    """Сервисный класс присваивает обьекту владельца = текущего пользователя"""
    def save_owner(self, serializer):
        serializer.save(owner=self.request.user)
