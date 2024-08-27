import requests

class BaseURLSession(requests.Session):
    def __init__(self, base_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        # Prepend base_url if provided and if the URL is not absolute
        if self.base_url and not url.startswith(('http://', 'https://')):
            url = f'{self.base_url}{url}'
        return super().request(method, url, *args, **kwargs)