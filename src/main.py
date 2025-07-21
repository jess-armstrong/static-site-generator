from textnode import TextNode, TextType

def main():
    node = TextNode("Anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()