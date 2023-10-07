# Web Knowledge Extraction Research

## Overview

This repository is a collection of subrepos of experiments for web knowledge extraction research.

## Setup

Run `git submodule update --init --recursive` to pull and initialize all submodules
README file from the sub modules would provide more information about the setup.

```
mark-zhang-web-knowledge-extraction/
    - Agent/        state machine agent
    - experiments/  experiments for web knowledge extraction
        -- html2text2.py   modified html2text to extract text from html while perserving the structure
    - framework/    a framework for plug-and-play data adaptors
    - htmlQA/       a small list of questions to benchmark single webpage QA
    - langchain_baseline/    a baseline of popular web QA techniques using langchain
    - Planning/     improved state machine agent as a testbed for planning techniques
```

## Functional Design (Usage)

### Framework

In framework, all adaptors should inherit from the abstract class `Adaptor` and implement the `is_suitable` and `run` methods. The `is_suitable` method should return a boolean indicating whether the adaptor is suitable for the given question and source strategy. The `run` method should return the answer to the question. The `run` method should be an async method.

```python
class Adaptor(ABC):
    """Adapator is the abstract class for all task adaptors."""
    def __init__(self):
        pass

    async def is_suitable(self, question, source_strategy) -> bool:
        """Check if the adaptor is suitable for the given question and source strategy."""

    async def run(self, question, source_strategy) -> str:
        """Run the task."""
```

When loaded into the `Engine` class, the `Engine` class will call the `is_suitable` method of each adaptor seqentially to find the first suitable adaptor for the given question and source strategy. The `Engine` class will then call the `run` method of that adaptor to get the answer to the question. If the `run` method does not return an answer, the `Engine` class will continue to call the `is_suitable` method of the remaining adaptors to find the next suitable adaptor. If no suitable adaptor is found, the `Engine` class will use the default adaptor.

### State Machine Agent & Planning

The state machine agent maintains a finite state machine where each state represent
one step in the process of answering a question. Each state inherits from the abstract class `State`. The run method of each state would create the next state
the state machine should be in. The state machine would run until it reaches the
`FinishedState`

```python
class State(ABC):
    ...

    @abstractmethod
    def run(self) -> None:
        pass
```

## [Video Demo](https://drive.google.com/file/d/1JA3iC7-YPFbTRj-TjTGz__IBrucTKDgE/view?usp=sharing)

## Algorithmic Design

See the README in each subrepo for more details.

## Issues and Future Work

The following are some of the issues we encountered during the development of the module. We also list some of the future work that can be done to improve the module.

### Issues

- The state machine agent is not able to reliably handle complex questions that require multiple steps to answer.
- The state machine agent is not able to handle questions that require multistep reasoning.

- How does the length of context and signal-to-noise ratio affect explicit and implicit hallucination?
- How to collect and utilize task execution and planning experience for LLM-powered agents during inference?
- What is the best form of representation for tracking agent state and reasoning?

## Change log

Summer 2023 (Mark Zhang zz91@illinois.edu)
Implemented state machine, planning, and question answering agents. Created a framework for data adaptors.

## References

- X. Chen, Z. Zhao, et al., “Websrc: a dataset for web-based structural reading comprehension,” 2021.
- Q. Wang, Y. Fang, et al., “Webformer: the web-page transformer for structure information extraction,” 2022.
- P. Veličković, G. Cucurull, et al., “Graph attention networks,” 2018.
- X. Deng, P. Shiralkar, C. Lockard, B. Huang, and H. Sun, “Dom-lm: learning generalizable representations for html documents,” 2022.
- R. Nakano, J. Hilton, et al., “Webgpt: browser-assisted question-answering with human feedback,” 2022
- B. Oguz, X. Chen, et al., “Unik-qa: unified representations of structured and unstructured knowledge for open-domain question answering,” 2022.
- Z. Wang, S. Cai, A. Liu, X. Ma, and Y. Liang, “Describe, explain, plan and select: interactive planning with large language models enables open-world multi-task agents,” 2023.
- C. H. Song, J. Wu, et al., “Llm-planner: fewshot grounded planning for embodied agents with large language models,” 2023.
