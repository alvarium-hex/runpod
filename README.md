## Runpod Serverless inference
Based upon https://github.com/runpod/serverless-workers/blob/main/workers/huggingface-transformers/README.md

## Building

Select one of the following models to build:

- `falcon-7b-instruct`
- `falcon-40b-instruct`
- `starcoder`
- `wizardcoder`

```BASH
docker build --build-arg MODEL_NAME={model name} -t repo/image_name:tag .
```

### Github Actions
The docker containers are also available in the packages of this repository.  
The build seems to flake out every now and then. Unsure why this is happening.

[![Docker](https://github.com/alvarium-hex/runpod/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/alvarium-hex/runpod/actions/workflows/docker-publish.yml)

## Requirements
Running a model requires that the model git repository is downloaded on the root a networked volume.  
The folder name has to match the model name

e.g. when using the starcoder model
the /runpod-volume is the mount location of the networked volume
```
/runpod-volume/starcoder
```
