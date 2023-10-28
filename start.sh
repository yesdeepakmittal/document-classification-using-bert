#!/bin/bash

python modeling_service/services/app.py &
uvicorn modeling_service.services.modeling:app --reload --host 0.0.0.0 --port 8000