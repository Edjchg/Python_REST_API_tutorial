# Python REST API tutorial
*by Andrey Garro(@AndreyGarro) & Edgar Chaves(@Edjchg)*

### Some dependencies before start:

- Python 3.5 or grater
- Flask

## Installing Flask:

If you do not have Pycharm then execute the following commands:

```sh
pip install flask
```
If you are using Ubuntu or some flavor of Linux install:

```sh
pip install uwsgi flask
```

If you have successfully install those dependencies, it is time to start.

## Understanding the previous code

We are going to implement almost all the available methods of a REST API.


```python
@main_api.route('/', methods=['GET'])
```

