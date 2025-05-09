def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Format the input text with optional prefix, suffix, capitalization, and max_length.

    Parameters:
        text (str): The input text to be formatted.
        prefix (str, optional): String to add at the beginning of the text. Default is "".
        suffix (str, optional): String to add at the end of the text. Default is "".
        capitalize (bool, optional): Whether to capitalize the text. Default is False.
        max_length (int, optional): Maximum length of the final string. Default is None.

    Returns:
        str: The formatted string.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If max_length is non-positive.

    Example:
        > format_text("hello", prefix=">>", suffix="<<")
        '>>hello<<'
    """
    # Validate input types
    if not isinstance(text, str):
        raise TypeError("The 'text' parameter must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' parameter must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' parameter must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' parameter must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' parameter must be an integer.")
        if max_length <= 0:
            raise ValueError("The 'max_length' parameter must be a positive integer.")

    # Capitalize text if required
    if capitalize:
        text = text.capitalize()

    # Add prefix and suffix
    formatted = f"{prefix}{text}{suffix}"

    # Apply length restriction if max_length is specified
    if max_length is not None:
        formatted = formatted[:max_length]

    return formatted


# Test the function
if __name__ == "__main__":
    try:
        print(format_text("hello", max_length=10))
        print(format_text("dinah", prefix=">>", suffix="<<", capitalize=True, max_length=9))
        print(format_text("mbabazi", prefix=">>", suffix="<<", capitalize=True, max_length=11))
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
