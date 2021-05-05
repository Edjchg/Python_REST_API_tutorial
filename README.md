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

### Endpoints 

Firts of all, we need to set the endpoints or the path to access the API. The way it is done with Python es like is shown at line 27:
```python
@main_api.route('/', methods=['GET'])
```
In this case, the path to access the functionality from the function
```python
def api_home():
```
is by going to the browser access that path.

### Methods

Like we explained before, there are some methods in a REST API, that are **GET**, **PUT**, **PUSH**, **DELETE**.

We specify that certain resource is obtained by one of this methods by declaring it like this example:

```python
@main_api.route('/', methods=['GET'])
```
Then you can see that we specify the resource method by typing 'GET', or whatever you want to delcare.

- **GET: **
For example, we have a list of books in the code shown in this repository. In order to access this resource from a browser, you need to execute a **GET**, and in that way you will be able to access that information:


When you need a certain element from a set of resources, in this case imagine that you need the only the first book from that JSON. In order to access this element is by passing the id through the URL when you execute a GET from the browser. 

```python
ide = int(request.args['id'])
```
The previous line shows the way we are getting that parameter.


- **PUT**
- **PUSH**
- **DELETE: **
When you want to delete some resource available in the API, this is the method you need to achieve that goal.

### Executing this little REST API example

Download the code from this repository by doing:

```sh
$ git clone https://github.com/Edjchg/Python_REST_API_tutorial
```
This command will create a directory called Python_REST_API_tutorial. So, go there by doing:

```sh
$ cd Python_REST_API_tutorial
```
In that repository, the only thing you need to do is to execute the python script by doing:

```sh
$ python3 api_hello_world.py
```
In Windows, just type:

```sh
$ python api_hello_world.py
```

If you have Pycharm, then just click the Play Button.


After this, you will see on the terminal something like this:

|![](images/img1.PNG)|
|:--:|
|**Figure 1**: The URL where the API is available.|

If you click over this link, then you will be able to see something like this:


|![](images/img2.PNG)|
|:--:|
|**Figure 2**: The API response seen from the browser.|

After this, by adding elements to the URL you will be able to access the REST API from the browser


For example, to get all the books available in the API, then just add to the URL:

```sh
http://127.0.0.1:5000/resources/books/all
```

You will get something like this:

|![](images/img3.PNG)|
|:--:|
|**Figure 3**: The API response after requesting all the books.|


But if you want to request or delete a certain book, then add to the URL something like the following:

```sh
http://127.0.0.1:5000/resources/book?id=<id of the book you want to request>
```

|![](images/img4.PNG)|
|:--:|
|**Figure 3**: The API response after requesting a certain the book.|














