def processingOutput(LlamaOutput):
    processedOutput = ""

    # Check if the output is wrapped in triple backticks
    if LlamaOutput.startswith("```") and LlamaOutput.endswith("```"):
        processedOutput = LlamaOutput[3:-3]  # Remove the triple backticks
    # Check if the output is wrapped in single backticks
    elif LlamaOutput.startswith("`") and LlamaOutput.endswith("`"):
        processedOutput = LlamaOutput[1:-1]  # Remove the single backticks
    else:
        processedOutput = LlamaOutput  # No change needed if there are no backticks

    # Remove any "sql" keyword if it's mistakenly added
    if processedOutput.lower().startswith("sql"):
        processedOutput = processedOutput[3:].strip()  # Remove the "sql" part

    return processedOutput
