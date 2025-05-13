from abc import ABC, abstractmethod
#Abstract component
class TextComponent:
    _text = None
    @abstractmethod
    def render(self):
        return NotImplementedError

#Decorator abstract class
class TextDecorator(TextComponent):
    def __init__(self, text_component:TextComponent):
        self._text_component = text_component

    @abstractmethod
    def render(self):
        return NotImplementedError

#Concrete Component : PlainText
class PlainText(TextComponent):
    def __init__(self, text:str):
        self._text = text

    def render(self):
        return self._text


#Decorator : BoldText
class Bold(TextDecorator):
    def render(self):
        return f"<b>{self._text_component.render()}</b>"
#Decorator : ItalicText
class Italic(TextDecorator):
    def render(self):
        return f"<i>{self._text_component.render()}</i>"
#Decorator : UnderlineText
class Underline(TextDecorator):
    def render(self):
        return f"<u>{self._text_component.render()}</u>"
#Decorator : StrikethroughText
class Strikethrough(TextDecorator):
    def render(self):
        return f"<s>{self._text_component.render()}</s>"
#Decorator : HighlightText
class Highlight(TextDecorator):
    def render(self):
        return f"<mark>{self._text_component.render()}</mark>"
#Decorator : SuperscriptText
class Superscript(TextDecorator):
    def render(self):
        return f"<sup>{self._text_component.render()}</sup>"
    
if __name__ == "__main__":
    # Create a plain text component
    plain_text = PlainText("Hello, World!")
    print(plain_text.render())  # Output: Hello, World!

    # Decorate the plain text with bold and italic
    bold_text = Bold(plain_text)
    italic_text = Italic(bold_text)
    print(italic_text.render())  # Output: <i><b>Hello, World!</b></i>

    # Further decorate with underline
    underline_text = Underline(italic_text)
    print(underline_text.render())  # Output: <u><i><b>Hello, World!</b></i></u>

    print("Decorating with multiple decorators:")
    # Create a new plain text component
    another_plain_text = PlainText("Python Decorator Pattern")
    # Decorate with multiple decorators
    decorated_text = Bold(Italic(Underline(Strikethrough(another_plain_text))))
    print(decorated_text.render())  # Output: <b><i><u><s>Python Decorator Pattern</s></u></i></b>