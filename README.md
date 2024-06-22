# GSoC 2023


## Introduction

This dataset was developed to overcome the limitations of publicly available datasets, which typically focus on a single document type (e.g., news) or provide disproportionately short summaries (usually 1-2 sentences), regardless of the document's length. The aim was to construct a dataset encompassing a diverse range of document types while maintaining a reasonable summary-to-document length ratio.



## Dataset Creation Process

### Step 1: Document Type Selection

The project initiated with the selection of 13 diverse document types, including novels, chat histories, emails, and more, to ensure the dataset's applicability across various text processing and summarization tasks.

### Step 2: Topic Generation

For each document type, topics ranging from 500 to 1000 (1~5 words each) were generated using the PaLM API. These topics were stored in text files for subsequent processing. For example, topics for the history document type could include WW1, WW2, and so on.

### Step 3: Prompt Creation
The process involved iterating through each text file, extracting topics, and embedding them into a predefined prompt structure. For instance, for the history document type, prompts were structured as follows:

```
body_parts = helper.file2List('historyEvents.txt')
prompts = []
for body_part in body_parts:
    prompts.append(f"Write a historical document on {body_part.strip()}.\n")
```

For more details about these topics and the pre-defined prompt structure, please check [this](https://github.com/seungjun-green/GSoC/tree/main/Project1/Prompts)

You can check all 13 prompt files [here](https://github.com/seungjun-green/GSoC/tree/main/Project1/Prompts_text_files)

### Step 4: Document Generation with PaLM API

Documents were generated using the PaLM API based on the prompts crafted in the previous step.

### Step 5: Summary Generation

Concise summaries for each document were also crafted using the PaLM API, ensuring that each summary adequately reflected the content of the original documents.


## Making text summarization models

Then created text summarization models by fine-tuning T5 and GPT2. Through experimentation, discovered that fine-tuning GPT-2 with equal loss weighting for original document and summary parts yielded the best results in terms of Rouge-L score. For more details please check [this notebook]().



## Links

[Google Summer of Code 2023 Archive](https://summerofcode.withgoogle.com/archive/2023/projects/qjSsWX86)

