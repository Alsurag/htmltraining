from textnode import TextNode, TextType

def main():
    node = TextNode("Some Text", TextType.NORMAL_TEXT, "https://example.com")
    print (node)

if __name__ == "__main__":
    main()
