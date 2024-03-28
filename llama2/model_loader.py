import os
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer
from dotenv import load_dotenv

load_dotenv()


class ModelLoader:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.config = AutoConfig.from_pretrained(
            self.model_path,
            trust_remote_code=True,
            
        )
        self.model = self._load_model()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path,use_fast=True)

    def _load_model(self):
        model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            config=self.config,
            trust_remote_code=True,
            revision="main",
            device_map="auto",  
        )
        return model
