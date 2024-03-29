# Django For Beginners

## Demo

Run project: 

```console
python manage.py runserver
```
Local host: http://127.0.0.1:8000

Home page:

<img src="./imgs/Home.png" alt="Home image" class="center" />

Article list:

<img src="./imgs/Article_list.png" alt="Article list" class="center" />

## Build project

Code nằm ở thư mục `source`:
* nhớ vào `source` để chạy code 
    ```console 
    cd .\source\  
    ```

Tạo môi trường ảo chứa framework django: 
```console
pipenv install django
```

Bật môi trường ảo:
```console
pipenv shell
```

Tạo project `newspaper`, chú ý là có dấu `.` ở cuối cùng:
```console
django-admin startproject newspaper_project .
```
Kiểm tra project: 
```console
python manage.py runserver
```
Local host: http://127.0.0.1:8000

## Pre-commit
Để đảm bảo tính thống nhất trong code, code dễ nhìn và dễ bảo trì hơn thì ta cần phải sử dụng pre-commit:
```console
precommit-install
```

có các file như:

    .pre-commit-config.yaml
    .pyproject.toml
    .flake8


Tham khảo 2 bài viết này: 

https://learndjango.com/tutorials/pre-commit-django

https://builtwithdjango.com/blog/improve-your-code-with-pre-commit#flake8

## Thêm app cho project

```console
python manage.py startapp <app_name>   
```

Ví dụ tạo users app: 

```console
python manage.py startapp users
```

Khi model của Django thay đổi (tạo mới / chỉnh sửa / xóa) thì phải tạo migrate và migrate nó lại:

```console
python manage.py makemigrations [<app_name>]
python manage.py migrate  
```

## Thêm tài khoản admin/staff/superuser

```console
python manage.py createsuperuser
```
* user - User@123 
* admin1 - Hoabanglang@123

## Đổi mật khẩu admin/staff/superuser

```console
python manage.py changepassword <username>
```

## Kiểm thử - test case

```console
python manage.py test
```

Kết quả:

```
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.064s

OK
Destroying test database for alias 'default'...
```
�