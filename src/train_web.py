from llmtuner import create_ui


def main(share=True):
    demo = create_ui()
    demo.queue()
    demo.launch(server_name="0.0.0.0", share=share, inbrowser=True)


if __name__ == "__main__":
    main()
