import re
from rest_framework.serializers import ValidationError


def validate_only_youtube_links(value):
    if not value or not isinstance(value, str):
        return

    # Ищем URL в тексте
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w .-]*'
    urls = re.findall(url_pattern, value)

    for url in urls:
        url_lower = url.lower()
        if not ('youtube.com' in url_lower or 'youtu.be' in url_lower):
            raise ValidationError(
                f"Запрещена ссылка на: {url}. Разрешены только YouTube."
            )
