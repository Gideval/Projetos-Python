from pathlib import Path

class PromptLoader:
    PROMPTS_DIR = Path(__file__).parent / "prompts"

    @classmethod
    def load(cls, filename: str) -> str:
        with open(cls.PROMPTS_DIR / filename, encoding="utf-8") as file:
            return file.read()