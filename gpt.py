import requests

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM





class GPT:

    def __init__(self, system_content=""):

        self.system_content = system_content

        self.URL = 'http://localhost:600/v1/chat/completions'

        self.HEADERS = {"Content-Type": "application/json"}

        self.MAX_TOKENS = 100

        self.assistant_content = "Решим задачу по шагам: "

    @staticmethod
    def count_tokens(prompt):

        tokenizer = AutoTokenizer.from_pretrained("NousResearch/Hermes-3-Llama-3.2-3B")
        model = AutoModelForCausalLM.from_pretrained("NousResearch/Hermes-3-Llama-3.2-3B")

        return len(tokenizer.encode(prompt))

    def process_resp(self, response) -> [bool, str]:

        if response.status_code < 200 or response.status_code >= 300:
            self.clear_history()

            return False, f"Ошибка: {response.status_code}"

        try:

            full_response = response.json()

        except:

            self.clear_history()

            return False, "Ошибка получения JSON"

        if "error" in full_response or 'choices' not in full_response:
            self.clear_history()

            return False, f"Ошибка: {full_response}"

        result = full_response["choices"][0]["message"]["content"]

        self.save_history(result)

        return True, self.assistant_content

    def make_prompt(self, user_request):

        json_gpt = {

            "messages": [

                {"role": "user", "content": user_request}

            ],

            "temperature": 1.2,

            "max_tokens": self.MAX_TOKENS

        }

        return json_gpt

    def send_request(self, json_gpt):

        resp = requests.post(url=self.URL, headers=self.HEADERS, json=json_gpt)

        return resp

    def save_history(self, content_response):

        self.assistant_content += content_response

    def clear_history(self):

        self.assistant_content = "Решим задачу по шагам: "