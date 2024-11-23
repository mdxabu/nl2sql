def processingOutput(LlamaOutput):
    ProcessedOutput = ""

    if LlamaOutput.startswith("```") and LlamaOutput.endswith("```"):
        ProcessedOutput = LlamaOutput[7:-3]
    elif LlamaOutput.startswith("`") and LlamaOutput.endswith("`"):
        ProcessedOutput = LlamaOutput[1:-1]
    else:
        ProcessedOutput = LlamaOutput

    return ProcessedOutput
     