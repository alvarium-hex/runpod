## Runpod Serverless inference
Based upon https://github.com/runpod/serverless-workers/blob/main/workers/huggingface-transformers/README.md

## Building

Select one of the following models to build:

- `gpt-neo-1.3B`
- `gpt-neo-2.7B`
- `gpt-neox-20b`
- `pygmalion-6b`
- `gpt-j-6b`
- `falcon-7b-instruct`
- `falcon-40b-instruct`

```BASH
docker build --build-arg MODEL_NAME={model name} -t repo/image_name:tag .
```