from tqdm.notebook import tqdm
import pandas as pd
from typing import Optional, List, Tuple
from datasets import Dataset
import matplotlib.pyplot as plt
import datasets

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


pd.set_option(
    "display.max_colwidth", None
)  

# Load dataset (HugguingFace Documentation in this case)
ds = datasets.load_dataset("m-ric/huggingface_doc", split="train")

# Create the raw knowledge base 
RAW_KNOWLEDGE_BASE = [
    Document(page_content=doc["text"], metadata={"source": doc["source"]})
    for doc in tqdm(ds)
]

# Parameters to tune 
# TOP_K - The number of relevant snippets to retrieve
# CHUNK_SIZE - The length of each retrieved snippet (can also be a variable number for each snippet)
# Disclaimer - Too much information (top_k * chunk_size) may cause the Lost-in-the-middle phenomenon

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\n",
    "\n---+\n",
    "\n___+\n",
    "\n\n",
    "\n",
    " ",
    "",
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,  
    add_start_index=True,  
    strip_whitespace=True, 
    separators=MARKDOWN_SEPARATORS,
)

docs_processed = []
for doc in RAW_KNOWLEDGE_BASE:
    docs_processed += text_splitter.split_documents([doc])

