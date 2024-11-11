from transformers import BartForConditionalGeneration, BartTokenizer

def summarize_paragraphs(paragraphs):
    # Combine the paragraphs into a single text block
    text = " ".join(paragraphs)
    
    # Load the BART model and tokenizer
    model_name = "facebook/bart-large-cnn"  # This is the BART model fine-tuned for summarization
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate the summary (output ids)
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=50, max_length=150, length_penalty=2.0, early_stopping=True)
    
    # Decode the summary to text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

# Input: Multiple paragraphs
paragraphs = [
    """Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".""",
    """AI research has been divided into subfields that often fail to communicate with each other. These include AI research on problem-solving, reasoning, knowledge representation, planning, learning, natural language processing, perception, and the ability to move and manipulate objects. The methods used include machine learning, reasoning, and search algorithms, as well as techniques from statistics, optimization, and other fields.""",
    """The success of AI systems has led to the creation of many innovative applications, from autonomous vehicles and robotic systems to advanced language models like GPT-3. Despite these successes, challenges remain in achieving generalized intelligence, ensuring ethical practices in AI development, and mitigating issues like bias in machine learning algorithms."""
]

# Get the summary of the input paragraphs
summary = summarize_paragraphs(paragraphs)
print("Summary:")
print(summary)
