#!/usr/bin/env python3
"""
Morse Code Ambiguity Decoder

Takes a sequence of dots (.) and dashes (-) without spaces and finds
all possible words/letter combinations that can be formed by inserting
spaces at different positions.
"""

# Morse code mapping
MORSE_TO_LETTER = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
}

# Reverse mapping: letter to morse
LETTER_TO_MORSE = {v: k for k, v in MORSE_TO_LETTER.items()}

# Maximum length of any morse code sequence (for optimization)
MAX_MORSE_LEN = max(len(code) for code in MORSE_TO_LETTER.keys())


def word_to_morse(word: str, with_spaces: bool = True) -> str | None:
    """
    Convert an English word to morse code.

    Args:
        word: The word to convert (letters and numbers only)
        with_spaces: If True, separate letters with spaces

    Returns:
        Morse code string, or None if word contains invalid characters
    """
    word = word.upper()
    morse_parts = []

    for char in word:
        if char in LETTER_TO_MORSE:
            morse_parts.append(LETTER_TO_MORSE[char])
        elif char == ' ':
            continue  # Skip spaces in input
        else:
            return None  # Invalid character

    separator = ' ' if with_spaces else ''
    return separator.join(morse_parts)


def find_all_decodings(morse_sequence: str) -> list[str]:
    """
    Find all possible letter combinations from a spaceless morse sequence.

    Uses dynamic programming/memoization to efficiently find all valid splits.

    Args:
        morse_sequence: A string of dots and dashes without spaces

    Returns:
        List of all possible decoded strings
    """
    memo = {}

    def decode_from(start: int) -> list[str]:
        """Recursively find all decodings starting from position 'start'."""
        if start == len(morse_sequence):
            return ['']

        if start in memo:
            return memo[start]

        results = []
        # Try all possible morse code lengths from current position
        for end in range(start + 1, min(start + MAX_MORSE_LEN + 1, len(morse_sequence) + 1)):
            segment = morse_sequence[start:end]

            if segment in MORSE_TO_LETTER:
                letter = MORSE_TO_LETTER[segment]
                # Get all possible continuations
                continuations = decode_from(end)
                for cont in continuations:
                    results.append(letter + cont)

        memo[start] = results
        return results

    return decode_from(0)


def decode_with_splits(morse_sequence: str) -> list[tuple[str, list[str]]]:
    """
    Find all decodings and show how the morse was split.

    Returns:
        List of tuples: (decoded_word, list_of_morse_segments)
    """
    results = []

    def backtrack(start: int, current_letters: list[str], current_segments: list[str]):
        if start == len(morse_sequence):
            results.append((''.join(current_letters), current_segments.copy()))
            return

        for end in range(start + 1, min(start + MAX_MORSE_LEN + 1, len(morse_sequence) + 1)):
            segment = morse_sequence[start:end]

            if segment in MORSE_TO_LETTER:
                letter = MORSE_TO_LETTER[segment]
                current_letters.append(letter)
                current_segments.append(segment)
                backtrack(end, current_letters, current_segments)
                current_letters.pop()
                current_segments.pop()

    backtrack(0, [], [])
    return results


def load_dictionary(filepath: str = None) -> set[str]:
    """Load a word dictionary for filtering valid words."""
    if filepath:
        try:
            with open(filepath, 'r') as f:
                return set(word.strip().upper() for word in f)
        except FileNotFoundError:
            print(f"Dictionary file not found: {filepath}")

    # Try common dictionary locations
    common_paths = [
        '/usr/share/dict/words',
        '/usr/share/dict/american-english',
    ]

    for path in common_paths:
        try:
            with open(path, 'r') as f:
                return set(word.strip().upper() for word in f)
        except FileNotFoundError:
            continue

    return set()


def filter_valid_words(decodings: list[str], dictionary: set[str]) -> list[str]:
    """Filter decodings to only include valid dictionary words."""
    return [word for word in decodings if word in dictionary]


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Decode ambiguous morse code sequences',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s ".-"              # Simple: decodes to A
  %(prog)s "..."             # Ambiguous: S, EI, IE, EEE
  %(prog)s "-.-" --show      # Show morse splits
  %(prog)s "..." --words     # Only show dictionary words
  %(prog)s --encode "HELLO"  # Convert word to morse, find variations
  %(prog)s -e "CAT" --words  # Find valid word variations for CAT
        '''
    )
    parser.add_argument('morse', nargs='?', help='Morse code sequence (dots and dashes only)')
    parser.add_argument('--encode', '-e', metavar='WORD',
                        help='Encode a word to morse and find all variations')
    parser.add_argument('--show', '-s', action='store_true',
                        help='Show how morse is split for each decoding')
    parser.add_argument('--words', '-w', action='store_true',
                        help='Only show valid dictionary words')
    parser.add_argument('--dict', '-d', metavar='FILE',
                        help='Path to dictionary file')
    parser.add_argument('--limit', '-l', type=int, default=100,
                        help='Maximum results to show (default: 100)')

    args = parser.parse_args()

    # Handle encode mode
    if args.encode:
        word = args.encode.strip().upper()
        morse_spaced = word_to_morse(word, with_spaces=True)
        morse = word_to_morse(word, with_spaces=False)

        if morse is None:
            print(f"Error: '{args.encode}' contains invalid characters (use letters/numbers only)")
            return 1

        print(f"Word: {word}")
        print(f"Morse (spaced): {morse_spaced}")
        print(f"Morse (combined): {morse}")
        print(f"Length: {len(morse)} symbols\n")
    else:
        if not args.morse:
            parser.print_help()
            return 1

        # Validate input
        morse = args.morse.strip()
        if not all(c in '.-' for c in morse):
            print("Error: Input must contain only dots (.) and dashes (-)")
            return 1

        if not morse:
            print("Error: Empty input")
            return 1

        print(f"Input: {morse}")
        print(f"Length: {len(morse)} symbols\n")

    if args.show:
        results = decode_with_splits(morse)

        if args.words:
            dictionary = load_dictionary(args.dict)
            if dictionary:
                results = [(word, splits) for word, splits in results if word in dictionary]
            else:
                print("Warning: No dictionary loaded, showing all results\n")

        total = len(results)
        print(f"Found {total} possible decoding(s):\n")

        for i, (word, splits) in enumerate(results[:args.limit]):
            split_str = ' '.join(splits)
            print(f"  {word:20} <- {split_str}")

        if total > args.limit:
            print(f"\n  ... and {total - args.limit} more (use --limit to see more)")
    else:
        results = find_all_decodings(morse)

        if args.words:
            dictionary = load_dictionary(args.dict)
            if dictionary:
                results = filter_valid_words(results, dictionary)
            else:
                print("Warning: No dictionary loaded, showing all results\n")

        total = len(results)
        print(f"Found {total} possible decoding(s):\n")

        for word in results[:args.limit]:
            print(f"  {word}")

        if total > args.limit:
            print(f"\n  ... and {total - args.limit} more (use --limit to see more)")

    return 0


if __name__ == '__main__':
    exit(main())
