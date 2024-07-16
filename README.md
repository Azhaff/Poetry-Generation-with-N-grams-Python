## Poetry Generation with N-grams

### Overview
This project explores natural language processing (NLP) techniques to generate creative and expressive poetry. The goal is to construct three stanzas, each comprising four verses with 7 to 10 words per verse. The generated poem aims to exhibit technical proficiency while evoking emotions and imagery, inspired by the styles of renowned poets William Shakespeare and Maya Angelou.

### Features
- **Unigram, Bigram, and Trigram Models**: The project uses N-gram models to predict and generate words, ensuring the generated verses are coherent and stylistically similar to the chosen poet.
- **Random Verse Length**: Each verse has a length between 7 and 10 words, adding variability and natural flow to the generated poetry.
- **User Input for Poet Style**: The user can select between the styles of William Shakespeare and Maya Angelou, influencing the vocabulary and structure of the generated poem.

### How It Works

1. **Load and Tokenize Corpus**: The script reads text files containing the works of the chosen poets and tokenizes the text into words.
2. **Generate N-gram Models**: Using the tokenized words, unigram, bigram, and trigram models are generated using NLTK's `ConditionalFreqDist`.
3. **Generate Verses and Stanzas**: For each stanza, four verses are generated using the N-gram models. Each verse's length is randomly determined within the specified range.
4. **User Input and Poem Generation**: The user is prompted to choose a poet's style, and the script generates and prints three stanzas using the selected style.

### File Structure
- `shakespeare.txt`: Text file containing works by William Shakespeare.
- `angelou.txt`: Text file containing works by Maya Angelou.
- `poetry_generation.py`: Python script implementing the N-gram models and poetry generation logic.

### Prerequisites
- Python 3.x
- NLTK library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/poetry-generation-ngram.git
   ```
2. Navigate to the project directory:
   ```bash
   cd poetry-generation-ngram
   ```
3. Install the required libraries:
   ```bash
   pip install nltk
   ```

### Usage
1. Ensure the text files `shakespeare.txt` and `angelou.txt` are in the project directory.
2. Run the script:
   ```bash
   python poetry_generation.py
   ```
3. Follow the prompt to select the poet style (Shakespeare/Angelou).

### Example Output
```plaintext
In which style do you want to generate the poem? (Shakespeare/Angelou): Shakespeare
Unigram Model Stanza:

Upon a time the heavens did sing
With spirits bright and lights agleam
In twilight's gentle, whispering wing
A dream awoke, in night serene


Bigram Model Stanza:

To sleep, perchance to dream. Ay, there's the rub,
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect.


Trigram Model Stanza:

Now is the winter of our discontent
Made glorious summer by this sun of York;
And all the clouds that lour'd upon our house
In the deep bosom of the ocean buried.
```

### Challenges and Enhancements
- **Word Prediction**: Selecting subsequent words involves predicting the most probable next word based on the N-gram model.
- **Rhyming**: Future enhancements could include a rhyming dictionary to add artistic quality to the generated verses.
- **Comparison of Models**: The generated stanzas using unigram, bigram, and trigram models provide a comparison of their effectiveness in creating coherent poetry.

### Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or new features.
