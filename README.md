# Chat Engine

This project demonstrates how to perform chat-like interactions with multiple indexes using the `llama_index` library. The code allows users to create separate indexes for each text file in a directory and interact with each index using a chat-like interface.

## Prerequisites

- Python 3.x
- Required libraries (specified in `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Change the present working directory to the cloned repository:
   ```bash
   cd your-repository-path
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

1. Place your text files in the ../data/ directory.

2. Run the script

3. Follow the on-screen instructions to select an engine and ask questions.

## Features

- Supports multiple indexes, with each index corresponding to a single text file.

- User-friendly chat-like interface for interacting with each index.

## Sample questions

#### For Engine corresponding to CHAPTER I
- What is the conclusion of chapter I?
- The summary of chapter I discusses the intellectual development of a child, focusing on the evolution of general ideas, the role of gestures as a precursor to speech, and the origins of language. It contrasts theories on whether individuals start with general terms or particulars and emphasizes the importance of creative imagination and early language acquisition. Examples of abstraction and generalization in infants before they develop speech are highlighted.

#### For Engine corresponding to CHAPTER III
- How does the Romanes describes the passage from the generic image to the concept?
- Romanes describes the passage from the generic image to the concept by explaining how water-fowl and humans perceive and interact with their surroundings differently. He illustrates that animals like water-fowl have recepts for solid substances and fluids, while humans have recepts for solid ground and unresisting fluids. Unlike water-fowl, humans can assign names to these recepts, elevating them to the level of concepts. This ability to assign names to ideas known as concepts is a crucial step in the transition from generic images to concepts.
#### For Engine corresponding to CHAPTER V
- What is the main focus of the passage "Section III. The Concept of Time"?
- The main focus of the passage "Section III. The Concept of Time" is on the development and evolution of the concept of time from a primitive understanding to a more abstract and conceptualized form. It discusses how early humans relied on concrete markers and natural phenomena to grasp the passage of time, gradually progressing towards a more sophisticated understanding through the observation of regular natural phenomena like the movements of celestial bodies. The passage also touches upon the subjective nature of our perception of time, the distinction between real and conceptual infinity, and the role of consciousness in shaping our understanding of time.

## Note 
- You need OpenAI_API_KEY to use this script
