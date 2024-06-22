# GSoC 2023

## Introduction
This dataset was developed to address the limitations in publicly available datasets, which often contain only one specific document type(e.g, news) or provide summaries that are disproportionately short (typically 1-2 sentences) regardless of the document length. The goal was to create a dataset that includes a variety of document types and maintains a reasonable summary-to-document length ratio.

## Dataset Creation Process

### Step 1: Document Type Selection

We began by selecting 13 diverse document types, including novels, chat histories, emails, and more. This variety ensures the dataset's applicability across different forms of text processing and summarization tasks.

### Step 2: Topic Generation

For each document type, we generated between 500 to 1000 topics using PaLM API. These topics were stored in text files for further processing. 


### Step 3: Prompt Creation

We iterated through each text file, extracting topics and embedding them into a pre-defined prompt structure. Here's how we structured our prompt creation for hisyoty type:

```
body_parts = helper.file2List('historyEvents.txt')
prompts = []
for body_part in body_parts:
    prompts.append(f"Write a historical document on {body_part.strip()}.\n")
```

For more details about what are those topics and what were the pre-defined prompt strucutre, please check [this](https://github.com/seungjun-green/GSoC/tree/main/Project1/Prompts)

You can check all 13 prompt files at [here](https://github.com/seungjun-green/GSoC/tree/main/Project1/Prompts_text_files)

### Step 4: Document Generation with PaLM API

Using the prompts generated in the previous step, we used the PaLM API to write documents corresponding to each prompt.

### Step 5: Summary Generation

For each document, we also used the PaLM API to generate concise summaries, ensuring that each summary adequately reflects the content of the document.




