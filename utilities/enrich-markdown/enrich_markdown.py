import os
import sys
import argparse
import concurrent.futures
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

# --- Model Imports ---
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def get_model_chain(provider="gemini"):
    """
    Factory function to get the model and output parser chain
    based on the selected provider.
    """
    if provider == "gemini":
        if not os.getenv("GOOGLE_API_KEY"):
            print("Error: GOOGLE_API_KEY not found in environment variables.", file=sys.stderr)
            sys.exit(1)
        model = ChatGoogleGenerativeAI(model="models/gemini-pro-latest", temperature=0)
    
    elif provider == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY not found in environment variables.", file=sys.stderr)
            sys.exit(1)
        model = ChatOpenAI(model="gpt-4o", temperature=0)
        
    elif provider == "anthropic":
        if not os.getenv("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
            sys.exit(1)
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0)
        
    else:
        print(f"Error: Unknown model provider '{provider}'", file=sys.stderr)
        sys.exit(1)

    output_parser = StrOutputParser()
    return model | output_parser

# --- System Prompt ---
system_prompt = """
Please convert the following text into beautifully structured markdown. 
Do not edit the text itself and keep it as the original.
Please return the full document without ommitting elements. 
Do not return anything except the perfectly structured markdown.
"""

# --- Processing Function (for each thread) ---
def process_chunk(chunk_text: str, chunk_index: int, chain) -> str:
    """
    Sends a single chunk to the LLM chain.
    """
    print(f"--- Processing chunk {chunk_index+1}... ---")
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Here is the document:\n\n{chunk_text}")
    ]
    
    try:
        result = chain.invoke(messages)
        return result
    except Exception as e:
        print(f"Error on chunk {chunk_index+1}: {e}", file=sys.stderr)
        return chunk_text # Return original text on failure

# --- Main Concurrent Execution ---
def main():
    # --- 1. Load .env and Parse Arguments ---
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="Enrich standard FinancialReports markdown using an LLM.")
    parser.add_argument("--input-file", required=True, help="Path to the standard .md file to enrich.")
    parser.add_argument("--output-file", required=True, help="Path to save the enriched .md file.")
    parser.add_argument(
        "--model", 
        default="gemini", 
        choices=["gemini", "openai", "anthropic"],
        help="The LLM provider to use (default: gemini)."
    )
    parser.add_argument(
        "--chunk-size", 
        type=int, 
        default=4000,
        help="Character chunk size for the text splitter (default: 4000)."
    )
    args = parser.parse_args()

    # --- 2. Get Model and Chain ---
    print(f"Using {args.model} provider...")
    chain = get_model_chain(args.model)

    # --- 3. Read and Split Document ---
    try:
        print(f"--- 1. Reading content from '{args.input_file}' ---")
        with open(args.input_file, 'r') as f:
            input_content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at '{args.input_file}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=200,
        separators=["\n\n\n", "\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(input_content)
    
    print(f"--- 2. Document split into {len(chunks)} physical chunks ---")

    enriched_chunks = ["" for _ in chunks] # Pre-allocate list for results

    # --- 4. Process chunks concurrently ---
    print(f"--- 3. Processing all {len(chunks)} chunks in parallel... ---")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_chunk = {
            executor.submit(process_chunk, chunk_text, i, chain): i 
            for i, chunk_text in enumerate(chunks)
        }
        
        for future in concurrent.futures.as_completed(future_to_chunk):
            chunk_index = future_to_chunk[future]
            try:
                result = future.result()
                enriched_chunks[chunk_index] = result # Store result in correct order
            except Exception as e:
                print(f"Chunk {chunk_index+1} generated an exception: {e}", file=sys.stderr)
                enriched_chunks[chunk_index] = chunks[chunk_index] # Fallback

    # --- 5. Merge and Save ---
    print("--- 4. All chunks processed. Merging... ---")
    final_content = "\n\n".join(enriched_chunks)

    try:
        with open(args.output_file, 'w') as f:
            f.write(final_content)
        print(f"--- 5. Successfully saved enriched output to '{args.output_file}' ---")
    except Exception as e:
        print(f"Error writing to output file: {e}", file=sys.stderr)
        sys.exit(1)

    print("\n--- 6. Process Complete ---")

if __name__ == "__main__":
    main()