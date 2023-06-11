import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
            return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }
    
    def upload_link(self, file_path: str):
        '''Получаем ссылку на место на Яндекс.Диске'''
        
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, file_path):
        '''Метод загружает файл на Яндекс.Диск'''
        
        href = self.upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open('test.txt', 'rb'))
        response.raise_for_status()
        # pprint(response)
        if response.status_code == 201:
            print('Файл загружен успешно!')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Нетология/test_20230611'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)