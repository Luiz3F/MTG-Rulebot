from langchain_text_splitters import MarkdownHeaderTextSplitter

def main():
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]
    input_file = 'comp_rules\\actually_correct_comp_rules.md'#'..\\comp_rules\\actually_correct_comp_rules.md'    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(text)
    print(md_header_splits[8])

if __name__ == '__main__':
    main()