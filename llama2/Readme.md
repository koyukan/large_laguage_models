# Changing model to quantized version of Llama2 ("TheBloke/Llama-2-7B-Chat-GPTQ")

- The original model is available at [TheBloke/Llama-2-7B-Chat-GPTQ](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GPTQ)

- Added requisite dependencies to the requirements.txt file
- Added necessary params to model_loader.py etc.
- Changed the concurrency of the Celery worker to 1


# Test the model without containerization

- Create a virtual environment
```bash
python3 -m venv venv
```
- Activate the virtual environment
```bash
source venv/bin/activate
```
- Install the requirements
```bash
pip install -r requirements.txt
```

- Start the Celery worker
```bash
celery -A celery_worker worker -c 1 --loglevel=debug
```

- Open another terminal activate the virtual environment and start the FastAPI server
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
- Run the run.py file to test the model
```bash
python run.py
```
# Build the Docker image

- Build the Docker image
```bash
docker compose up
```

Note: this will build the Docker image and start the FastAPI server and Celery worker in the container however the Celery worker will not be able to connect to use the GPU as the Docker container does not have access to the GPU. I will try to find a remedy for this.

```bash
 used in the `LlamaAttention` class
llama2-worker-1  | [2024-03-28 19:13:42,446: ERROR/ForkPoolWorker-1] Signal handler <function setup_model at 0x77219c10d4c0> raised: ValueError('Found modules on cpu/disk. Using Exllama or Exllamav2 backend requires all the modules to be on GPU.You can deactivate exllama backend by setting `disable_exllama=True` in the quantization config object')

```