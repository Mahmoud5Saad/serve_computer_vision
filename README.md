# serve_computer_vision

This is a repo in which we deploy a computer vision model for face detection and drawing bounding boxes on top of FastAPI then containerize them.

To use it you only have to build the container:

```bash
$ docker build -t myimage .
```

Then run it:

```bash
$ docker run -d --name mycontainer -p 8000:8000 myimage
```

Then it is only a matter of reaching for this API with

```bash
http://localhost:8000/docs
```

to be able to send requests to this backend
