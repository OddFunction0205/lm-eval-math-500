import datasets

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        question = doc["problem"].strip()
        answer = doc["solution"].strip()
        out_doc = {
            "question": question,
            "answer": answer
        }
        return out_doc

    return dataset.map(_process_doc)
