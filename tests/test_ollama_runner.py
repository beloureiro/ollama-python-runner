import unittest
from src.ollama_runner import run_ollama

class TestOllamaRunner(unittest.TestCase):
    def test_run_ollama(self):
        output = run_ollama('llama3.1:8b')
        self.assertTrue(output.startswith("Model output"))
