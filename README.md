# Django simple_settings

simple_settings is a simple and a reusable Django application for providing a simple *Site Settings* model that has only one instance which is available via a template tag

## Quick start
0. Copy the `simple_settings` folder to your Django project

1. Add "simple_settings" to your INSTALLED_APPS setting like this
    ```python
    INSTALLED_APPS = [
        ...
        'simple_settings',
    ]
    ```
2. Include `simple_settings.context_processors.settings` into the template context processors inside your **settings.py**

    ```python
    TEMPLATES = [
        {
        ...
            'OPTIONS': {
            ...
                'context_processors': [
                    'simple_settings.context_processors.settings',
                ...
                ],
            },
        },
    ]
    ```
3. Run `python manage.py makemigrations && python manage.py migrate` to create the simple_settings model.

4. Start the development server and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) you will find the new `Site Settings` application that you can only edit.

5. To use these settings in your templates, just include `{{ settings.FIELD_NAME }}`, for example: 
    ```html
        <div>
            <h2>About us</h2>
            <p>{{settings.about_us}}</p>
        </div>
    ```

6. To costumize your site settings, go to `simple_settings/models.py` and add your fields then run `python manage.py makemigrations && python manage.py migrate` again

## Thanks to
* [Singleton Design Pattern Example: Singleton Models in Django](https://steelkiwi.com/blog/practical-application-singleton-design-pattern/)
* [Answer: Django admin: redirect to object change page if only one exists in list](https://stackoverflow.com/a/45909391/5078746?stw=2)
