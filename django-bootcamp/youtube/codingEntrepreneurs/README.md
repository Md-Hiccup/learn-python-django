## CodingEnterpreneurs

#### 10 Days Coding to build a Single Page eCommerce app from scratch
>   https://youtu.be/RUMohoZzNLc

-   Django
-   Models/Views/Templates
-   QuerySets & Model Managers
-   Tests (Models & Views)
-   Authentication (Django & Social)


### Day 0

#### Initialize the project. (00:00 - 25:00)
    -   mkdir dj-bootcamp
    -   cd dj-bootcamp
    -   virtualenv env -p python3 .
    -   source env/bin/activate
    -   pip install django
    -   django-admin startproject dj_bootcamp .
    -   python manage.py migrate
    -   python manage.py createsuperuser
    -   python mannage.py runserver


### Day 1

#### Classes, Functions and Syntax
    -   Virtual Environments
    -   Classes
    -   Functions
    -   Basic Maths
    -   Objects & Methods
    -   Basic Syntax

#### Why Django
    -   It's a Web-Framework
    -   It's written in Python
    -   Batteries Included (User authentication, Admin panel etc.)

#### Code
    -   django-admin startapp products
    -   python manage.py startapp profiles
    -   python manage.py makemigrations
    -   python manage.py migrate
    -   python manage.py shell
        -   from products.models import Product
        -   Product.objects.create(title='Raspberry Pi')
        -   Product.objects.get(id=1)
        -   Product.objects.get(id=2)
        -   obj = Product.objects.get(id=1)
        -   obj.content = 'this is content for content field'
        -   obj.save()
        -   obj.delete()

#### Bulk creating the product
    -   Product.objects.bulk_create([
            Product(title='This is a test'),
            Product(title='This is only a test'),
        ])


### Day 2
    -   python manage.py shell
        -   from products.models import Product
        -   obj = Product.objects.get(id=1)
        -   qs = Product.objects.all()
    -   Model -> migrate -> Url -> Views


### Day 3
    -   3 Formats of String substitution
        -   name = "Jack"
        -   sub1 = f"Hello {name}"
        -   sub2 = "Hello {name}".format(name=name)
        -   sub3 = "Hello %s" % (name)

### Day 4

#### Add / Update data in your database without the Django
    -   Http Methods
        -   Post    -   Create
        -   Get     -   Retrieve
        -   Put     -   Update
        -   Delete  -   Destroy

#### Django Forms Validation
    -   Django Form
    -   Django ModelForm
