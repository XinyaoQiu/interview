# AI Coding Interview Prompts

State your intent to the interviewer, prompt the AI, review the output, and explain the result before moving on. Briefly explain decisions rather than reading each prompt aloud.

## Interviewer Narration and AI Prompts

| Scenario | What to say to the interviewer | Prompt for the AI |
|---|---|---|
| Choose an algorithm | “I’ll ask the AI to check the algorithm choices and complexity before I commit to an approach.” | “Given [requirements], compare suitable algorithms and their time and space complexity. Distinguish exact solutions from heuristics. Do not write code yet.” |
| Review your approach | “I have an approach in mind. I’ll use the AI to check for overlooked cases.” | “My approach is [approach]. Check it against [requirements]. Identify flaws or provide a small counterexample. Do not implement it yet.” |
| Complete the implementation | “I’ve defined the interface and core tests. I’ll ask the AI to fill in the implementation using my approach.” | “Implement the missing methods using [approach]. Preserve my class structure, method signatures, and existing tests. Keep the implementation concise.” |
| Add tests | “I’ll ask the AI for additional edge cases, then verify their expected results.” | “Add tests for edge cases missing from the existing suite. Derive expected results from the requirements, not the implementation. Briefly explain each case.” |
| Understand generated code | “I want to check how this part works before accepting it.” | “Walk through [function] with a small example. Show how the main data structures change and explain the key decisions.” |
| Fix a failing test | “This test fails. I suspect [cause]. I’ll ask the AI to check that and make a targeted fix.” | “This test fails: [test and output]. My hypothesis is [cause]. Identify the root cause and make the smallest fix. Preserve the test expectations unless they contradict the requirements.” |
| Correct a deviation from the plan | “This doesn’t follow the approach I intended. I’ll clarify the constraint and have it corrected.” | “Use [chosen approach] instead of [generated approach], because [reason]. Preserve [interfaces and behavior]. Change only [scope].” |
| Simplify the code | “This adds more structure than we need. I’ll ask the AI to simplify it.” | “Remove unnecessary abstractions and unrelated functionality. Keep the existing interface and required behavior. Do not add dependencies.” |
| Add a feature | “The current tests pass. I’ll extend the implementation with [feature], then check for regressions.” | “Add [feature] to the current implementation. Preserve existing behavior and tests. Add focused tests for the new behavior.” |
| Optimize performance | “The current bottleneck is [operation]. I’ll ask the AI to implement [optimization], then rerun the tests.” | “Replace [operation] with [approach] to improve [complexity]. Preserve observable behavior and existing tests. Explain the resulting time and space complexity.” |

## Python Code Style

Append this to implementation prompts:

> Write concise Python code without type annotations or imports from `typing`. For invalid input, print an error message and return. Do not raise exceptions or add try/except blocks. Do not include a `main()` function or an `if __name__ == "__main__":` block. Only provide the requested classes and functions.
