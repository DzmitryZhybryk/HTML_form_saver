# HTML form saver

Приложение принимает данные из HTML формы, валидирует их и сохраняет в CSV файл. Имеет два отдельных микросервиса. Может запускаться через docker-compose файл.

+ Директория "csv_saver_app" содержит HTML формы и Python код для взаимодействия с ними.
+ Директория "csv_storage_app" содержит Python код для работы с CSV файлом. 
