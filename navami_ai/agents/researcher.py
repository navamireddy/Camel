from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType


def create_researcher():
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OLLAMA,
        model_type="llama3.2",
        url="http://localhost:11434/v1",
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