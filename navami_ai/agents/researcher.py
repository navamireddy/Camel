from dotenv import load_dotenv

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

load_dotenv()


def create_researcher():
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
        model_config_dict={
            "temperature": 0.2,
        },
    )

    researcher = ChatAgent(
        system_message=(
            "You are a research assistant. "
            "Analyze the user's research topic, identify important concepts, "
            "and organize the information clearly."
        ),
        model=model,
    )

    return researcher