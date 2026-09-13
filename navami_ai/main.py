from agents.researcher import create_researcher


def main():
    researcher = create_researcher()

    topic = input("Enter a research topic: ")

    response = researcher.step(
        f"Research and explain this topic clearly: {topic}"
    )

    print("\n===== NAVAMI AI RESEARCHER =====\n")
    print(response.msgs[0].content)


if __name__ == "__main__":
    main()