# Define a class to analyze text
class TextAnalyzer(object):

    def __init__(self, text):
        # Remove punctuation from the input text
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # Convert all text to lowercase to ensure consistency (e.g., "Lorem" and "lorem" are treated the same)
        formattedText = formattedText.lower()

        # Store the cleaned/formatted text as an instance variable
        self.fmtText = formattedText

    def freqAll(self):
        # Split the formatted text into a list of words
        wordList = self.fmtText.split(' ')

        # Initialize an empty dictionary to store word frequencies
        freqMap = {}

        # Loop over the unique words only using set() to avoid counting the same word multiple times
        for word in set(wordList):
            # Count how many times the word appears in the list
            freqMap[word] = wordList.count(word)

        # Return the dictionary containing word frequencies
        return freqMap

    def freqOf(self, word):
        # Get the full frequency map of all words
        freqDict = self.freqAll()

        # Return the frequency of the specific word if it exists in the map
        if word in freqDict:
            return freqDict[word]
        else:
            # If the word is not found, return 0
            return 0


# Sample input text with punctuation and mixed case
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Create an instance of TextAnalyzer using the sample text
analyzed = TextAnalyzer(givenstring)

# Print the cleaned/formatted text (punctuation removed, lowercase)
print("Formatted Text:", analyzed.fmtText)

# Get the frequency map of all words and print it
freqMap = analyzed.freqAll()
print(freqMap)

# Choose a word to find its frequency
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word", word, "appears", frequency, "times.")
