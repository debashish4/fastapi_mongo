# test

test desc

## Setting up

1. Create a virtual environment
    ```bash
    python3 -m venv myenv
    ```
    or
    ```bash
    # If you have virtualenv installed

    virtualenv -p python3 myenv
    ```

2. Activate the virtual environment
    ```bash
    source ./myenv/bin/activate
    ```

3. Install all dependency
    ```bash
    pip intall -r requirements.txt
    ```

4. Run the development web server
    ```bash
    python manage.py runserver
    ```

5. Run unit tests
    ```bash
    python manage.py test
    ```


# Setup project using docker

1. Create Docker image
    ```sh
    $ sudo docker build -t yourimagename .
    ```
2. Run Docker Container
    ```sh
    $ sudo docker run -v "$(pwd)"/logs/:/test/logs -it --name yourcontainername -p 8000:8000 yourimagename
    ```
# And then open it at browser
   http://127.0.0.1:8000/

# Check swagger Api's
   http://127.0.0.1:8000/api/v1/docs

# Check Swagger Documentation
   http://127.0.0.1:8000/api/v1/redoc
