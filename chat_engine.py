# Importing the VectorStoreIndex and SimpleDirectoryReader classes from the llama_index module
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')
# The data_dir variable is used to specify the directory from which the text data will be loaded.
# Set the directory path where the text data is located
data_dir = "data"
# Dictionary to store the indexes
index_dict = {}  
# Iterate over the files in the directory
filenames = sorted(os.listdir(data_dir))
for filename in filenames:
    file_path = os.path.join(data_dir, filename)
    
    # Create a separate index for each file
    reader = SimpleDirectoryReader(input_files=[file_path])
    data = reader.load_data()
    index = VectorStoreIndex.from_documents(data)
    index_dict[filename] = index

# Create separate chat engines for each index
chat_engine_dict = {}
for filename, index in index_dict.items():
    chat_engine = index.as_chat_engine(chat_mode='react', verbose=True)
    chat_engine_dict[filename] = chat_engine
#Display all available engines
print("Available engines:")
for i, filename in enumerate(chat_engine_dict.keys()):
    print(f"{i+1}. {filename}")

# Prompt user to select the engine
selected_index = int(input("Select the engine (1, 2, 3, ...): "))
selected_filename = list(chat_engine_dict.keys())[selected_index - 1]
selected_chat_engine = chat_engine_dict[selected_filename]

# Initialize a flag to control the loop
continue_interaction = True

while continue_interaction:
    # Prompt user to enter the question
    question = input("Enter your question (type 'quit' to end): ")
    
    # Check if the user wants to quit
    if question.lower() == 'quit':
        continue_interaction = False
        continue # Skip the rest of the loop iteration
    
    # Chat with the selected chat engine
    response = selected_chat_engine.chat(question)
    print(f"Response from {selected_filename}: {response}")

print("Chat session ended")