# Word Matches

## How to run

#### 1. Install Dependencies

Run the following command to install necessary dependencies

```bash
pip3 install -r requirements.txt
```

#### 2. Run the Program

```bash
python3 main.py <PREDEFINED_WORDS_FILE> <INPUT_FILE>
```

- `PREDEFINED_WORDS_FILE`, `INPUT_FILE` are relative paths from the current directory.

## What has been tested

- The program was initially tested with the provided sample list of words and lines.

- To test with larger files, I downloaded words from [this repo](https://github.com/dwyl/english-words/blob/master/words.txt)
  and text file from [this](https://raw.githubusercontent.com/dscape/spell/master/test/resources/big.txt).
- Checked the word counts for "delight" ,"constantly" etc., and the output count matched the find text tool count in my IDE.

## Assumptions

- Special Characters in Words
  - Words with special characters in between are not matched. For example, text containing `John's` will not match for a predefined word: `John`.
- Word Seperation
  - Words are assumed to be separated by spaces, although they may contain special characters at the beginning or end.
- Zero matches
  - Words with zero matches are not shown in the output.

## Output

- The output is written to the console and also saved to a file named `output.txt` for better visibility if list is huge.
