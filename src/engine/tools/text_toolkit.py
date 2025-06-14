from .base import BaseTool
import unicodedata

class TextToolkit(BaseTool):
    
    def normalize(self, text: str, keep_whitespace: bool = False) -> str:
        """
        Normalize a string for fuzzy matching or comparison:
        - Converts Unicode to normalized NFKC form
        - Strips punctuation
        - Converts to lowercase
        - Collapses all whitespace
        """
        delimiter = " " if keep_whitespace else ""
        return delimiter.join(self.tokenize(text))

    def tokenize(self, text: str) -> list[str]:
        unicode_normalized = self.normalize_unicode(text)
        stripped_punctuation = self.strip_punctuation(unicode_normalized)
        
        return stripped_punctuation.lower().strip().split()


    def strip_punctuation(self, text: str) -> str:
        return self.tools.regex.sub(
            pattern=self.tools.regex.common_patterns.PUNCTUATION, 
            repl="", 
            text=text
        )
    
    def normalize_unicode(self, text: str) -> str:
        """
        Converts text to Unicode NFKC form.

        This flattens weird or invisible characters like:
        - Zero-width space (U+200B)
        - Non-breaking space (U+00A0)
        - Full-width characters (e.g. Ａ → A)
        - Ligatures or symbol-like characters (e.g. ① → 1)

        Useful for matching text from PDFs, web data, or user input.
        """
        return unicodedata.normalize("NFKC", text)