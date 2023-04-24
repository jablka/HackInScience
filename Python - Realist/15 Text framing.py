from dataclasses import dataclass

@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    text_container = text.split(sep='\n')
    # print(text_container)
    max_size = len(max(text_container, key=lambda x:len(x))) 
    # print(max_size)
    buffer = [ ]
    for n, line in enumerate(text_container):
        if n==0:
            s = frame.top_left + max_size*frame.top + frame.top_right
            buffer.append(s)
        
        line_ = line.ljust(max_size)
        s = frame.left + line_ + frame.right
        buffer.append(s)

        if n==len(text_container)-1: # last line in text_container
            s = frame.bottom_left + max_size*frame.bottom + frame.bottom_right
            buffer.append(s)

    text = "\n".join(buffer)
    return text
