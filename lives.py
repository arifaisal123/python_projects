def generate_image(num):
    """
    Takes number as input, return an image as string.
    """
    if num == 7:
        return """
          +---+
              |
              |
              |
              |
              |
        =========
        """
    elif num == 6:
        return """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """
    elif num == 5:
        return """
          +---+
          |   |
          0   |
              |
              |
              |
        =========
        """
    elif num == 4:
        return """
          +---+
          |   |
          0   |
          |   |
              |
              |
        =========
        """
    elif num == 3:
        return """
          +---+
          |   |
          0   |
          |\  |
              |
              |
        =========
        """
    elif num == 2:
        return """
          +---+
          |   |
          0   |
         /|\  |
              |
              |
        =========
        """
    elif num == 1:
        return """
          +---+
          |   |
          0   |
         /|\  |
         /    |
              |
        =========
        """
    elif num == 0:
        return """
          +---+
          |   |
          0   |
         /|\  |
         / \  |
              |
        =========
        """
    